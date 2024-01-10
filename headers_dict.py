#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Time      : 2024/1/8 11:58
# @Author    : 我是Rain呀 --  (｡♥ᴗ♥｡)
# @File      : headers_dict.py
# @Software  : PyCharm

data_dictionary = {
    "tablespace_usage": ['表空间使用情况', ('表空间名', '已使用', '总大小', '剩余空间', '已使用%')],
    "data_files": ["数据文件详情", ('表空间名', '文件路径', '文件大小Mb', '状态', '自动拓展')],
    "version": ["数据库版本", ('版本信息',)],
    "instance_memory_usage": ["实例内存使用情况", ('NAME', 'MB', 'RESIZEABL')],
    "instance_sga_usage": ["SGA使用情况", ('Name', 'TYPE', 'VALUE')],
    "archive_mode": ["归档模式", ('归档模式',)],
    "parameter_all": ["整体参数配置", ('序号', '名称', '值')],
    "sga_parameter": ["SGA各项参数", ('池Pool', '名称Name', '大小Bytes')],
    "controlfile": ["控制文件", ('NAME', 'IS_RECOVERY_DEST_FILE', 'BLOCK_SIZE', 'FILE_SIZE_BLKS')],
    "logfile": ["Redo日志应用情况", ('GROUP#', 'THREAD#', 'BYTES', 'MEMBER', 'STATUS')],
    "ash_img": ["30分钟ASH", ('INST_ID', 'RK', 'EVENT', 'COUNT')],
    "library_cache": ['Library Cache命中率', ('Hit Ratio',)],
    "buffer_pool": ['buffer pool命中率', ('NAME', 'PHYSICAL_READS', 'DB_BLOCK_GETS', 'CONSISTENT_GETS', 'Hit Ratio')]
}
