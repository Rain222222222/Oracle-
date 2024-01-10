#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Time      : 2024/1/8 16:58
# @Author    : 我是Rain呀 --  (｡♥ᴗ♥｡) 
# @File      : user_pass.py
# @Software  : PyCharm

source_data = [
    {"business_name": "投资数据库", "ipaddr": "10.6.170.88", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "investdb"},
    {"business_name": "数据计算平台轨迹库", "ipaddr": "10.0.74.155", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "lckh"},
    {"business_name": "阿拉丁生产数据库", "ipaddr": "10.5.2.112", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "alddb"},
    {"business_name": "数据计算平台数据库", "ipaddr": "10.6.74.181", "username": "zabbix", "password": "zabbix", "port": "1522", "instance": "bidb"},
    {"business_name": "保单登记平台三期库", "ipaddr": "10.5.2.55", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "bddjpt3"},
    {"business_name": "保单登记3期数据库", "ipaddr": "10.5.2.59", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "bddj3"},
    {"business_name": "风控系统数据库", "ipaddr": "10.5.2.37", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "riskdb"},
    {"business_name": "反洗钱生产数据库", "ipaddr": "10.5.2.101", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "nbaml"},
    {"business_name": "客户风险系统数据库", "ipaddr": "10.5.2.43", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "oracle"},
    {"business_name": "投资自主估值", "ipaddr": "10.6.170.30", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "fepdb"},
    {"business_name": "投研系统数据库", "ipaddr": "10.6.170.39", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "sirm"},
    {"business_name": "估值数据库", "ipaddr": "10.6.170.89", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "apprdb"},
    {"business_name": "风险评估数据库", "ipaddr": "10.6.170.90", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "wcdb"},
    {"business_name": "衡泰信评系统", "ipaddr": "10.6.170.127", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "orcl"},
    {"business_name": "大数据平台生产数据库", "ipaddr": "10.5.2.125", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "infodb"},
    {"business_name": "OA数据库", "ipaddr": "10.5.2.46", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "oadb"},
    {"business_name": "双录数据库", "ipaddr": "10.5.2.34", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "kldrsdb"},
    {"business_name": "全前置机生产数据库", "ipaddr": "10.5.2.161", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "bqlis"},
    {"business_name": "审计系统数据库", "ipaddr": "10.5.2.33", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "shenjiprd"},
    {"business_name": "驾驶舱生产数据库1", "ipaddr": "10.5.2.95", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "mgmtrpt"},
    {"business_name": "费控数据库", "ipaddr": "10.5.2.57", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "orcl"},
    {"business_name": "实名查验数据库", "ipaddr": "10.5.2.206", "username": "zabbix", "password": "zabbix", "port": "1528", "instance": "prcr"},
    {"business_name": "SAP旧准则", "ipaddr": "10.5.2.38", "username": "zabbix", "password": "zabbix", "port": "1527", "instance": "klt"},
    {"business_name": "产EAST数据库01", "ipaddr": "10.5.2.130", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "east"},
    {"business_name": "健管数据库", "ipaddr": "10.5.2.36", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "jgxtdb"},
    {"business_name": "北京健康险数据库", "ipaddr": "10.5.2.70", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "rpdb"},
    {"business_name": "数据地图数据库", "ipaddr": "10.5.2.150", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "datamap"},
    {"business_name": "新一代统信数据库", "ipaddr": "10.5.2.23", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "circ"},
    {"business_name": "保单险种现价数据库", "ipaddr": "10.5.2.103", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "cvs"},
    {"business_name": "短信数据库", "ipaddr": "10.5.2.45", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "orcl"},
    {"business_name": "短信平台数据库", "ipaddr": "10.5.2.66", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "smsdb"},
    {"business_name": "短信数据库", "ipaddr": "10.5.2.44", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "klsms"},
    {"business_name": "销管数据库", "ipaddr": "10.5.2.56", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "KLSMISSTAND"},
    {"business_name": "数据交换平台数据库", "ipaddr": "10.6.74.25", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "dxpdb"},
    {"business_name": "万得资讯数据库", "ipaddr": "10.6.142.144", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "windoracle"},
    {"business_name": "SAP系统", "ipaddr": "10.6.74.51", "username": "zabbix", "password": "zabbix", "port": "1527", "instance": "PRD"},
    {"business_name": "资金数据库生产", "ipaddr": "10.6.74.65", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "klzjrac"},
    {"business_name": "核心数据库", "ipaddr": "10.5.2.3", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "lisdb"},
    {"business_name": "出单数据库", "ipaddr": "10.5.2.6", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "uwsdb"},
    {"business_name": "生产genesys数据库", "ipaddr": "10.5.2.72", "username": "c##zabbix", "password": "zabbix", "port": "1521", "instance": "orcl"},
    {"business_name": "再保系统数据库", "ipaddr": "10.5.2.89", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "ris"},
    {"business_name": "财汇数据库", "ipaddr": "10.6.142.143", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "caihui"},
    {"business_name": "税优数据库", "ipaddr": "10.5.2.32", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "sydb"},
    {"business_name": "移动展业生产库", "ipaddr": "10.5.2.58", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "mosale"},
    {"business_name": "口袋昆仑生产", "ipaddr": "10.6.74.82", "username": "zabbix", "password": "zabbix", "port": "1521", "instance": "oaracdb"}
]
