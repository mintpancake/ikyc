# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accounts.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("background: #f7f6fb")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(-60, -190, 391, 391))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("resources/small_logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(400, 80, 400, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setStyleSheet("color: #003780; background:None; text-align: center;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(930, 650, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BackButton.setStyleSheet("QPushButton{\n"
"    background: #004094;\n"
"    background-image : url(resources/back.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 100px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(0, 71, 163);\n"
"    background-image : url(resources/back.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 100px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: #004094;\n"
"    background-image : url(resources/back.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 100px;\n"
"}")
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")
        self.HKDButton = QtWidgets.QPushButton(self.centralwidget)
        self.HKDButton.setGeometry(QtCore.QRect(100, 300, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.HKDButton.setFont(font)
        self.HKDButton.setStyleSheet("QPushButton{\n"
"    border: 3px solid; \n"
"    border-color: #003780;\n"
"    border-radius:100px;\n"
"    background: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.HKDButton.setObjectName("HKDButton")
        self.HKDLabel = QtWidgets.QLabel(self.centralwidget)
        self.HKDLabel.setGeometry(QtCore.QRect(100, 330, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.HKDLabel.setFont(font)
        self.HKDLabel.setStyleSheet("border: None; color: #003780; text-align: center; background:None")
        self.HKDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HKDLabel.setObjectName("HKDLabel")
        self.depositButton = QtWidgets.QPushButton(self.centralwidget)
        self.depositButton.setGeometry(QtCore.QRect(367, 300, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.depositButton.setFont(font)
        self.depositButton.setStyleSheet("QPushButton{\n"
"    border: 3px solid; \n"
"    border-color: #003780;\n"
"    border-radius:100px;\n"
"    background: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.depositButton.setObjectName("depositButton")
        self.depositLabel = QtWidgets.QLabel(self.centralwidget)
        self.depositLabel.setGeometry(QtCore.QRect(367, 330, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.depositLabel.setFont(font)
        self.depositLabel.setStyleSheet("border: None; color: #003780; text-align: center; background:None")
        self.depositLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.depositLabel.setObjectName("depositLabel")
        self.USDButton = QtWidgets.QPushButton(self.centralwidget)
        self.USDButton.setGeometry(QtCore.QRect(633, 300, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.USDButton.setFont(font)
        self.USDButton.setStyleSheet("QPushButton{\n"
"    border: 3px solid; \n"
"    border-color: #003780;\n"
"    border-radius:100px;\n"
"    background: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.USDButton.setObjectName("USDButton")
        self.USDLabel = QtWidgets.QLabel(self.centralwidget)
        self.USDLabel.setGeometry(QtCore.QRect(633, 330, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.USDLabel.setFont(font)
        self.USDLabel.setStyleSheet("border: None; color: #003780; text-align: center; background:None")
        self.USDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.USDLabel.setObjectName("USDLabel")
        self.CNYLabel = QtWidgets.QLabel(self.centralwidget)
        self.CNYLabel.setGeometry(QtCore.QRect(900, 330, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CNYLabel.setFont(font)
        self.CNYLabel.setStyleSheet("border: None; color: #003780; text-align: center; background:None")
        self.CNYLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CNYLabel.setObjectName("CNYLabel")
        self.CNYButton = QtWidgets.QPushButton(self.centralwidget)
        self.CNYButton.setGeometry(QtCore.QRect(900, 300, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.CNYButton.setFont(font)
        self.CNYButton.setStyleSheet("QPushButton{\n"
"    border: 3px solid; \n"
"    border-color: #003780;\n"
"    border-radius:100px;\n"
"    background: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.CNYButton.setObjectName("CNYButton")
        self.CNYButton.raise_()
        self.logoLabel.raise_()
        self.titleLabel.raise_()
        self.BackButton.raise_()
        self.HKDButton.raise_()
        self.HKDLabel.raise_()
        self.depositButton.raise_()
        self.depositLabel.raise_()
        self.USDButton.raise_()
        self.USDLabel.raise_()
        self.CNYLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iKYC"))
        self.titleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">My Accounts</span></p></body></html>"))
        self.HKDButton.setText(_translate("MainWindow", "$10,000"))
        self.HKDLabel.setText(_translate("MainWindow", "HKD"))
        self.depositButton.setText(_translate("MainWindow", "$10,000"))
        self.depositLabel.setText(_translate("MainWindow", "Deposit"))
        self.USDButton.setText(_translate("MainWindow", "$10,000"))
        self.USDLabel.setText(_translate("MainWindow", "USD"))
        self.CNYLabel.setText(_translate("MainWindow", "CNY"))
        self.CNYButton.setText(_translate("MainWindow", "￥10,000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

