#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2024/1/9 17:31
# @Author    : 我是Rain呀 --  (｡♥ᴗ♥｡)
# @File      : check_configure.py
# @Software  : PyCharm

import configparser


class ConfigError(Exception):
    """自定义异常类，用于处理配置相关错误"""
    pass


class ConfigUre:
    # 配置文件路径
    CONFIG_FILE_PATH = 'config.conf'

    # 初始化配置解析器并读取配置文件
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)

    @classmethod
    def get(cls, section, key):
        """
        获取配置项的值

        Parameters:
        - section (str): 配置文件中的节名
        - key (str): 配置项的键名

        Returns:
        - str: 配置项的值

        Raises:
        - ConfigError: 配置相关错误的自定义异常
        """
        try:
            res = cls.config.get(section, key)
            return res
        except configparser.NoOptionError:
            # 当配置项不存在时抛出 ConfigError 异常
            raise ConfigError(f"Option '{key}' not found in the '{section}' section.")
        except configparser.NoSectionError:
            # 当配置节不存在时抛出 ConfigError 异常
            raise ConfigError(f"Section '{section}' not found.")
        except (SyntaxError, ValueError) as er:
            # 处理配置文件中值的语法错误或类型错误
            raise ConfigError(f"Error in parsing the configuration file: {er}")
