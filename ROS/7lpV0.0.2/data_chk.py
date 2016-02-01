# -*- coding: utf-8 -*-
'''
这个脚本是用来解决ROS数据获取写入脚本的不稳定而做的临时解决方案
通过linux的crontab来定期执行该脚本
检查数据存储表的增长是否停止
如果停止增长假定脚本卡死
通过os.system()执行shell命令stop、start守护进程
'''

import MySQLdb ,os
import ConfigParser, string

# 准备配置文件
conf = ConfigParser.ConfigParser()
conf.read("7liping-data.cfg")
# 数据库的配置数据
dbhost = conf.get('db_mysql', 'host')
dbport = (conf.get('db_mysql', 'port'))
dbuser = conf.get('db_mysql', 'user')
dbpwd = conf.get('db_mysql', 'password')
dbname = conf.get('db_mysql', 'db')
dbtable = conf.get('db_mysql','table')

