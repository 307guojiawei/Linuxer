# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 613)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/img/Linuxer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.sidebar = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QtCore.QSize(60, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sidebar.setStyleSheet("")
        self.sidebar.setObjectName("sidebar")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebarLayout.setContentsMargins(0, 5, 0, 5)
        self.sidebarLayout.setSpacing(0)
        self.sidebarLayout.setObjectName("sidebarLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem)
        self.btnDash = QtWidgets.QPushButton(self.sidebar)
        self.btnDash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDash.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnDash.setStyleSheet("")
        self.btnDash.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/img/sidebar-icons/dash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDash.setIcon(icon1)
        self.btnDash.setIconSize(QtCore.QSize(35, 35))
        self.btnDash.setCheckable(True)
        self.btnDash.setChecked(True)
        self.btnDash.setObjectName("btnDash")
        self.sidebarLayout.addWidget(self.btnDash)
        self.btnStartups = QtWidgets.QPushButton(self.sidebar)
        self.btnStartups.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStartups.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnStartups.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/img/sidebar-icons/startup-apps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStartups.setIcon(icon2)
        self.btnStartups.setIconSize(QtCore.QSize(35, 35))
        self.btnStartups.setCheckable(True)
        self.btnStartups.setObjectName("btnStartups")
        self.sidebarLayout.addWidget(self.btnStartups)
        self.btnProcesses = QtWidgets.QPushButton(self.sidebar)
        self.btnProcesses.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProcesses.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnProcesses.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/img/sidebar-icons/process.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProcesses.setIcon(icon3)
        self.btnProcesses.setIconSize(QtCore.QSize(35, 35))
        self.btnProcesses.setCheckable(True)
        self.btnProcesses.setObjectName("btnProcesses")
        self.sidebarLayout.addWidget(self.btnProcesses)
        self.btnResource = QtWidgets.QPushButton(self.sidebar)
        self.btnResource.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnResource.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnResource.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/img/sidebar-icons/resources.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnResource.setIcon(icon4)
        self.btnResource.setIconSize(QtCore.QSize(35, 35))
        self.btnResource.setCheckable(True)
        self.btnResource.setObjectName("btnResource")
        self.sidebarLayout.addWidget(self.btnResource)
        self.btnSetup = QtWidgets.QPushButton(self.sidebar)
        self.btnSetup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetup.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSetup.setStyleSheet("")
        self.btnSetup.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/img/sidebar-icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetup.setIcon(icon5)
        self.btnSetup.setIconSize(QtCore.QSize(35, 35))
        self.btnSetup.setCheckable(True)
        self.btnSetup.setObjectName("btnSetup")
        self.sidebarLayout.addWidget(self.btnSetup)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem1)
        self.btnDash.raise_()
        self.btnSetup.raise_()
        self.btnResource.raise_()
        self.btnStartups.raise_()
        self.btnProcesses.raise_()
        self.rightWidget = QtWidgets.QWidget(self.splitter)
        self.rightWidget.setObjectName("rightWidget")
        self.mainLayout = QtWidgets.QGridLayout(self.rightWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName("mainLayout")
        self.mainWidgetBox = QtWidgets.QWidget(self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidgetBox.sizePolicy().hasHeightForWidth())
        self.mainWidgetBox.setSizePolicy(sizePolicy)
        self.mainWidgetBox.setMinimumSize(QtCore.QSize(0, 0))
        self.mainWidgetBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.mainWidgetBox.setBaseSize(QtCore.QSize(0, 0))
        self.mainWidgetBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mainWidgetBox.setObjectName("mainWidgetBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidgetBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainWidget = QtWidgets.QWidget(self.mainWidgetBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout.addWidget(self.mainWidget)
        self.mainLayout.addWidget(self.mainWidgetBox, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.rightWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainWidgetLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidgetLabel.sizePolicy().hasHeightForWidth())
        self.mainWidgetLabel.setSizePolicy(sizePolicy)
        self.mainWidgetLabel.setMinimumSize(QtCore.QSize(0, 29))
        self.mainWidgetLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mainWidgetLabel.setScaledContents(False)
        self.mainWidgetLabel.setObjectName("mainWidgetLabel")
        self.verticalLayout_2.addWidget(self.mainWidgetLabel, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("color: rgb(0, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.mainLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.mainLayout.setRowStretch(0, 1)
        self.mainLayout.setRowStretch(2, 6)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnDash.clicked.connect(MainWindow.selectPage)
        self.btnStartups.clicked.connect(MainWindow.selectPage)
        self.btnProcesses.clicked.connect(MainWindow.selectPage)
        self.btnResource.clicked.connect(MainWindow.selectPage)
        self.btnSetup.clicked.connect(MainWindow.selectPage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linuxer"))
        self.btnDash.setToolTip(_translate("MainWindow", "Dashboard"))
        self.btnStartups.setToolTip(_translate("MainWindow", "Starup Services"))
        self.btnProcesses.setToolTip(_translate("MainWindow", "Processes"))
        self.btnResource.setToolTip(_translate("MainWindow", "Resouce Chart"))
        self.btnSetup.setToolTip(_translate("MainWindow", "Application Setups"))
        self.mainWidgetLabel.setText(_translate("MainWindow", "System Dash Board"))

