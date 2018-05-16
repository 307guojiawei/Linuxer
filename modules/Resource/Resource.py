
from PyQt5 import QtWidgets

from modules.Processes.design import Ui_Form


class ResourceWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self,parent = None):
        super(ResourceWidget,self).__init__(parent)
        self.setupUi(self)
        print("ResourceWidget init")

    def show(self):
        super(ResourceWidget)
        print("show ResourceWidget")



