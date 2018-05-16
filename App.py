from PyQt5.QtWidgets import QMainWindow, QApplication

from design import *
from modules.Dash.Dash import DashWidget
from modules.Processes.Processes import ProcessesWidget
from modules.Resource.Resource import ResourceWidget
from modules.Setup.Setup import SetupWidget
from modules.Startups.Startups import StartupsWidget

pages = [               #右侧页面选择
    'btnDash',
    'btnProcesses',
    'btnResource',
    'btnSetup',
    'btnStartups'
]


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.mainWidget = DashWidget(self.rightWidget)   #初始页面
        self.mainLayout.addWidget(self.mainWidget, 1, 0, 1, 1)
        self.mainWidget.show()

    def selectPage(self):   #响应左边slidebar切换页面操作
        sender = self.sender()
        #print(sender.objectName()+"click")
        name = sender.objectName()
        self.mainWidget.hide()
        title = ""
        if name == "btnDash":
            self.mainWidget = DashWidget(self.rightWidget)
            title = "System Dash Board"
        elif name == "btnProcesses":
            self.mainWidget = ProcessesWidget(self.rightWidget)
            title = "Current Processes"
        elif name == "btnResource":
            self.mainWidget = ResourceWidget(self.rightWidget)
            title = "System Resource Chart"
        elif name == "btnSetup":
            self.mainWidget = SetupWidget(self.rightWidget)
            title = "Setup & Info"
        elif name == "btnStartups":
            self.mainWidget = StartupsWidget(self.rightWidget)
            title = "Start up Analyse"
        self.mainWidgetLabel.setText(title)
        self.mainLayout.addWidget(self.mainWidget, 1, 0, 1, 1)
        self.mainWidget.show()

