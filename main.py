import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
import time
from adb import *

form_class = uic.loadUiType("start.ui")[0]
form_class2 = uic.loadUiType("tool.ui")[0]

class Window_1(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Asseertive Wallpad Tool")
        self.pushButton.clicked.connect(self.showwindow_main)

    def showwindow_main(self):
        self.hide()
        self.w = Window_2()
        self.w.show()

class Window_2(QMainWindow, form_class2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Asseertive Wallpad Tool")
        self.close_btn.clicked.connect(QCoreApplication.instance().quit)
        self.start_btn.clicked.connect(self.Result)
        self.clear_btn.clicked.connect(self.result_text.clear)

    def Result(self):
        add_text = self.result_text.append
        add_text("비정상 포트를 점검합니다.\n")
        add_text(tool.t_netstat()+"\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window_1 = Window_1()
    Window_1.show()
    app.exec_()