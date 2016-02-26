#!/usr/bin/env python
# encoding: utf-8


"""
@version: V2.6
@author: bobxiao
@license: Apache Licence
@contact: wolfxb2005@gmail.com
@software: PyCharm
@file: 1.py
@time: 2016/2/23 17:38
@brife:

"""
import sys, time
import ConfigParser, string
from daemon import Daemon
import MySQLdb
from getdata import Getdata
from sqlinserte import Sqldb

 # 准备配置文件
conf = ConfigParser.ConfigParser()
conf.read("/root/ROS/7lpV0.1.0/cfg/7liping-data.cfg")
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
# sql = conf.get('db_mysql', 'sql')


sql_hsp_col = "insert into %s (time,host,mac,DHCP,address,to_address,uptime,server,\
        bypassed,bridge_port,authroized,http_proxy,packets_out,\
        packets_in,bytes_out,bytes_in,found_by,\
        idle_timeout,idle_time,hostdead_time,idnum)  values(%s)"
table = 'text2x'
sql_test2x = sql_hsp_col %("test2x",'%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s')

class MyDaemon(Daemon):
    def run(self):

        while True:
            gd = Getdata(host,port,user,pwd)
            v_list = gd.getdata()
            # print v_list
            # print sql_test2x
            sI = Sqldb(dbhost,dbuser,dbpwd,dbport,dbname)
            sI.sqlLogin()
            sI.instData(sql_test2x,v_list)

if __name__ == "__main__":
    daemon = MyDaemon('/root/ROS/7lpV0.1.0/log/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

class Sql:

    def loginSql(self):
        def __init__(self, dbHost, dbUser, dbPwd, dbPort, dbDb, dbTable, v_list):
            self.dbHost = dbHost
            self.dbUser = dbUser
            self.dbPwd = dbPwd
            self.dbPort = int(dbPort)
            self.dbDb = dbDb
            self.dbTable = dbTable
            self.v_list = v_list

    def sqlLogin(self):
        self.conn = MySQLdb.connect(host=self.dbHost, \
                               user=self.dbUser, \
                               passwd=self.dbPwd, \
                               db = self.dbDb,\
                               port=self.dbPort)
        self.cur = self.conn.cursor()

    def insertdata(self,sql,v_list):
        try:
            self.cur.executemany(sql,v_list)
        except Exception as e:
            print ("执行MySQL时出错：%s"%(e))
        self.closeCur()
        self.closeSQL()

    def closeCur(self):
        self.cur.close()
    def closeSQL(self):
        self.conn.close()