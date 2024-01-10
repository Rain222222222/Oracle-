#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Time      : 2024/1/8 10:23
# @Author    : 我是Rain呀 --  (｡♥ᴗ♥｡) 
# @File      : ExecuteCommandLibrary.py
# @Software  : PyCharm

version = """
    select * from v$version
"""

library_cache = """
    select (1-(sum(getmisses)/sum(gets))) * 100 "Hit Ratio" from v$rowcache
"""

buffer_pool = """
    SELECT NAME, PHYSICAL_READS, DB_BLOCK_GETS, CONSISTENT_GETS,
        1 - (PHYSICAL_READS / (DB_BLOCK_GETS + CONSISTENT_GETS)) "Hit Ratio"
    FROM V$BUFFER_POOL_STATISTICS
"""


instance_memory_usage = """
    select name,bytes/1024/1024 as "MB",RESIZEABLE from v$sgainfo
"""

instance_sga_usage = """
    select name,type,value from v$parameter where name like '%sga%'
"""

archive_mode = """
    SELECT log_mode FROM v$database
"""

parameter_all = """
    select num,name,value from v$parameter where isdefault='FALSE'
"""

tablespace_usage = """
    select TABLESPACE_NAME,
         round(used_space * 8 / 1024 / 1024, 2) USED_GB,
         round(TABLESPACE_SIZE * 8 / 1024 / 1024, 2) MAX_GB,
         round((TABLESPACE_SIZE - used_space) * 8 / 1024 / 1024, 2) FREE_GB,
         round(USED_PERCENT, 2) as USED_PERCENT
    from dba_tablespace_usage_metrics
    order by 5
"""

data_files = """
     select 
        TABLESPACE_NAME, 
        file_name,
        bytes/1024/1024,
        status,
        autoextensible 
     from dba_data_files 
     order by 1
"""

logfile = """
    select a.group#,b.thread#,b.bytes,a.member,b.status 
    from v$logfile a,v$log b 
    where a.group#=b.group# 
    order by b.thread#
"""

controlfile = """
     select NAME,IS_RECOVERY_DEST_FILE,BLOCK_SIZE,FILE_SIZE_BLKS from v$controlfile
"""

ash_img = """
    select *
    from (select inst_id,
                   rank() over(partition by inst_id order by cnt desc) rk,
                   event,
                   cnt
              from (select ash.INST_ID, ash.EVENT, count(*) CNT
                      from gv$active_session_history ash
                     where ash.SAMPLE_TIME > sysdate - 1 / 24 / 60 * 30
                       and event is not null
                     group by ash.INST_ID, ash.EVENT))
    where rk <= 10
"""

sga_parameter = """
    select * from v$sgastat
"""
