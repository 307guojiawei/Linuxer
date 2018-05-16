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
        #print("show Dash")
        
    def hide(self):
        super(DashWidget, self).hide()
        self.myThread.setActive(False)

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


class DashThread(GeneralDaemonThread):
    def getInfo(self):
        return DashInfo.getDashInfo()
