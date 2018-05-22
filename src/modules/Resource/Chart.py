import random
from queue import Queue

from PyQt5 import QtCore, QtWidgets

# import matplotlib
from PyQt5.QtChart import QChart, QChartView, QSplineSeries, QScatterSeries
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QSizePolicy, QWidget, QStyle


class QtChartCanvas(QWidget):
    def __init__(self,parent=None):
        super(QtChartCanvas, self).__init__(parent)
        self.setStyleSheet("border:0;background-color:#263848")
        self.plotChart = QChart()
        self.plotChart.legend().hide()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        self.plotView = QChartView(self.plotChart)
        self.plotView.setStyleSheet("border:0;background-color:#263848;")
        self.plotView.setBackgroundBrush(QBrush(QColor("#263848")))
        self.plotChart.setBackgroundBrush(QBrush(QColor("#263848")))

        #self.plotChart.setStyle()
        self.verticalLayout.addWidget(self.plotView)

        self.plotCurve = QSplineSeries()
        self.plotCurve.setColor(QColor("#AABFFF"))
        self.plotCurve.setUseOpenGL(True)
        self.plotCurve.pen().setColor(QColor("#FAF0FF"))
        self.plotChart.addSeries(self.plotCurve)

        # self.scatter=QScatterSeries()
        # self.scatter.setMarkerSize(8)
        # self.plotChart.addSeries(self.scatter)

        self.plotChart.createDefaultAxes()
        self.plotChart.axisY().setGridLineColor(QColor("#5D5C72"))
        self.plotChart.axisY().setLinePenColor(QColor("#9D9CA2"))
        self.plotChart.axisY().setLabelsColor(QColor("#F8F6F6"))
        self.plotChart.axisX().hide()

        self.RecvData = []  # 存储接收到的传感器数据
        self.RecvIndx = 0

        self.setLockY=True

        self.isTop=False
        self.minY=0
        self.maxY=100


    def update_figure(self,payload):
        data=payload["data"]
        data=1 if data<1 else data
        data=99 if data>99 else data
        self.RecvData.append(data)
        self.RecvData=self.RecvData[-20:]
        plotData = []
        if self.isTop:
            for i, val in enumerate(self.RecvData):
                plotData.append(QPoint(i, val))
            self.plotCurve.replace(plotData)
            #self.scatter.replace(plotData)
            self.plotChart.axisX().setMax(len(plotData))
            if not self.setLockY:
                self.plotChart.axisY().setRange(0, max(self.RecvData)*1.3)
            else:
                self.plotChart.axisY().setRange(self.minY, self.maxY)

    def setYLimit(self,miny=0,maxy=100,lockY = True):
        self.setLockY=lockY
        if self.setLockY:
            self.maxY=maxy
            self.minY=miny

    def changeTop(self,isTop):
        self.isTop=isTop



