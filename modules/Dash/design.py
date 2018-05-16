# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './modules/Dash/design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DashForm(object):
    def setupUi(self, DashForm):
        DashForm.setObjectName("DashForm")
        DashForm.resize(807, 509)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DashForm)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdCpu = QtWidgets.QLCDNumber(DashForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdCpu.sizePolicy().hasHeightForWidth())
        self.lcdCpu.setSizePolicy(sizePolicy)
        self.lcdCpu.setMinimumSize(QtCore.QSize(0, 150))
        self.lcdCpu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdCpu.setSmallDecimalPoint(False)
        self.lcdCpu.setDigitCount(2)
        self.lcdCpu.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdCpu.setObjectName("lcdCpu")
        self.gridLayout.addWidget(self.lcdCpu, 0, 0, 1, 1)
        self.labelMemInfo = QtWidgets.QLabel(DashForm)
        self.labelMemInfo.setObjectName("labelMemInfo")
        self.gridLayout.addWidget(self.labelMemInfo, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lcdMem = QtWidgets.QLCDNumber(DashForm)
        self.lcdMem.setDigitCount(2)
        self.lcdMem.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdMem.setObjectName("lcdMem")
        self.gridLayout.addWidget(self.lcdMem, 0, 1, 1, 1)
        self.lcdDisk = QtWidgets.QLCDNumber(DashForm)
        self.lcdDisk.setDigitCount(2)
        self.lcdDisk.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdDisk.setObjectName("lcdDisk")
        self.gridLayout.addWidget(self.lcdDisk, 0, 2, 1, 1)
        self.labelCpuInfo = QtWidgets.QLabel(DashForm)
        self.labelCpuInfo.setObjectName("labelCpuInfo")
        self.gridLayout.addWidget(self.labelCpuInfo, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.labelDiskInfo = QtWidgets.QLabel(DashForm)
        self.labelDiskInfo.setObjectName("labelDiskInfo")
        self.gridLayout.addWidget(self.labelDiskInfo, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.widget = QtWidgets.QWidget(DashForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(DashForm)
        QtCore.QMetaObject.connectSlotsByName(DashForm)

    def retranslateUi(self, DashForm):
        _translate = QtCore.QCoreApplication.translate
        DashForm.setWindowTitle(_translate("DashForm", "Form"))
        self.lcdCpu.setToolTip(_translate("DashForm", "CPU"))
        self.labelMemInfo.setText(_translate("DashForm", "Loading..."))
        self.lcdMem.setToolTip(_translate("DashForm", "Memory"))
        self.lcdDisk.setToolTip(_translate("DashForm", "Disk"))
        self.labelCpuInfo.setText(_translate("DashForm", "Loading..."))
        self.labelDiskInfo.setText(_translate("DashForm", "Loading..."))

