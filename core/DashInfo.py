#DashInfo包括CPU负载、内存占用、磁盘使用

import os
import psutil
import time


def getDashInfo():
    dashInfo = dict()
    #CPU info
    dashInfo['cpu_percent']=psutil.cpu_percent(interval=0.2)
    dashInfo['cpu_count']=psutil.cpu_count()
    dashInfo['cpu_freq']=psutil.cpu_freq()

    #Mem Info
    dashInfo['mem']=psutil.virtual_memory()

    #Disk Info
    dashInfo['disk_usage']=psutil.disk_usage("/")
    dashInfo['disk_io']=psutil.disk_io_counters()
    #Net Info
    dashInfo['net_if']=psutil.net_if_stats()
    return dashInfo


if __name__ == '__main__':
    while True:
        info = getDashInfo()
        print(info)
        #print(info['net_if'])

