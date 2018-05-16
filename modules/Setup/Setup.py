
from PyQt5 import QtWidgets

from modules.Processes.design import Ui_Form


class SetupWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self,parent = None):
        super(SetupWidget,self).__init__(parent)
        self.setupUi(self)
        print("SetupWidget init")

    def show(self):
        super(SetupWidget)
        print("show SetupWidget")



