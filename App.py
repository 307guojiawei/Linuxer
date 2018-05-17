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

    def selectPage(self):   #响应左边slidebar切换页面操作
        #清除所有按钮状态
        self.btnDash.setChecked(False)
        self.btnProcesses.setChecked(False)
        self.btnResource.setChecked(False)
        self.btnSetup.setChecked(False)
        self.btnStartups.setChecked(False)

        sender = self.sender()
        sender.setChecked(True)

        #print(sender.objectName()+"click")
        name = sender.objectName()
        self.mainWidget.hide()
        title = ""
        if name == "btnDash":
            self.mainWidget = DashWidget(self.mainWidgetBox)
            title = "System Dash Board"
        elif name == "btnProcesses":
            self.mainWidget = ProcessesWidget(self.mainWidgetBox)
            title = "Current Processes"
        elif name == "btnResource":
            self.mainWidget = ResourceWidget(self.mainWidgetBox)
            title = "System Resource Chart"
        elif name == "btnSetup":
            self.mainWidget = SetupWidget(self.mainWidgetBox)
            title = "Setup & Info"
        elif name == "btnStartups":
            self.mainWidget = StartupsWidget(self.mainWidgetBox)
            title = "Start up Analyse"
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidgetLabel.setText(title)
        self.verticalLayout.addWidget(self.mainWidget)
        self.mainWidget.show()

