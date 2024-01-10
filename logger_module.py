#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Time      : 2024/1/8 10:54
# @Author    : 我是Rain呀 --  (｡♥ᴗ♥｡) 
# @File      : logger_module.py
# @Software  : PyCharm

import logging
import os
import sys

from check_configure import ConfigUre, ConfigError

try:
    # 获取日志文件路径配置
    log_path = ConfigUre.get('Logger', 'path')

    # 定义创建目录的函数
    def create_directory(directory_path):
        if os.path.isabs(directory_path):
            os.makedirs(directory_path, exist_ok=True)
        else:
            print(f'Invalid path: {directory_path}')
            sys.exit(1)


    # 创建日志目录
    create_directory(log_path)

except ConfigError as e:
    print(e)
    sys.exit(1)

# 将日志文件路径和文件名合并
log_path = os.path.join(log_path, 'result.log')

# 配置 logging 模块
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_debug(message):
    """记录调试级别的日志"""
    logging.debug(message)


def log_info(message):
    """记录信息级别的日志"""
    logging.info(message)


def log_warning(message):
    """记录警告级别的日志"""
    logging.warning(message)


def log_error(message):
    """记录错误级别的日志"""
    logging.error(message)


def log_critical(message):
    """记录严重错误级别的日志"""
    logging.critical(message)
