#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser, string
# from lib.daemon import Daemon
from getdata import Getdata
from sqlinserte import Sqlinsert



# 准备配置文件
conf = ConfigParser.ConfigParser()
conf.read("7liping-data.cfg")
# 设备的配置数据
host = conf.get('device1', 'host')
port = string.atoi(conf.get('device1', 'port'))
user = conf.get('device1', 'user')
pwd = conf.get('device1', 'password')
# 数据库的配置数据
dbhost = conf.get('db_mysql', 'host')
dbport = (conf.get('db_mysql', 'port'))
dbuser = conf.get('db_mysql', 'user')
dbpwd = conf.get('db_mysql', 'password')
dbname = conf.get('db_mysql', 'db')
dbtable = conf.get('db_mysql','table')


gd = Getdata(host,port,user,pwd)
v_list = gd.getdata()
print v_list
# sI = Sqlinsert(dbhost,dbuser,dbpwd,dbport,dbname,dbtable,v_list)
# sI.sqlinsert()