# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './modules/Startups/design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartupForm(object):
    def setupUi(self, StartupForm):
        StartupForm.setObjectName("StartupForm")
        StartupForm.resize(804, 521)
        self.verticalLayout = QtWidgets.QVBoxLayout(StartupForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(StartupForm)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_seq = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_seq.sizePolicy().hasHeightForWidth())
        self.widget_seq.setSizePolicy(sizePolicy)
        self.widget_seq.setObjectName("widget_seq")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_seq)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_seq)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textStartupSeq = QtWidgets.QTextBrowser(self.widget_seq)
        self.textStartupSeq.setObjectName("textStartupSeq")
        self.gridLayout.addWidget(self.textStartupSeq, 1, 0, 1, 2)
        self.btnSVG = QtWidgets.QPushButton(self.widget_seq)
        self.btnSVG.setCheckable(False)
        self.btnSVG.setFlat(False)
        self.btnSVG.setObjectName("btnSVG")
        self.gridLayout.addWidget(self.btnSVG, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout.addWidget(self.widget_seq)
        self.widget_bootTime = QtWidgets.QWidget(self.widget)
        self.widget_bootTime.setObjectName("widget_bootTime")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_bootTime)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdBootTime = QtWidgets.QLCDNumber(self.widget_bootTime)
        self.lcdBootTime.setSmallDecimalPoint(True)
        self.lcdBootTime.setDigitCount(3)
        self.lcdBootTime.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdBootTime.setObjectName("lcdBootTime")
        self.verticalLayout_2.addWidget(self.lcdBootTime)
        self.label_2 = QtWidgets.QLabel(self.widget_bootTime)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.widget_bootTime)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.serviceTable = QtWidgets.QTextBrowser(StartupForm)
        self.serviceTable.setOpenExternalLinks(False)
        self.serviceTable.setOpenLinks(False)
        self.serviceTable.setObjectName("serviceTable")
        self.verticalLayout.addWidget(self.serviceTable)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(StartupForm)
        self.btnSVG.clicked.connect(StartupForm.generateSVG)
        self.serviceTable.anchorClicked['QUrl'].connect(StartupForm.handleOperation)
        QtCore.QMetaObject.connectSlotsByName(StartupForm)

    def retranslateUi(self, StartupForm):
        _translate = QtCore.QCoreApplication.translate
        StartupForm.setWindowTitle(_translate("StartupForm", "Form"))
        self.label.setText(_translate("StartupForm", "System start up sequence"))
        self.textStartupSeq.setHtml(_translate("StartupForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'WenQuanYi Micro Hei\'; font-size:9.7002pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9.7002pt;\">Analysing.....</span></p></body></html>"))
        self.btnSVG.setText(_translate("StartupForm", "View More"))
        self.label_2.setText(_translate("StartupForm", "Boot Time(s)"))
        self.serviceTable.setHtml(_translate("StartupForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'WenQuanYi Micro Hei\'; font-size:9.7002pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Analysing,please wait.....</span></p></body></html>"))

