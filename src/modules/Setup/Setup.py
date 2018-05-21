
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl

from modules.Setup.design import Ui_SetupForm
import webbrowser

class SetupWidget(QtWidgets.QWidget, Ui_SetupForm):
    def __init__(self,parent = None):
        super(SetupWidget,self).__init__(parent)
        self.setupUi(self)


    def show(self):
        super(SetupWidget)

    def openUrl(self,qurl):
        print(qurl.path())
        url = "https://github.com"+qurl.path()
        webbrowser.open(url)



