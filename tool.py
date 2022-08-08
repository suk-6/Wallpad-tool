import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("tool.ui")[0]

class Window_2(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Asseertive Wallpad Tool")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window_2 = Window_2()
    Window_2.show()
    app.exec_()