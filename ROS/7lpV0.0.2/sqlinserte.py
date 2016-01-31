# -*- coding: utf-8 -*-f
# 向指定数据库注入数据

import MySQLdb


class Sqlinsert:

    def __init__(self, dbHost, dbUser, dbPwd, dbPort, dbDb, dbTable, v_list):
        self.dbHost = dbHost
        self.dbUser = dbUser
        self.dbPwd = dbPwd
        self.dbPort = int(dbPort)
        self.dbDb = dbDb
        self.dbTable = dbTable
        self.v_list = v_list

    def sqlinsert(self):
        conn = MySQLdb.connect(host=self.dbHost, \
                               user=self.dbUser, \
                               passwd=self.dbPwd, \
                               db = self.dbDb,\
                               port=self.dbPort)
        cur = conn.cursor()
        cur.execute("show databases")

        sql = "insert into test2x (time,host,mac,DHCP,address,to_address,uptime,server,\
        bypassed,bridge_port,authroized,http_proxy,packets_out,\
        packets_in,bytes_out,bytes_in,found_by,\
        idle_timeout,idle_time,hostdead_time,idnum)  values(%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"
        try:
            cur.executemany(sql,self.v_list)
        except Exception as e:
            print ("执行MySQL时出错：%s"%(e))
        finally:
            cur.close()
            conn.close()