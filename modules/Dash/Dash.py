import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from modules.GeneralDaemonThread import GeneralDaemonThread

from modules.Dash.design import Ui_DashForm
import core.DashInfo as DashInfo


class DashWidget(QtWidgets.QWidget, Ui_DashForm):
    def __init__(self,parent = None):
        super(DashWidget,self).__init__(parent)
        self.setupUi(self)
        self.myThread = DashThread(parent=self)
        self.myThread.sinOut.connect(self.receiveDashInfo)
        self.myThread.start()
        #print("Dash init")

    def show(self):
        super(DashWidget, self).show()
        self.myThread.setActive(True)
        self.initSysInfo()
        #print("show Dash")
        
    def hide(self):
        super(DashWidget, self).hide()
        self.myThread.setActive(False)

    def initSysInfo(self):
        sysInfo = SystemInfo()
        cpuInfo = sysInfo.getCpu()
        buf = "Computer Name: "+sysInfo.getHostname()["hostname"] + "<br>" \
            + "GCC version: "+sysInfo.getGccVersion()["gccVersion"] + "<br>" \
            + "Linux version: "+sysInfo.getOsVersion()["osver"] + "<br>"\
            + "CPU type:" + cpuInfo["cpu_model"]+"<br>"\
            + "CPU cores:"+str(cpuInfo["cpu_num"])
        self.systemInfo.setText(buf)

    def receiveDashInfo(self,payload):
        #print("receive:"+str(payload))
        cpuPercent = int(payload["cpu_percent"])
        if cpuPercent>=100:
            cpuPercent = 99
        self.lcdCpu.display(cpuPercent)
        #print(cpuPercent)
        memPercent = int(payload['mem'].percent)
        if memPercent>=100:
            memPercent = 99
        self.lcdMem.display(memPercent)
        #print(memPercent)

        diskPercent = int(payload["disk_usage"].percent)
        if diskPercent>=100:
            diskPercent=99
        self.lcdDisk.display(diskPercent)

        cpuFreq = int(payload["cpu_freq"].current)
        cpuFreq = round(cpuFreq/1000,2)
        self.labelCpuInfo.setText("CPU Freq: <strong>"+str(cpuFreq)+"</strong> GHZ")

        memTotal = round(payload['mem'].total/1024/1024/1024,2)
        memUsed = round((payload['mem'].total-payload['mem'].available)/1024/1024/1024,2)

        self.labelMemInfo.setText("Memory: "+str(memUsed)+"/"+str(memTotal)+" GB")

        diskTotal = round(payload['disk_usage'].total/1024/1024/1024,2)
        diskUsed = round(payload['disk_usage'].used/1024/1024/1024,2)
        self.labelDiskInfo.setText("Disk usage: " + str(diskUsed) + "/" + str(diskTotal) + " GB")

        self.lcdNetIn.display(payload['net_speed_in'])
        self.lcdNetOut.display(payload['net_speed_out'])


class DashThread(GeneralDaemonThread):
    def getInfo(self):
        return DashInfo.getDashInfo()

class SystemInfo:
    ''' 获取Linux系统主机名称 '''
    def getHostname(self):
        with open('/proc/version') as fd:
            hostname = "unkown"
            for line in fd:
                hostname = line.split("(")[0]
        return {'hostname':hostname}
    def getGccVersion(self):
        gccVersion = "unkown"
        with open('/proc/version') as fd:
            for line in fd:
                gccVersion = line.split("(gcc")[1]
                gccVersion = gccVersion.split("#")[0]
        return {'gccVersion':gccVersion}

    ''' 获取Linux系统的版本信息 '''
    def getOsVersion(self):
        osver = "unkown"
        with open('/etc/issue') as fd:
            for line in fd:
                osver = line.split('\\n')[0]
                break
        return {'osver':osver}

    ''' 获取CPU的型号和CPU的核心数 '''
    def getCpu(self):
        num = 0
        with open('/proc/cpuinfo') as fd:
            for line in fd:
                if line.startswith('processor'):
                    num += 1
                if line.startswith('model name'):
                    cpu_model = line.split(':')[1].strip().split()
                    cpu_model = cpu_model[0] + ' ' + cpu_model[2]  + ' ' + cpu_model[-1]
        return {'cpu_num':num, 'cpu_model':cpu_model}
