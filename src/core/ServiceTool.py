# 主要实现对Service的查看、管理
import os
import re


class ServiceTool:
    def __init__(self):
        self.services = list()

    def getServices(self):
        with os.popen('systemctl list-unit-files -t service -a --state=enabled,disabled') as fd:
            for line in fd:
                if re.match(".*[^@].service",line):
                    service = dict()
                    buf = line.split(" ")
                    service['name'] = buf[0]
                    service['isEnabled'] = self.serviceIsEnabled(buf[0])
                    service['description'] = self.getServiceDescription(buf[0])
                    service['isActive'] = self.serviceIsActive(buf[0])
                    self.services.append(service)
                    #print(service)
        return self.services


    def getServiceDescription(self,serviceName):
        with os.popen('systemctl cat '+serviceName) as fd:
            for line in fd:
                if re.match("^Description=",line):
                    res = line.split("=")[1]
                    res = res.split("\n")[0]
                    return res

    def serviceIsActive(self,serviceName):
        with os.popen('systemctl is-active '+serviceName) as fd:
            for line in fd:
                res = line.split("\n")[0]
                return res

    def serviceIsEnabled(self,serviceName):
        with os.popen('systemctl is-enabled '+serviceName) as fd:
            for line in fd:
                res = line.split("\n")[0]
                return res

    # status:boolean
    def changeServiceStatus(self,serviceName,status=True):
        opr = "enable"
        if not status:
            opr = "disable"
        os.system('systemctl '+opr+" "+serviceName)

    def changeServiceActive(self,serviceName,status=True):
        opr = "start"
        if not status:
            opr = "stop"
        os.system('systemctl '+opr+" "+serviceName)

if __name__ == '__main__':
    tool = ServiceTool()
    tool.getServices()