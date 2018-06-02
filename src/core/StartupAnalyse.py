# 本文件用于分析系统启动过程，生成启动过程svg，获取启动时间，获取所有系统服务并设置是否可以自启动等功能
import os


def getStartupInfo():
    res = dict()
    res['boot_time'] = getBootTime()
    res['critical_chain'] = getCriticalChain()
    return res

def getStartupSVG():
    res = dict()
    res["svg"] = getSvg()
    return res


def getBootTime():
    with os.popen('systemd-analyze') as fd:
        res = 0
        for line in fd:
            res = line.split("=")[1]
            res = res.split("s")[0]
            buf = res.split("min")
            totalTime = float(buf[0])*60+float(buf[1])
    return round(totalTime,1)

def getCriticalChain():
    with os.popen('systemd-analyze critical-chain') as fd:
        res = ""
        for line in fd:
            res += line
    return res

def getSvg():
    with os.popen('systemd-analyze plot') as fd:
        res = ""
        for line in fd:
            res += line
    return res




if __name__ == '__main__':
    print(getBootTime())
    print(getCriticalChain())
    print(getSvg())
