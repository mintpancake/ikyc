# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transaction.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
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
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(247, 246, 251);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transferTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.transferTitleLabel.setGeometry(QtCore.QRect(190, 20, 601, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.transferTitleLabel.setFont(font)
        self.transferTitleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transferTitleLabel.setObjectName("transferTitleLabel")
        self.outScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.outScrollArea.setGeometry(QtCore.QRect(290, 230, 810, 160))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.outScrollArea.setFont(font)
        self.outScrollArea.setStyleSheet("QWidget{\n"
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
"    stop: 0 #004094, stop: 0.5 #004094, stop:1 #004094);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 #004094, stop: 0.5 #004094, stop:1 #004094);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 #004094, stop: 0.5 #004094, stop:1 #004094);\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.outScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.outScrollArea.setWidgetResizable(True)
        self.outScrollArea.setObjectName("outScrollArea")
        self.outScrollAreaWidget = QtWidgets.QWidget()
        self.outScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 810, 160))
        self.outScrollAreaWidget.setAutoFillBackground(False)
        self.outScrollAreaWidget.setObjectName("outScrollAreaWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.outScrollAreaWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.outScrollAreaWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.outScrollArea.setWidget(self.outScrollAreaWidget)
        self.inScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.inScrollArea.setGeometry(QtCore.QRect(290, 470, 810, 160))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.inScrollArea.setFont(font)
        self.inScrollArea.setStyleSheet("QWidget{\n"
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
"    stop: 0 #004094, stop: 0.5 #004094, stop:1 #004094);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 #004094, stop: 0.5 #004094, stop:1 #004094);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 #004094, stop: 0.5 #004094, stop:1 #004094);\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.inScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.inScrollArea.setWidgetResizable(True)
        self.inScrollArea.setObjectName("inScrollArea")
        self.inScrollAreaWidget = QtWidgets.QWidget()
        self.inScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 810, 160))
        self.inScrollAreaWidget.setAutoFillBackground(False)
        self.inScrollAreaWidget.setObjectName("inScrollAreaWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.inScrollAreaWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.listWidget_2 = QtWidgets.QListWidget(self.inScrollAreaWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_5.addWidget(self.listWidget_2)
        self.inScrollArea.setWidget(self.inScrollAreaWidget)
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(-60, -190, 391, 391))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("resources/small_logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(470, 90, 81, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel.setObjectName("TimeLabel")
        self.TimeLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_2.setGeometry(QtCore.QRect(290, 172, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_2.setFont(font)
        self.TimeLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_2.setObjectName("TimeLabel_2")
        self.TimeLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_3.setGeometry(QtCore.QRect(520, 170, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_3.setFont(font)
        self.TimeLabel_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_3.setObjectName("TimeLabel_3")
        self.Income = QtWidgets.QLabel(self.centralwidget)
        self.Income.setGeometry(QtCore.QRect(120, 250, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Income.setFont(font)
        self.Income.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Income.setObjectName("Income")
        self.TimeLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_5.setGeometry(QtCore.QRect(830, 90, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_5.setFont(font)
        self.TimeLabel_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_5.setObjectName("TimeLabel_5")
        self.TimeLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_6.setGeometry(QtCore.QRect(730, 172, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_6.setFont(font)
        self.TimeLabel_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_6.setObjectName("TimeLabel_6")
        self.TimeLabel_7 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_7.setGeometry(QtCore.QRect(900, 172, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_7.setFont(font)
        self.TimeLabel_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_7.setObjectName("TimeLabel_7")
        self.fromAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.fromAmount.setGeometry(QtCore.QRect(800, 180, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.fromAmount.setFont(font)
        self.fromAmount.setStyleSheet("QLineEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}")
        self.fromAmount.setObjectName("fromAmount")
        self.toAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.toAmount.setGeometry(QtCore.QRect(940, 180, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.toAmount.setFont(font)
        self.toAmount.setStyleSheet("QLineEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}")
        self.toAmount.setObjectName("toAmount")
        self.tickButton = QtWidgets.QPushButton(self.centralwidget)
        self.tickButton.setGeometry(QtCore.QRect(1050, 170, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tickButton.setFont(font)
        self.tickButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tickButton.setStyleSheet("QPushButton{\n"
"    background: rgb(139, 229, 253);\n"
"    background-image: url(resources/tick.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(133, 221, 243);\n"
"    background-image: url(resources/tick.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(128, 212, 233);\n"
"    background-image: url(resources/tick.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}")
        self.tickButton.setText("")
        self.tickButton.setObjectName("tickButton")
        self.Income_2 = QtWidgets.QLabel(self.centralwidget)
        self.Income_2.setGeometry(QtCore.QRect(60, 490, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Income_2.setFont(font)
        self.Income_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Income_2.setObjectName("Income_2")
        self.TimeLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_4.setGeometry(QtCore.QRect(290, 410, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_4.setFont(font)
        self.TimeLabel_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_4.setObjectName("TimeLabel_4")
        self.toAmount_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.toAmount_2.setGeometry(QtCore.QRect(940, 418, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.toAmount_2.setFont(font)
        self.toAmount_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}")
        self.toAmount_2.setObjectName("toAmount_2")
        self.TimeLabel_9 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_9.setGeometry(QtCore.QRect(520, 410, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_9.setFont(font)
        self.TimeLabel_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_9.setObjectName("TimeLabel_9")
        self.tickButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.tickButton_2.setGeometry(QtCore.QRect(1050, 410, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tickButton_2.setFont(font)
        self.tickButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tickButton_2.setStyleSheet("QPushButton{\n"
"    background: rgb(139, 229, 253);\n"
"    background-image: url(resources/tick.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(133, 221, 243);\n"
"    background-image: url(resources/tick.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(128, 212, 233);\n"
"    background-image: url(resources/tick.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}")
        self.tickButton_2.setText("")
        self.tickButton_2.setObjectName("tickButton_2")
        self.fromAmount_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.fromAmount_2.setGeometry(QtCore.QRect(800, 418, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.fromAmount_2.setFont(font)
        self.fromAmount_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}")
        self.fromAmount_2.setObjectName("fromAmount_2")
        self.TimeLabel_11 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_11.setGeometry(QtCore.QRect(730, 410, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_11.setFont(font)
        self.TimeLabel_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_11.setObjectName("TimeLabel_11")
        self.fromDate = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.fromDate.setGeometry(QtCore.QRect(360, 180, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setWeight(50)
        self.fromDate.setFont(font)
        self.fromDate.setStyleSheet("QDateTimeEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
" \n"
"QDateTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.fromDate.setObjectName("fromDate")
        self.toDate = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.toDate.setGeometry(QtCore.QRect(560, 180, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setWeight(50)
        self.toDate.setFont(font)
        self.toDate.setStyleSheet("QDateTimeEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
" \n"
"QDateTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.toDate.setObjectName("toDate")
        self.toDate_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.toDate_2.setGeometry(QtCore.QRect(560, 420, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setWeight(50)
        self.toDate_2.setFont(font)
        self.toDate_2.setStyleSheet("QDateTimeEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
" \n"
"QDateTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.toDate_2.setObjectName("toDate_2")
        self.fromDate_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.fromDate_2.setGeometry(QtCore.QRect(360, 420, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setWeight(50)
        self.fromDate_2.setFont(font)
        self.fromDate_2.setStyleSheet("QDateTimeEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"}\n"
" \n"
"QDateTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.fromDate_2.setObjectName("fromDate_2")
        self.TimeLabel_8 = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel_8.setGeometry(QtCore.QRect(900, 410, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel_8.setFont(font)
        self.TimeLabel_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeLabel_8.setObjectName("TimeLabel_8")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(930, 650, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.backButton.setStyleSheet("QPushButton{\n"
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
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.hintLabel = QtWidgets.QLabel(self.centralwidget)
        self.hintLabel.setGeometry(QtCore.QRect(290, 285, 810, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        self.hintLabel.setFont(font)
        self.hintLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hintLabel.setObjectName("hintLabel")
        self.hintLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.hintLabel_2.setGeometry(QtCore.QRect(290, 525, 810, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        self.hintLabel_2.setFont(font)
        self.hintLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hintLabel_2.setObjectName("hintLabel_2")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(290, 650, 131, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.refreshButton.setFont(font)
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.refreshButton.setStyleSheet("QPushButton{\n"
"    background: rgb(139, 229, 253);\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(133, 221, 243);\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(128, 212, 233);\n"
"    border-radius: 25px;\n"
"    color:rgb(0, 55, 128);\n"
"}")
        self.refreshButton.setObjectName("refreshButton")
        self.outScrollArea.raise_()
        self.inScrollArea.raise_()
        self.logoLabel.raise_()
        self.TimeLabel.raise_()
        self.TimeLabel_2.raise_()
        self.TimeLabel_3.raise_()
        self.transferTitleLabel.raise_()
        self.Income.raise_()
        self.TimeLabel_5.raise_()
        self.TimeLabel_6.raise_()
        self.TimeLabel_7.raise_()
        self.fromAmount.raise_()
        self.toAmount.raise_()
        self.tickButton.raise_()
        self.Income_2.raise_()
        self.TimeLabel_4.raise_()
        self.toAmount_2.raise_()
        self.TimeLabel_9.raise_()
        self.tickButton_2.raise_()
        self.fromAmount_2.raise_()
        self.TimeLabel_11.raise_()
        self.fromDate.raise_()
        self.toDate.raise_()
        self.toDate_2.raise_()
        self.fromDate_2.raise_()
        self.TimeLabel_8.raise_()
        self.backButton.raise_()
        self.hintLabel.raise_()
        self.hintLabel_2.raise_()
        self.refreshButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iKYC"))
        self.transferTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#003780;\">Transaction History</span></p></body></html>"))
        self.TimeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#003780;\">Time</span></p></body></html>"))
        self.TimeLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">from: </span></p></body></html>"))
        self.TimeLabel_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">to: </span></p></body></html>"))
        self.Income.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#003780;\">Income</span></p></body></html>"))
        self.TimeLabel_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#003780;\">Amount</span></p></body></html>"))
        self.TimeLabel_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">from: </span></p></body></html>"))
        self.TimeLabel_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">to: </span></p></body></html>"))
        self.Income_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#003780;\">Expenditure</span></p></body></html>"))
        self.TimeLabel_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">from: </span></p></body></html>"))
        self.TimeLabel_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">to: </span></p></body></html>"))
        self.TimeLabel_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">from: </span></p></body></html>"))
        self.TimeLabel_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#003780;\">to: </span></p></body></html>"))
        self.hintLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#003780;\">No     record!</span></p></body></html>"))
        self.hintLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#003780;\">No record!</span></p></body></html>"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
