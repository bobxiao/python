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

v_list = [('2016-01-31-16-24-20', 'qlphotspt', '28:E3:1F:50:59:EE', 'NULL', '10.0.0.177', '10.0.0.177', '3h56m13s', 'hs-N', 'true', 'cap002', 'false', 'NULL', '68150', '39086', '45726881', '4543248', 'TCP :50180 -> 10.0.0.1:80', '5m', '1m3s', '1m3s', '*1A3'), ('2016-01-31-16-24-20', 'qlphotspt', '94:E9:6A:62:93:1C', 'NULL', '10.0.0.50', '10.0.0.50', '1h59m19s', 'hs-N', 'true', 'cap005', 'false', 'NULL', '391178', '205768', '574588218', '14621669', 'UDP :59904 -> 10.0.0.1:53', '5m', '1s', '1s', '*2EE'), ('2016-01-31-16-24-20', 'qlphotspt', 'DC:2B:2A:30:F9:FB', 'NULL', '10.0.0.40', '10.0.0.40', '1h53m31s', 'hs-N', 'true', 'cap005', 'false', 'NULL', '38032', '34370', '18595714', '10925663', 'TCP :61483 -> 125.39.247.224:443', '5m', '22s', '22s', '*2F5'), ('2016-01-31-16-24-20', 'qlphotspt', '2C:28:2D:FD:11:1C', 'true', '10.0.0.78', '10.0.0.78', '1h29m42s', 'hs-N', 'false', 'cap061-2', 'false', '163.177.86.108:80', '1279', '1531', '166043', '158241', 'ICMP type<3> code<3> to 10.0.0.1', '5m', '2m47s', '2m47s', '*340'), ('2016-01-31-16-24-20', 'qlphotspt', '80:41:4E:31:F4:E6', 'true', '10.0.0.144', '10.0.0.144', '1h23m37s', 'hs-N', 'false', 'cap017-2', 'false', '220.249.243.39:80', '2510', '2869', '241956', '423899', 'UDP :37278 -> 10.0.0.1:53', '5m', '0s', '0s', '*347'), ('2016-01-31-16-24-20', 'qlphotspt', 'A4:31:35:EE:E7:B2', 'NULL', '10.0.0.65', '10.0.0.65', '45m43s', 'hs-N', 'true', 'cap033', 'false', 'NULL', '172129', '135051', '253561763', '9326353', 'UDP :60577 -> 10.0.0.1:53', '5m', '7s', '7s', '*399'), ('2016-01-31-16-24-20', 'qlphotspt', 'F4:8E:92:D3:E1:28', 'NULL', '10.0.0.27', '10.0.0.27', '29m45s', 'hs-N', 'true', 'cap002', 'false', 'NULL', '962', '1136', '634350', '172342', 'UDP :27847 -> 10.0.0.1:53', '5m', '1m30s', '17s', '*3AC'), ('2016-01-31-16-24-20', 'qlphotspt', 'BC:3A:EA:DF:C4:A8', 'NULL', '10.4.0.77', '10.4.0.77', '27m14s', 'hs-S', 'true', 'cap047', 'false', 'NULL', '160', '226', '45026', '32541', 'ARP reply to 10.4.0.1', '5m', '4s', '4s', '*3B3'), ('2016-01-31-16-24-20', 'qlphotspt', '00:22:F4:8D:59:51', 'true', '10.0.0.73', '10.0.0.73', '4m39s', 'hs-N', 'false', 'cap016', 'false', 'NULL', '73', '68', '10475', '7602', 'UDP :26014 -> 10.0.0.1:53', '5m', '4m25s', '4m25s', '*3C2'), ('2016-01-31-16-24-20', 'qlphotspt', 'EC:89:F5:D2:D4:3A', 'true', '10.0.0.164', '10.0.0.164', '3m39s', 'hs-N', 'false', 'cap016', 'false', 'NULL', '131', '142', '17887', '52801', 'UDP :28024 -> 10.0.0.1:53', '5m', '44s', '44s', '*3C5'), ('2016-01-31-16-24-20', 'qlphotspt', '9C:3A:AF:6D:34:9A', 'true', '10.0.0.9', '10.0.0.9', '2m43s', 'hs-N', 'false', 'cap016', 'false', '163.177.71.211:80', '225', '246', '30698', '33746', 'TCP :50571 -> 112.90.74.148:443', '5m', '0s', '0s', '*3C6'), ('2016-01-31-16-24-20', 'qlphotspt', '6C:25:B9:44:AC:B4', 'NULL', '10.0.0.163', '10.0.0.163', '2m8s', 'hs-S', 'true', 'cap058', 'false', 'NULL', '423', '465', '27918', '32122', 'TCP :60461 -> 163.177.86.108:80', '5m', '3s', '3s', '*3C9'), ('2016-01-31-16-24-20', 'qlphotspt', '4C:5E:0C:B0:55:5B', 'true', '10.0.10.8', '10.0.10.8', '1m44s', 'hs-B', 'false', 'cap043', 'false', 'NULL', '15', '17', '792', '1202', 'TCP :48891 -> 115.28.135.23:1723', '5m', '1s', '1s', '*3CA'), ('2016-01-31-16-24-20', 'qlphotspt', '50:FC:9F:A8:35:87', 'NULL', '10.0.0.53', '10.0.0.53', '1m36s', 'hs-N', 'true', 'cap016', 'false', 'NULL', '544', '671', '103002', '89781', 'UDP :38686 -> 119.6.6.6:53', '5m', '13s', '13s', '*3CB')]
# gd = Getdata(host,port,user,pwd)
# v_list = gd.getdata()
# print v_list
while True:
    sI = Sqlinsert(dbhost,dbuser,dbpwd,dbport,dbname,dbtable,v_list)
    sI.sqlinsert()
    print 'OK'

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