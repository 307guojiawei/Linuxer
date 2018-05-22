import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from modules.GeneralDaemonThread import GeneralDaemonThread
from modules.Resource.Chart import QtChartCanvas
from modules.Resource.design import Ui_resourceForm

import core.DashInfo as DashInfo

class ResourceWidget(QtWidgets.QWidget, Ui_resourceForm):
    def __init__(self,parent = None):
        super(ResourceWidget,self).__init__(parent)
        self.setupUi(self)
        self.cpu_canvas = QtChartCanvas(self)
        self.cpu_canvas.changeTop(True)
        self.mem_canvas = QtChartCanvas(self)
        self.net_canvas = QtChartCanvas(self)
        self.net_canvas.setYLimit(lockY=False)
        self.cpu_layout.addWidget(self.cpu_canvas)
        self.mem_layout.addWidget(self.mem_canvas)
        self.network_layout.addWidget(self.net_canvas)
        self.cpuThread = CPUThread(self)
        self.memThread = MemThread(self)
        self.netThread = NetThread(self)
        self.messageParser = MessageParser()

        self.cpuThread.sinOut.connect(self.messageParser.onMessageRecv)
        self.memThread.sinOut.connect(self.messageParser.onMessageRecv)
        self.netThread.sinOut.connect(self.messageParser.onMessageRecv)
        self.messageParser.sinCPUOut.connect(self.cpu_canvas.update_figure)
        self.messageParser.sinMemOut.connect(self.mem_canvas.update_figure)
        self.messageParser.sinNetOut.connect(self.net_canvas.update_figure)

        self.cpuThread.start()
        self.memThread.start()
        self.netThread.start()

    def show(self):
        super(ResourceWidget, self).show()
        self.cpuThread.setActive(True)
        self.memThread.setActive(True)
        self.netThread.setActive(True)

    def hide(self):
        super(ResourceWidget, self).hide()
        self.cpuThread.setActive(False)
        self.memThread.setActive(False)
        self.netThread.setActive(False)

    def topBarChanged(self,value):
        if value == 0:
            self.cpu_canvas.changeTop(True)
            self.mem_canvas.changeTop(False)
            self.net_canvas.changeTop(False)
        if value == 1:
            self.cpu_canvas.changeTop(False)
            self.mem_canvas.changeTop(True)
            self.net_canvas.changeTop(False)
        if value == 2:
            self.cpu_canvas.changeTop(False)
            self.mem_canvas.changeTop(False)
            self.net_canvas.changeTop(True)

class CPUThread(GeneralDaemonThread):
    def setParams(self):
        self.freshInterval = 0.15
        self.type = 0

    def getInfo(self):
        return DashInfo.getCPUInfo()

class MemThread(GeneralDaemonThread):
    def setParams(self):
        self.freshInterval = 0.5
        self.type = 1

    def getInfo(self):
        return DashInfo.getMemInfo()

class NetThread(GeneralDaemonThread):
    def setParams(self):
        self.freshInterval = 0.4
        self.type = 2

    def getInfo(self):
        return DashInfo.getNetSpeed()

class MessageParser(QObject):
    sinCPUOut = pyqtSignal(dict)
    sinMemOut = pyqtSignal(dict)
    sinNetOut = pyqtSignal(dict)
    def onMessageRecv(self,payload):
        sender = self.sender()
        res = dict()
        res['time'] = round(time.time() * 1000)
        if sender.type == 0:
            data = payload['cpu_percent']
            data=1 if data<1 else data
            data=99 if data>99 else data
            res["data"] =data
            self.sinCPUOut.emit(res)
        elif sender.type == 1:
            res['data'] = payload['mem'].percent
            self.sinMemOut.emit(res)
        elif sender.type == 2:
            res['data'] = payload['net_speed_in']
            self.sinNetOut.emit(res)




