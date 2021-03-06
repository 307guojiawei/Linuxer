
from PyQt5 import QtWidgets
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt, QModelIndex, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView

from core.Proccess import ProcessTool
from modules.GeneralDaemonThread import GeneralDaemonThread
from modules.Processes.design import Ui_processForm


class ProcessesWidget(QtWidgets.QWidget, Ui_processForm):
    def __init__(self,parent = None):
        super(ProcessesWidget,self).__init__(parent)
        self.setupUi(self)
        self.myThread = ProcessThread(self)
        self.processModel = ProcessTableModel()
        self.processTable.setModel(self.processModel)
        self.myThread.sinOut.connect(self.updateProcessData)
        self.processModel.selectPidPosition.connect(self.processTable.selectRow)
        self.processTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.processTable.show()
        self.selectedPID = None

    def show(self):
        super(ProcessesWidget)
        self.myThread.start()

    def hide(self):
        super(ProcessesWidget, self).hide()
        self.myThread.setActive(False)

    def updateProcessData(self,payload):
        self.setUpdatesEnabled(False)
        payload["selectPID"]=self.selectedPID
        self.processModel.loadData(payload)
        self.lcdProcess.display(payload['count'])
        self.setUpdatesEnabled(True)

    def selectProcess(self,index):
        process = self.processModel.item(index.row(),0)
        self.selectedPID = int(process.text())
        self.labelPID.setText("Selected PID: "+str(self.selectedPID))

    def killProcess(self):
        if self.selectedPID is not None:
            tool = ProcessTool()
            tool.killProcess(self.selectedPID)


class ProcessTableModel(QStandardItemModel):
    selectPidPosition = pyqtSignal(int)


    def __init__(self):
        super(ProcessTableModel, self).__init__()
        self.setHeaders()

    def setHeaders(self):
        self.setHorizontalHeaderLabels(["PID","Memory %","CPU %","User","Process"])


    def loadData(self,payload): #payload是一个list,其中item是dict类型
        selectPid = payload["selectPID"]
        pidPos=-1
        payload = payload["res"]
        self.removeRows(0,self.rowCount())
        for index,item in enumerate(payload):
            process = list()
            if (selectPid):
                if selectPid==int(item['pid']):
                    pidPos=index
            items=QStandardItem()
            items.setData(int(item['pid']),Qt.DisplayRole)
            process.append(items)
            items = QStandardItem()
            items.setData(float(item['mem']), Qt.DisplayRole)
            process.append(items)
            items = QStandardItem()
            items.setData(float(item['cpu']), Qt.DisplayRole)
            process.append(items)
            process.append(QStandardItem(item['user']))
            process.append(QStandardItem(item['name']))
            self.appendRow(process)
        #self.resetInternalData()
        if pidPos!=-1:
            self.selectPidPosition.emit(pidPos)



        #self.dataChanged.emit()


#
# class ProcessTableModel(QAbstractTableModel):
#     dataChanged = pyqtSignal()
#
#
#     def __init__(self):
#         super(ProcessTableModel, self).__init__()
#         self.data = list()
#         self.dirty = False
#
#     def getRow(self,index):
#         if (not index.isValid() or
#                 not (0 <= index.row() < len(self.data))):
#             return QVariant()
#         process = self.data[index.row()]
#         return process
#
#     def data(self, index, role=Qt.DisplayRole):
#         if (not index.isValid() or
#                 not (0 <= index.row() < len(self.data))):
#             return QVariant()
#         process = self.data[index.row()]
#         column = index.column()
#         if role == Qt.DisplayRole:
#             return process[column]
#
#     def headerData(self, section, orientation, role=Qt.DisplayRole):
#         if role == Qt.TextAlignmentRole:
#             if orientation == Qt.Horizontal:
#                 return QVariant(int(Qt.AlignLeft | Qt.AlignVCenter))
#             return QVariant(int(Qt.AlignRight | Qt.AlignVCenter))
#         if role != Qt.DisplayRole:
#             return QVariant()
#         if orientation == Qt.Horizontal:
#             if section == 0:
#                 return QVariant("PID")
#             elif section == 1:
#                 return QVariant("Memory %")
#             elif section == 2:
#                 return QVariant("CPU %")
#             elif section == 3:
#                 return QVariant("User")
#             elif section == 4:
#                 return QVariant("Process")
#         return QVariant(int(section + 1))
#
#     def rowCount(self, index=QModelIndex()):
#         return 100
#
#     def columnCount(self, index=QModelIndex()):
#         return 5
#
#     def loadData(self,payload): #payload是一个list,其中item是dict类型
#         payload = payload["res"]
#         res = list()
#         for item in payload:
#             process = list()
#             process.append(item['pid'])
#             process.append(item['mem'])
#             process.append(item['cpu'])
#             process.append(item['user'])
#             process.append(item['name'])
#             res.append(process)
#         self.resetInternalData()
#         self.data = res
#         self.dirty = True
#
#
#
#         self.dataChanged.emit()




class ProcessThread(GeneralDaemonThread):
    def setParams(self):
        self.freshInterval = 3

    def getInfo(self):
        tool = ProcessTool()
        res = tool.getProcessInfo()
        return {"res": res, "count": len(res)}







