
from PyQt5 import QtWidgets

from modules.Processes.design import Ui_Form


class StartupsWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self,parent = None):
        super(StartupsWidget,self).__init__(parent)
        self.setupUi(self)
        print("StartupsWidget init")

    def show(self):
        super(StartupsWidget)
        print("show StartupsWidget")



