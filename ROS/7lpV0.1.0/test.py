#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser, string
# from lib.daemon import Daemon
from getdata import Getdata
from sqlinserte import MySQLdb



# 准备配置文件
conf = ConfigParser.ConfigParser()
conf.read("./cfg/7liping-data.cfg")
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

while True:
    gd = Getdata(host,port,user,pwd)
    v_list = gd.getdata()
    sI = MySQLdb(dbhost,dbuser,dbpwd,dbport,dbname,dbtable,v_list)
    sI.sqlLogin()
    sI.instData()
    print v_list
# sI = Sqlinsert(dbhost,dbuser,dbpwd,dbport,dbname,dbtable,v_list)
# sI.sqlinsert()

    # def __init__(self,r1Host="124.161.108.46",r1Port=20001,r1User="api",r1Pwd="api",cmd=""):
    #     self.r1Host=r1Host
    #     self.r1Port=r1Port
    #     self.r1User=r1User
    #     self.r1Pwd=r1Pwd
    #
    # def getdata(self):
    #     '''从rosAPI获取数据'''
    #     api1 = Core(self.r1Host, self.r1Port)
    #     api1.login(self.r1User, self.r1Pwd)
    #
    #     '''获取hotspot数据'''
    #     hptdata = (api1.response_handler(api1.talk(["/ip/hotspot/host/print"])))