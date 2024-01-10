#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Time      : 2024/1/8 10:31
# @Author    : 我是Rain呀 --  (｡♥ᴗ♥｡) 
# @File      : main_ins.py
# @Software  : PyCharm

# 导入必要的库
import os
import sys
import zipfile
from datetime import datetime

import cx_Oracle
import owncloud
from jinja2 import Template

import ExecuteCommandLibrary
import headers_dict as headers
import zabbix_api
from check_configure import ConfigUre, ConfigError
from logger_module import log_info, log_error

# 全局变量
has_executed = False
conn_str = ''


# 配置类
class ConFig(object):
    try:
        # 从 ConfigUre 中获取配置值
        oc_url = ConfigUre.get('OwnCloud', 'oc_url')
        oc_user = ConfigUre.get('OwnCloud', 'oc_user')
        oc_password = ConfigUre.get('OwnCloud', 'oc_password')
        oc_path = ConfigUre.get('OwnCloud', 'oc_path')
        path_temp = ConfigUre.get('Path', 'path_temp')
        if not os.path.isabs(path_temp):
            print(f'无效的路径: {path_temp}')
            sys.exit(1)
    except ConfigError as e:
        print(e)
        sys.exit(1)


# 自动化巡检类
class AutoIns(ConFig):
    def __init__(self, connect_string: dict):
        super().__init__()
        global has_executed, conn_str
        try:
            # 从输入字典中提取连接详细信息
            self.basi_name = connect_string['business_name']
            self.ipaddr = connect_string['ipaddr']
            self.user = connect_string['username']
            self.passwd = connect_string['password']
            self.port = connect_string['port']
            self.instance = connect_string['instance']

            # 创建连接字符串
            conn_str = self.user + '/' + self.passwd + '@' + self.ipaddr + ':' + self.port + '/' + self.instance
            self.conn = cx_Oracle.connect(conn_str)
            self.cursor = self.conn.cursor()
            log_info(f'成功登录到数据库 -->> {self.ipaddr}')
        except cx_Oracle.DatabaseError as e:
            log_error(f'连接数据库失败 -->> {conn_str} {e}')
            raise
        except KeyError as e:
            log_error(f'登录 URL 字典写错了。{e}')
            raise

        current_time = datetime.now()
        self.formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.current_script_directory = os.path.dirname(os.path.abspath(__file__))
        self.tmpdir = self.path_temp

        self.save_file_name = os.path.join(self.tmpdir, f"{self.ipaddr}.html")
        self.zipfile_name = os.path.join(self.tmpdir, f"{self.formatted_time.split()[0]}.zip")

        if not has_executed:
            self.manage_temp_directory()
            has_executed = True

    def manage_temp_directory(self):
        # 检查 temp 目录是否存在
        if not os.path.exists(self.tmpdir):
            # 如果不存在，创建 temp 目录
            os.makedirs(self.tmpdir)
            log_info(f"目录不存在 创建成功: {self.tmpdir}")
        else:
            # 如果存在，清空 temp 目录下的所有文件
            for file_name in os.listdir(self.tmpdir):
                file_path = os.path.join(self.tmpdir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)
                except Exception as e:
                    log_error(f"无法删除 {file_path}: {e}")
            log_info(f"清空 scratch_file 目录: {self.tmpdir}")

    def close(self):
        # 巡检结束后调用该函数，断开数据库连接
        try:
            self.cursor.close()
            self.conn.close()
        except AttributeError:
            pass

    def main(self):
        # 初始数据，包括基本信息和磁盘使用情况
        data_lists = [
            {
                "name": "基础信息",
                "headers": ('键值', '值'),
                "data": [('数据库业务名称', self.basi_name), ('IP地址', self.ipaddr),
                         ('巡检账户', self.user), ('巡检时间', self.formatted_time)],
            },
            {
                "name": "磁盘使用率",
                "headers": ('分区名', '空闲iNode%', '已使用百分比%', '总大小Gb', '已使用Gb'),
                "data": [tuple(res.values()) for res in zabbix_api.ZabbixApi().get_system_disks(self.ipaddr)],
            }
        ]

        # 获取执行命令库中定义的变量
        var_dict = vars(ExecuteCommandLibrary)
        all_variable_names = [(var, var_dict[var]) for var in var_dict if not var.startswith('__')]
        for var_name, var_value in all_variable_names:
            name = headers.data_dictionary[var_name][0]
            header = headers.data_dictionary[var_name][1]
            try:
                # 执行数据库查询并获取结果
                self.cursor.execute(var_value.strip().upper())
                result = self.cursor.fetchall()
                temp_dicts = {
                    "name": name,
                    "headers": header,
                    "data": [res for res in result],
                }
                log_info(f'指标：{name} 获取成功。')
                data_lists.append(temp_dicts)
            except AttributeError as e:
                log_error(f'指标：{name} 获取失败 --> {str(e)}')
                continue
        self.close()

        # 读取模板文件并渲染 HTML
        with open(os.path.join(self.current_script_directory, 'template.html'), mode='r', encoding='utf-8') as file:
            template_content = file.read()

        template = Template(template_content)
        rendered_html = template.render(tables=data_lists)

        # 打印或保存渲染后的 HTML
        with open(self.save_file_name, mode='w', encoding='utf-8') as f:
            f.write(rendered_html)

        # 将 HTML 文件添加到 ZIP 归档文件
        with zipfile.ZipFile(self.zipfile_name, mode='a') as zip_file:
            zip_file.write(self.save_file_name, os.path.basename(self.save_file_name))

        # 删除 HTML 文件
        os.remove(self.save_file_name)


def upload_files():
    # 上传归档文件到 OwnCloud
    oc = owncloud.Client(ConFig.oc_url)
    oc.login(ConFig.oc_user, ConFig.oc_password)
    try:
        files = os.listdir(ConFig.path_temp)
        for file_name in files:
            if file_name.endswith(".zip"):
                director_file = os.path.join(ConFig.path_temp, file_name)
                oc.put_file(f'{ConFig.oc_path.strip("/")}/{file_name}', director_file)
                os.remove(director_file)
                log_info(f"+---->>> {file_name} 成功上传到 OwnCloud")
    except owncloud.owncloud.HTTPResponseError as e:
        log_error(f"$---->>> 上传到 OwnCloud 失败: {e}")
    except Exception as e:
        log_error(f"$---->>> 上传到 OwnCloud 失败: {e}")


if __name__ == '__main__':
    import user_pass

    # 遍历 user_pass.source_data 并执行巡检
    for info in user_pass.source_data:
        try:
            auto_ins_instance = AutoIns(info)
            auto_ins_instance.main()
        except cx_Oracle.DatabaseError:
            continue
        except KeyError:
            continue

    # 巡检结束后上传文件到 OwnCloud
    upload_files()
