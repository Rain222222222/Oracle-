import ast
import sys

import requests
from pyzabbix import ZabbixAPI

from check_configure import ConfigUre, ConfigError
from logger_module import log_info, log_error, log_warning


class ZabbixApi(object):
    def __init__(self):
        try:
            url = ConfigUre.get('Zabbix', 'zabbix_url')
            user = ConfigUre.get('Zabbix', 'zabbix_user')
            passwd = ConfigUre.get('Zabbix', 'zabbix_password')
            try:
                self.group_names = ast.literal_eval(ConfigUre.get('Zabbix', 'group_names'))
            except (SyntaxError, ValueError) as e:
                print(e)
                sys.exit(1)
        except ConfigError as e:
            print(e)
            sys.exit(1)
        try:
            self.zapi = ZabbixAPI(url)
            self.zapi.login(user, passwd)
        except requests.exceptions.HTTPError as e:
            print(e)
            log_error(e)
            sys.exit(1)

    def get_system_disks(self, user_address):
        try:
            ip_mapping = {}

            host_ip = ip_mapping.get(user_address, user_address)

            group_ids = []

            # 获取指定名称的主机群组的ID
            for group_name in self.group_names:
                groups = self.zapi.hostgroup.get(filter={'name': group_name})
                if groups:
                    group_ids.append(groups[0]['groupid'])
                else:
                    # print(f"No group found with name {group_name}")
                    log_warning(f"$---->>> Zabbix6.0 No group found with name {group_name}")
                    continue

            # 获取指定主机群组内的主机
            hosts = self.zapi.host.get(groupids=group_ids, filter={'ip': host_ip})
            if hosts:
                host_id = hosts[0]['hostid']
                # 获取主机的所有监控项
                items = self.zapi.item.get(hostids=host_id, output=['itemid', 'key_', 'lastvalue'])

                # 存储临时列表和磁盘名、类型的列表
                disk_name = []
                disk_type = []

                def source_data():
                    temp_list_a = []
                    for item in items:
                        if item['key_'].split('[')[0] == 'vfs.fs.inode' or item['key_'].split('[')[0] == 'vfs.fs.size':
                            item_key = item['key_']
                            result = item_key.split("[")[1].split("]")[0].split(",")
                            if result[0] not in disk_name:
                                disk_name.append(result[0])
                            if result[1] not in disk_type:
                                disk_type.append(result[1])
                            temp_list_a.append(item)
                    return temp_list_a

                # 获取过滤后的数据
                source_data = source_data()

                result = []
                for i in disk_name:
                    t_dict = {'name': i}
                    for i1 in disk_type:
                        for j in source_data:
                            name = j['key_'].split('[')[1].split(',')[0]
                            type1 = j['key_'].split('[')[1].split(',')[1].split(']')[0]
                            if i == name and i1 == type1:
                                if type1 == 'total' or type1 == 'used':
                                    # 将字节转换为GB，并四舍五入到整数
                                    t_dict_1 = {i1: round(int(j['lastvalue']) / 1024 / 1024 / 1024, 0)}
                                    t_dict.update(t_dict_1)
                                else:
                                    t_dict_1 = {i1: j['lastvalue']}
                                    t_dict.update(t_dict_1)
                    result.append(t_dict)
                log_info("指标： Zabbix磁盘空间 获取成功。")
                return result
            else:
                # print(f"No host found with IP {host_ip}")
                none_dict = [{
                    'name': 'Zabbix未添加该主机',
                    'total': '无',
                    'used': '无',
                    'pused': '无',
                    'pfree': '无'
                }]
                log_warning(f"$---->>> Zabbix6.0 No host found with IP {host_ip}")
                return none_dict

        except Exception as e:
            log_error(f"+---->>> Operating system disk space acquisition failed:{e}")
