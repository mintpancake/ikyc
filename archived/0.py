import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(360, 202, 1200, 800)
        self.setWindowTitle("Guo's Bank")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.move(500, 20)
        self.label.setText("Click \"Log in\" to start")
        self.label.adjustSize()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(550, 600)
        self.b1.setText("Log in")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.move(375, 20)
        self.label.setText("Sorry, we can't recognize you, please adjust you camera.")
        self.label.adjustSize()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
