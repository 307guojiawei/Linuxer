import random
import time
from PyQt5.QtCore import QThread, pyqtSignal

#通用的守护线程类，作为所有模块后台线程的父类使用
class GeneralDaemonThread(QThread):
    sinOut = pyqtSignal(dict)

    def __init__(self,parent=None):
        super(GeneralDaemonThread, self).__init__(parent)
        self.isActive = True
        self.freshInterval = 1
        self.setParams()

    def setActive(self,value=True):
        self.isActive = bool(value)
        if not value:
            self.exit()

    def run(self):
        last = 0
        now = time.time()
        interval = self.freshInterval
        while True:
            now = time.time()
            if now-last < interval or not self.isActive:
                time.sleep(random.random()/3.0)
                continue
            self.sinOut.emit(self.getInfo())
            last = now

    def exit(self, returnCode: int = ...):
        #print("exit")
        super(GeneralDaemonThread, self).exit()
        
    def getInfo(self):
        pass

    def setParams(self):
        pass