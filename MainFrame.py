import os
import sys

from PyQt5.QtWidgets import QApplication

import App
styleDir = "./assets/style.qss" #全局style文件路径


def main():
    # # 提升到root权限
    # if os.geteuid():
    #     args = [sys.executable] + sys.argv
    #     # 下面两种写法，一种使用su，一种使用sudo，都可以
    #     #os.execlp('su', 'su', '-c', ' '.join(args))
    #     os.execlp('sudo', 'sudo', *args)

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
