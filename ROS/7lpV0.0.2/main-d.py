#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, time
import ConfigParser, string
from daemon import Daemon
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

v_list = 1234
class MyDaemon(Daemon):
    def run(self):

        while True:
            # gD = Getdata(host,port,user,pwd)
            # v_list = gD.getdata()
            print v_list

            # sI = Sqlinsert(dbhost,dbuser,dbpwd,dbport,dbname,dbtable,v_list)
            # sI.sqlinsert()
            # time.sleep(2)
            # timenow = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            # count = open('/tmp/count.txt','a')
            # count.write('\n')
            # # count.write(str(VLIST))
            # # f_get.write('\n')
            # count.write('================================')
            # count.write(timenow)
            # count.write('================================')
            # count.write('\n')
            # count.close()


if __name__ == "__main__":
	daemon = MyDaemon('/tmp/rosapi2x/daemon-example.pid')
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
