#DashInfo包括CPU负载、内存占用、磁盘使用

import os
import psutil
import time

lastIn = 0
lastOut = 0
lastTime = time.time()

def getDashInfo():


    dashInfo = dict()
    #CPU info
    dashInfo['cpu_percent']=psutil.cpu_percent(interval=0.2)
    dashInfo['cpu_count']=psutil.cpu_count()
    dashInfo['cpu_freq']=psutil.cpu_freq()

    #Mem Info
    dashInfo['mem'] = psutil.virtual_memory()

    #Disk Info
    dashInfo['disk_usage']=psutil.disk_usage("/")
    dashInfo['disk_io']=psutil.disk_io_counters()
    #Net Info
    dashInfo['net_io']=psutil.net_io_counters()
    dashInfo = caculateNetSpeed(dashInfo)
    return dashInfo

def getCPUInfo():
    dashInfo = dict()
    # CPU info
    dashInfo['cpu_percent'] = psutil.cpu_percent(interval=0.1)
    dashInfo['cpu_count'] = psutil.cpu_count()
    dashInfo['cpu_freq'] = psutil.cpu_freq()
    return dashInfo

def getMemInfo():
    dashInfo = dict()
    # Mem Info
    dashInfo['mem'] = psutil.virtual_memory()
    return dashInfo

def getNetSpeed():
    dashInfo = dict()
    dashInfo['net_io'] = psutil.net_io_counters()
    dashInfo = caculateNetSpeed(dashInfo)
    return dashInfo

def caculateNetSpeed(dashInfo):
    netInfo = dashInfo['net_io']
    thisIn = netInfo.bytes_recv
    thisOut = netInfo.bytes_sent

    global lastIn,lastOut,lastTime
    devIn = thisIn - lastIn
    devOut = thisOut - lastOut
    thisTime = time.time()
    devTime = thisTime - lastTime

    if lastIn == 0 or lastOut == 0:#首次计算，忽略掉
        devIn = 0
        devOut = 0

    lastIn = thisIn
    lastOut = thisOut
    lastTime = thisTime

    dashInfo['net_speed_in'] = round(1 / 1024 * devIn / devTime, 1)
    dashInfo['net_speed_out'] = round(1 / 1024 * devOut / devTime, 1)
    return dashInfo


if __name__ == '__main__':
    while True:
        info = getDashInfo()
        print(info)
        #print(info['net_if'])

