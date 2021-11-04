# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 805)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 250, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 164, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 250, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 250, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 164, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 250, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 250, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 164, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 246, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(247, 246, 251);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.small_logo = QtWidgets.QLabel(self.centralwidget)
        self.small_logo.setGeometry(QtCore.QRect(-60, -190, 391, 391))
        self.small_logo.setText("")
        self.small_logo.setPixmap(QtGui.QPixmap("resources/small_logo.png"))
        self.small_logo.setScaledContents(True)
        self.small_logo.setObjectName("small_logo")
        self.homeTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.homeTitleLabel.setGeometry(QtCore.QRect(190, 50, 671, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.homeTitleLabel.setFont(font)
        self.homeTitleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.homeTitleLabel.setObjectName("homeTitleLabel")
        self.lastLoginTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastLoginTimeLabel.setGeometry(QtCore.QRect(870, 50, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lastLoginTimeLabel.setFont(font)
        self.lastLoginTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lastLoginTimeLabel.setObjectName("lastLoginTimeLabel")
        self.profileButton = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton.setGeometry(QtCore.QRect(80, 210, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.profileButton.setFont(font)
        self.profileButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.profileButton.setStyleSheet("QPushButton{\n"
"    background: rgb(51, 235, 215);\n"
"    background-image : url(resources/profile.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(49, 225, 204);\n"
"    background-image : url(resources/profile.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(46, 215, 195);\n"
"    background-image : url(resources/profile.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}")
        self.profileButton.setText("")
        self.profileButton.setObjectName("profileButton")
        self.transactionButton = QtWidgets.QPushButton(self.centralwidget)
        self.transactionButton.setGeometry(QtCore.QRect(310, 480, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.transactionButton.setFont(font)
        self.transactionButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.transactionButton.setStyleSheet("QPushButton{\n"
"    background: rgb(71, 96, 137);\n"
"    background-image : url(resources/history.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(66, 89, 127);\n"
"    background-image : url(resources/history.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(61, 82, 117);\n"
"    background-image : url(resources/history.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}")
        self.transactionButton.setText("")
        self.transactionButton.setObjectName("transactionButton")
        self.transferButton = QtWidgets.QPushButton(self.centralwidget)
        self.transferButton.setGeometry(QtCore.QRect(80, 480, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.transferButton.setFont(font)
        self.transferButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.transferButton.setStyleSheet("QPushButton{\n"
"    background: rgb(65, 124, 252);\n"
"    background-image : url(resources/transfer.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(63, 119, 242);\n"
"    background-image : url(resources/transfer.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(60, 114, 232);\n"
"    background-image : url(resources/transfer.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}")
        self.transferButton.setText("")
        self.transferButton.setObjectName("transferButton")
        self.accountButton = QtWidgets.QPushButton(self.centralwidget)
        self.accountButton.setGeometry(QtCore.QRect(310, 210, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountButton.setFont(font)
        self.accountButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.accountButton.setStyleSheet("QPushButton{\n"
"    background: rgb(139, 229, 253);\n"
"    background-image : url(resources/account.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(133, 221, 243);\n"
"    background-image : url(resources/account.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(128, 212, 233);\n"
"    background-image : url(resources/account.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 55px;\n"
"}")
        self.accountButton.setText("")
        self.accountButton.setObjectName("accountButton")
        self.profileLabel = QtWidgets.QLabel(self.centralwidget)
        self.profileLabel.setGeometry(QtCore.QRect(80, 370, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.profileLabel.setFont(font)
        self.profileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.profileLabel.setObjectName("profileLabel")
        self.accountLabel = QtWidgets.QLabel(self.centralwidget)
        self.accountLabel.setGeometry(QtCore.QRect(310, 370, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.accountLabel.setFont(font)
        self.accountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.accountLabel.setObjectName("accountLabel")
        self.transferLabel = QtWidgets.QLabel(self.centralwidget)
        self.transferLabel.setGeometry(QtCore.QRect(80, 640, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.transferLabel.setFont(font)
        self.transferLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.transferLabel.setObjectName("transferLabel")
        self.historyLabel = QtWidgets.QLabel(self.centralwidget)
        self.historyLabel.setGeometry(QtCore.QRect(310, 640, 150, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.historyLabel.setFont(font)
        self.historyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.historyLabel.setObjectName("historyLabel")
        self.loanScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.loanScrollArea.setGeometry(QtCore.QRect(540, 210, 281, 501))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.loanScrollArea.setFont(font)
        self.loanScrollArea.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"}\n"
"QScrollBar:vertical {       \n"
"    background:transparent;\n"
"    width:10px;\n"
"    margin:0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 rgb(139, 229, 253), stop: 0.5 rgb(139, 229, 253), stop:1 rgb(139, 229, 253));\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 rgb(139, 229, 253), stop: 0.5 rgb(139, 229, 253),  stop:1 rgb(139, 229, 253));\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(139, 229, 253), stop: 0.5 rgb(139, 229, 253),  stop:1 rgb(139, 229, 253));\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.loanScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.loanScrollArea.setWidgetResizable(True)
        self.loanScrollArea.setObjectName("loanScrollArea")
        self.loanScrollAreaWidget = QtWidgets.QWidget()
        self.loanScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 281, 501))
        self.loanScrollAreaWidget.setAutoFillBackground(False)
        self.loanScrollAreaWidget.setObjectName("loanScrollAreaWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.loanScrollAreaWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AAAAAAAAA = QtWidgets.QLabel(self.loanScrollAreaWidget)
        self.AAAAAAAAA.setObjectName("AAAAAAAAA")
        self.verticalLayout.addWidget(self.AAAAAAAAA)
        self.loanListWidget = QtWidgets.QListWidget(self.loanScrollAreaWidget)
        self.loanListWidget.setObjectName("loanListWidget")
        self.verticalLayout.addWidget(self.loanListWidget)
        self.loanScrollArea.setWidget(self.loanScrollAreaWidget)
        self.loanLabel = QtWidgets.QLabel(self.centralwidget)
        self.loanLabel.setGeometry(QtCore.QRect(550, 160, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.loanLabel.setFont(font)
        self.loanLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.loanLabel.setObjectName("loanLabel")
        self.loginHistoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginHistoryLabel.setGeometry(QtCore.QRect(880, 160, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.loginHistoryLabel.setFont(font)
        self.loginHistoryLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.loginHistoryLabel.setObjectName("loginHistoryLabel")
        self.historyScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.historyScrollArea.setGeometry(QtCore.QRect(870, 210, 281, 501))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.historyScrollArea.setFont(font)
        self.historyScrollArea.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"}\n"
"QScrollBar:vertical {       \n"
"    background:transparent;\n"
"    width:10px;\n"
"    margin:0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 rgb(139, 229, 253), stop: 0.5 rgb(139, 229, 253), stop:1 rgb(139, 229, 253));\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 rgb(139, 229, 253), stop: 0.5 rgb(139, 229, 253),  stop:1 rgb(139, 229, 253));\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(139, 229, 253), stop: 0.5 rgb(139, 229, 253),  stop:1 rgb(139, 229, 253));\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.historyScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.historyScrollArea.setWidgetResizable(True)
        self.historyScrollArea.setObjectName("historyScrollArea")
        self.historyScrollAreaWidget = QtWidgets.QWidget()
        self.historyScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 281, 501))
        self.historyScrollAreaWidget.setAutoFillBackground(False)
        self.historyScrollAreaWidget.setObjectName("historyScrollAreaWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.historyScrollAreaWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.historyListWidget = QtWidgets.QListWidget(self.historyScrollAreaWidget)
        self.historyListWidget.setObjectName("historyListWidget")
        self.verticalLayout_4.addWidget(self.historyListWidget)
        self.historyScrollArea.setWidget(self.historyScrollAreaWidget)
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(1090, 50, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logoutButton.setFont(font)
        self.logoutButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.logoutButton.setStyleSheet("QPushButton{\n"
"    background: #004094;\n"
"    background-image : url(resources/logout.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(0, 71, 163);\n"
"    background-image : url(resources/logout.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: #004094;\n"
"    background-image : url(resources/logout.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 30px;\n"
"}")
        self.logoutButton.setText("")
        self.logoutButton.setObjectName("logoutButton")
        self.loanButton = QtWidgets.QPushButton(self.centralwidget)
        self.loanButton.setGeometry(QtCore.QRect(615, 660, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loanButton.setFont(font)
        self.loanButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.loanButton.setStyleSheet("QPushButton{\n"
"    background: rgb(139, 229, 253);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 15px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(133, 221, 243);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 15px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(128, 212, 233);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 15px;\n"
"    color:rgb(0, 55, 128);\n"
"}")
        self.loanButton.setObjectName("loanButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iKYC"))
        self.homeTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">Welcome back, Luo Ping!</span></p></body></html>"))
        self.lastLoginTimeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#646464;\">Last login time:<br/>1970-01-01-00-00-00</span></p></body></html>"))
        self.profileLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">My Profile</span></p></body></html>"))
        self.accountLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">My Accounts</span></p></body></html>"))
        self.transferLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">Transfer</span></p></body></html>"))
        self.historyLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">Transaction<br/>History</span></p><p><span style=\" color:#003780;\"><br/></span></p></body></html>"))
        self.AAAAAAAAA.setText(_translate("MainWindow", "TextLabel"))
        self.loanLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">Loans</span></p></body></html>"))
        self.loginHistoryLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">Login History</span></p></body></html>"))
        self.loanButton.setText(_translate("MainWindow", "View Details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

