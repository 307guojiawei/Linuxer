import random
from queue import Queue

from PyQt5 import QtCore, QtWidgets

# import matplotlib
from PyQt5.QtChart import QChart, QChartView, QSplineSeries
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QSizePolicy, QWidget


class QtChartCanvas(QWidget):
    def __init__(self,parent=None):
        super(QtChartCanvas, self).__init__(parent)
        self.plotChart = QChart()
        self.plotChart.legend().hide()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        self.plotView = QChartView(self.plotChart)
        self.verticalLayout.addWidget(self.plotView)

        self.plotCurve = QSplineSeries()
        self.plotCurve.setUseOpenGL(True)
        self.plotCurve.pen().setColor(Qt.red)
        self.plotChart.addSeries(self.plotCurve)

        self.plotChart.createDefaultAxes()
        self.plotChart.axisX().hide()

        self.RecvData = []  # 存储接收到的传感器数据
        self.RecvIndx = 0

        self.setLockY=True

        self.isTop=False
        self.minY=0
        self.maxY=100


    def update_figure(self,payload):
        self.RecvData.append(payload["data"])
        self.RecvData=self.RecvData[-20:]
        plotData = []
        if self.isTop:
            for i, val in enumerate(self.RecvData):
                plotData.append(QPoint(i, val))

            self.plotCurve.replace(plotData)
            self.plotChart.axisX().setMax(len(plotData))
            if not self.setLockY:
                self.plotChart.axisY().setRange(0, max(self.RecvData)+10)
            else:
                self.plotChart.axisY().setRange(self.minY, self.maxY)

    def setYLimit(self,miny=0,maxy=100,lockY = True):
        self.setLockY=lockY
        if self.setLockY:
            self.maxY=maxy
            self.minY=miny

    def changeTop(self,isTop):
        self.isTop=isTop


#
#
# class MyMplCanvas(FigureCanvas):
#     """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi,facecolor='#263848',edgecolor='#263848')
#         self.axes = fig.add_subplot(111)
#
#         # 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
#         self.axes.hold(False)
#         self.axes.get_xaxis().set_visible(False)
#         self.axes.spines['top'].set_visible(False)
#         self.axes.spines['right'].set_visible(False)
#         self.axes.spines['left'].set_color("#9D9CA2")
#         self.axes.spines['bottom'].set_color("#9D9CA2")
#         self.axes.tick_params(which='major',width=2,colors='#F8F6F6')
#         self.compute_initial_figure()
#
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#
#         FigureCanvas.setSizePolicy(self,
#                                    QSizePolicy.Expanding,
#                                    QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)
#
#     def compute_initial_figure(self):
#         pass

#
# class MyDynamicMplCanvas(MyMplCanvas):
#
#     """动态画布：每秒自动更新，更换一条折线。"""
#     def __init__(self, *args, **kwargs):
#         MyMplCanvas.__init__(self, *args, **kwargs)
#         self.queue_y = list()
#         self.min_y = 0
#         self.max_y = 100
#         self.lockY = True
#         self.isTop = False
#
#     def setYLimit(self,miny=0,maxy=100,lockY = True):
#         self.min_y = miny
#         self.max_y = maxy
#         self.lockY = lockY
#
#     def compute_initial_figure(self):
#         self.axes.set_xlabel('x')
#         self.axes.set_ylabel('y')
#
#
#
#     def changeTop(self,isTop):
#         self.isTop = isTop
#
#     def update_figure(self,payload):
#         if len(self.queue_y) > 10:
#             self.queue_y = self.queue_y[1::]
#         self.queue_y.append(payload['data'])
#         if not self.isTop:
#             return
#
#         x = len(self.queue_y)
#         x = range(x)
#         y = self.queue_y
#         self.axes.plot(x, y, color="#0BCFF7")
#         if self.lockY:
#             self.axes.set_ylim(self.min_y, self.max_y)
#
#         self.axes.grid('on')
#         self.axes.patch.set_alpha(0.8)
#         self.axes.patch.set_facecolor("#263848")
#         self.draw()
