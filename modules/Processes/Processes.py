
from PyQt5 import QtWidgets

from modules.Processes.design import Ui_Form


class ProcessesWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self,parent = None):
        super(ProcessesWidget,self).__init__(parent)
        self.setupUi(self)
        print("Processes init")

    def show(self):
        super(ProcessesWidget)
        print("show Processes")



