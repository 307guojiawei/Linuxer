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
        self.mainWidget = DashWidget(self.mainWidgetBox)   #初始页面
        self.verticalLayout.addWidget(self.mainWidget)
        self.mainWidget.show()
        self.dash=None
        self.proc=None
        self.res=None
        self.setup=None
        self.start=None

    def selectPage(self):   #响应左边slidebar切换页面操作
        sender = self.sender()
        if sender.isChecked() == False: #本来就处于该页面下，无需切换
            sender.setChecked(True)
            return
        #清除所有按钮状态
        self.btnDash.setChecked(False)
        self.btnProcesses.setChecked(False)
        self.btnResource.setChecked(False)
        self.btnSetup.setChecked(False)
        self.btnStartups.setChecked(False)


        sender.setChecked(True)

        #print(sender.objectName()+"click")
        name = sender.objectName()
        self.mainWidget.hide()
        title = ""
        if name == "btnDash":
            if self.dash is None:
                self.dash=DashWidget(self.mainWidgetBox)
            self.mainWidget = self.dash
            title = "System Dash Board"
        elif name == "btnProcesses":
            self.proc=ProcessesWidget(self.mainWidgetBox)
            self.mainWidget = self.proc
            title = "Current Processes"
        elif name == "btnResource":
            if self.res is None:
                self.res=ResourceWidget(self.mainWidgetBox)
            self.mainWidget = self.res
            title = "System Resource Chart"
        elif name == "btnSetup":
            if self.setup is None:
                self.setup=SetupWidget(self.mainWidgetBox)
            self.mainWidget = self.setup
            title = "Setup & Info"
        elif name == "btnStartups":
            if self.start is None:
                self.start=StartupsWidget(self.mainWidgetBox)
            self.mainWidget = self.start
            title = "Start up Analyse"
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidgetLabel.setText(title)
        self.verticalLayout.addWidget(self.mainWidget)
        self.mainWidget.show()

