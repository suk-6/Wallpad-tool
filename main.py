import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tool import Window_2

form_class = uic.loadUiType("start.ui")[0]

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window_1 = Window_1()
    Window_1.show()
    app.exec_()