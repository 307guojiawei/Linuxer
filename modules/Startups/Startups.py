
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from core.ServiceTool import ServiceTool
from modules.GeneralDaemonThread import GeneralDaemonThread
from modules.Startups.design import Ui_StartupForm
from core.StartupAnalyse import getStartupInfo
from core.StartupAnalyse import getStartupSVG
import webbrowser

class StartupsWidget(QtWidgets.QWidget, Ui_StartupForm):
    def __init__(self,parent = None):
        super(StartupsWidget, self).__init__(parent)
        self.setupUi(self)
        self.myThread = StartupThread(self)
        self.myThread.sinOut.connect(self.handleServiceTable)
        self.myThread.start()

        self.sysInfoThread = StartupThread_SysInfo(self)
        self.sysInfoThread.sinOut.connect(self.handleSystemInfo)
        self.sysInfoThread.start()

    def show(self):
        super(StartupsWidget, self).show()

    def hide(self):
        super(StartupsWidget, self).hide()
        self.myThread.setActive(False)

    def updateStartupInfo(self,info):
        self.lcdBootTime.display(info['boot_time'])
        self.textStartupSeq.setText(info['critical_chain'])

    def updateServiceTable(self,services):
        html = "<style>" \
                "a{	text-decoration: none;color:#0A50F0}"\
                "table{ table-layout:fixed; empty-cells:show; border-collapse: collapse; margin:0 auto; } td{ height:30px; } h1,h2,h3{ font-size:12px; margin:0; padding:0; } .table{ border:1px solid #cad9ea; color:#666; } .table th { background-repeat:repeat-x; height:30px; } .table td,.table th{ border:1px solid #cad9ea; padding:0 1em 0; } .table tr.alter{ background-color:#f5fafe; } "\
                "</style>"
        html += "<table>" \
               "<tr><td>No.</td><td>Service Name</td><td>Description</td><td>Enable</td><td>Active</td></tr>"
        num = 1
        for service in services:
            hrefEnable = ""
            hrefActive = ""
            if service['isEnabled'] == "enabled":
                hrefEnable = service['name']+"___"+"disable"
            else:
                hrefEnable = service['name'] + "___" + "enable"
            if service['isActive'] == "active":
                hrefActive = service['name']+"___"+"inactive"
            else:
                hrefActive = service['name'] + "___" + "active"
            html += "<tr>"
            html += "<td>"+str(num)+"</td>"
            num += 1
            html += "<td>" + str(service['name']) + "</td>"
            html += "<td>" + str(service['description']) + "</td>"
            html += "<td><a href=\""+hrefEnable+"\">" + str(service['isEnabled']) + "</a></td>"
            html += "<td><a href=\""+hrefActive+"\">" + str(service['isActive']) + "</a></td>"
            html += "</tr>"
        html += "</table>"
        self.serviceTable.setText(html)

    def generateSVG(self):
        res = getStartupSVG()
        fname = QFileDialog.getSaveFileName(self,"Save SVG graph",filter="svg")
        fname_str = fname[0]+"."+fname[1]
        try:
            fd = open(fname_str,"w")
            fd.write(res['svg'])
            fd.close()
        except:
            print("generateSVG err: writing file")
            return
        webbrowser.open(fname_str)

    def handleServiceTable(self,payload):
        #self.updateStartupInfo(payload['info'])
        self.updateServiceTable(payload['services'])

    def handleSystemInfo(self,payload):
        self.updateStartupInfo(payload['info'])
        #self.updateServiceTable(payload['services'])

    def handleOperation(self,url):
        print(url.fileName())
        request = url.fileName().split("___")
        serviceName = request[0]
        operationName = request[1]
        tool = ServiceTool()
        if operationName == "enable":
            tool.changeServiceStatus(serviceName,True)
        elif operationName == "disable":
            tool.changeServiceStatus(serviceName, False)
        elif operationName == "active":
            tool.changeServiceActive(serviceName, True)
        elif operationName == "inactive":
            tool.changeServiceActive(serviceName, False)
        self.myThread.isActive = True


class StartupThread(GeneralDaemonThread):
    def __init__(self,parent=None):
        super(StartupThread, self).__init__(parent)
        self.freshInterval = 1

    def getInfo(self):
        res = dict()
        #res['info'] = getStartupInfo()
        tool = ServiceTool()
        res['services'] = tool.getServices()
        self.isActive = False
        return res


class StartupThread_SysInfo(GeneralDaemonThread):
    def __init__(self,parent=None):
        super(StartupThread_SysInfo, self).__init__(parent)
        self.freshInterval = 1

    def getInfo(self):
        res = dict()
        res['info'] = getStartupInfo()
        self.setActive(False)
        return res






