# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './modules/Processes/design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_processForm(object):
    def setupUi(self, processForm):
        processForm.setObjectName("processForm")
        processForm.resize(730, 436)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(processForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(processForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lcdProcess = QtWidgets.QLCDNumber(processForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdProcess.sizePolicy().hasHeightForWidth())
        self.lcdProcess.setSizePolicy(sizePolicy)
        self.lcdProcess.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdProcess.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdProcess.setDigitCount(3)
        self.lcdProcess.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdProcess.setObjectName("lcdProcess")
        self.horizontalLayout.addWidget(self.lcdProcess)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.processTable = QtWidgets.QTableView(processForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processTable.sizePolicy().hasHeightForWidth())
        self.processTable.setSizePolicy(sizePolicy)
        self.processTable.setFrameShape(QtWidgets.QFrame.HLine)
        self.processTable.setDragDropOverwriteMode(False)
        self.processTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.processTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.processTable.setGridStyle(QtCore.Qt.SolidLine)
        self.processTable.setSortingEnabled(True)
        self.processTable.setObjectName("processTable")
        self.verticalLayout.addWidget(self.processTable)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnKillProcess = QtWidgets.QPushButton(processForm)
        self.btnKillProcess.setObjectName("btnKillProcess")
        self.horizontalLayout_2.addWidget(self.btnKillProcess)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(processForm)
        QtCore.QMetaObject.connectSlotsByName(processForm)

    def retranslateUi(self, processForm):
        _translate = QtCore.QCoreApplication.translate
        processForm.setWindowTitle(_translate("processForm", "Form"))
        self.label.setText(_translate("processForm", "Process Static"))
        self.btnKillProcess.setText(_translate("processForm", "KILL Process"))

