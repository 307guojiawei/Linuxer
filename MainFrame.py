import sys

from PyQt5.QtWidgets import QApplication

import App
styleDir = "./assets/style.qss" #全局style文件路径


def main():
    app = QApplication(sys.argv)
    window = App.MyWindow()
    with open(styleDir) as file:
        buf = file.readlines()
        buf = ''.join(buf).strip('\n')
    app.setStyleSheet(buf)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
