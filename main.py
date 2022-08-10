import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
import time
from adb import *
import asyncio

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

    async def Result_text(self):
        add_text = self.result_text.append
        add_text(tool.t_netstat())
        await asyncio.sleep(1.0)
        add_text("sleep 1")

    def Result(self):
        asyncio.run(Window_2.Result_text()) # 야 비동기; 빨리 돌으라고;

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window_1 = Window_1()
    Window_1.show()
    app.exec_()