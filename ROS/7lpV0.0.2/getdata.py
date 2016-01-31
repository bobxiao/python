# -*- coding: utf-8 -*-

import time
from RosAPI import Core


class Getdata:

    def __init__(self, r1Host, r1Port, r1User, r1Pwd):
        self.r1Host = r1Host
        self.r1Port = r1Port
        self.r1User = r1User
        self.r1Pwd = r1Pwd

    def getdata(self):
        '''从rosAPI获取数据'''
        api1 = Core(self.r1Host, self.r1Port)
        api1.login(self.r1User, self.r1Pwd)

        '''获取hotspot数据'''
        hptdata = (api1.response_handler(api1.talk(["/ip/hotspot/host/print"])))

        '''获取设备数据'''
        devname = (api1.response_handler(api1.talk(['/sys/identity/print'])))

        # print devname

        '''获取当前时间'''
        timenow = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

        '''定义处理数据所需的list'''
        keyslist = ['mac-address', 'DHCP', 'address', 'to-address', 'uptime', 'server', \
                    'bypassed', 'bridge-port', 'authorized', 'http-proxy', 'packets-out' \
            , 'packets-in', 'bytes-out', 'bytes-in', 'found-by', \
                    'idle-timeout', 'idle-time', 'host-dead-time', '.id']
        vlist = []
        VLIST = []

        '''数据排版成需要的格式'''
        for i in hptdata:
            vlist.append(timenow)
            vlist.append(devname[0]['name'])
            for j in keyslist:
                if j in i.keys():
                    vlist.append(i[j])
                else:
                    vlist.append('NULL')
            vtuple = tuple(vlist)
            vlist = []
            VLIST.append(vtuple)

        return VLIST
