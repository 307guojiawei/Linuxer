# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './modules/Resource/design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_resourceForm(object):
    def setupUi(self, resourceForm):
        resourceForm.setObjectName("resourceForm")
        resourceForm.resize(770, 469)
        self.verticalLayout = QtWidgets.QVBoxLayout(resourceForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(resourceForm)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_cpu = QtWidgets.QWidget()
        self.tab_cpu.setObjectName("tab_cpu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_cpu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cpu_layout = QtWidgets.QVBoxLayout()
        self.cpu_layout.setObjectName("cpu_layout")
        self.verticalLayout_2.addLayout(self.cpu_layout)
        self.tabWidget.addTab(self.tab_cpu, "")
        self.tab_mem = QtWidgets.QWidget()
        self.tab_mem.setObjectName("tab_mem")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_mem)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mem_layout = QtWidgets.QVBoxLayout()
        self.mem_layout.setObjectName("mem_layout")
        self.verticalLayout_3.addLayout(self.mem_layout)
        self.tabWidget.addTab(self.tab_mem, "")
        self.tab_net = QtWidgets.QWidget()
        self.tab_net.setObjectName("tab_net")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_net)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.network_layout = QtWidgets.QVBoxLayout()
        self.network_layout.setObjectName("network_layout")
        self.verticalLayout_4.addLayout(self.network_layout)
        self.tabWidget.addTab(self.tab_net, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(resourceForm)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBarClicked['int'].connect(resourceForm.topBarChanged)
        QtCore.QMetaObject.connectSlotsByName(resourceForm)

    def retranslateUi(self, resourceForm):
        _translate = QtCore.QCoreApplication.translate
        resourceForm.setWindowTitle(_translate("resourceForm", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cpu), _translate("resourceForm", "CPU"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mem), _translate("resourceForm", "Memory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_net), _translate("resourceForm", "Network"))

