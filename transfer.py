# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transfer.ui'
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.small_logo = QtWidgets.QLabel(self.centralwidget)
        self.small_logo.setGeometry(QtCore.QRect(-60, -190, 391, 391))
        self.small_logo.setText("")
        self.small_logo.setPixmap(QtGui.QPixmap("resources/small_logo.png"))
        self.small_logo.setScaledContents(True)
        self.small_logo.setObjectName("small_logo")
        self.transferTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.transferTitleLabel.setGeometry(QtCore.QRect(190, 30, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.transferTitleLabel.setFont(font)
        self.transferTitleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transferTitleLabel.setObjectName("transferTitleLabel")
        self.profileButton = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton.setGeometry(QtCore.QRect(210, 600, 150, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.profileButton.setFont(font)
        self.profileButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.profileButton.setStyleSheet("QPushButton{\n"
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
        self.profileButton.setObjectName("profileButton")
        self.profileLabel = QtWidgets.QLabel(self.centralwidget)
        self.profileLabel.setGeometry(QtCore.QRect(190, 230, 121, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.profileLabel.setFont(font)
        self.profileLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.profileLabel.setObjectName("profileLabel")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(640, 180, 451, 511))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea_2.setFont(font)
        self.scrollArea_2.setStyleSheet("QWidget{\n"
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
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.friendScrollAreaWidget_4 = QtWidgets.QWidget()
        self.friendScrollAreaWidget_4.setGeometry(QtCore.QRect(0, 0, 441, 675))
        self.friendScrollAreaWidget_4.setAutoFillBackground(False)
        self.friendScrollAreaWidget_4.setObjectName("friendScrollAreaWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.friendScrollAreaWidget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.recentLabel = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.recentLabel.setFont(font)
        self.recentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.recentLabel.setObjectName("recentLabel")
        self.verticalLayout_4.addWidget(self.recentLabel)
        self.label_26 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_4.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_4.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_4.addWidget(self.label_28)
        self.label_30 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_4.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_4.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_4.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_4.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.friendScrollAreaWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_4.addWidget(self.label_34)
        self.scrollArea_2.setWidget(self.friendScrollAreaWidget_4)
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
"    background-image : url(resources/small_back.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(0, 71, 163);\n"
"    background-image : url(resources/small_back.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: #004094;\n"
"    background-image : url(resources/small_back.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border-radius: 30px;\n"
"}")
        self.logoutButton.setText("")
        self.logoutButton.setObjectName("logoutButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 230, 240, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background: rgb(0, 55, 128);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.profileLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.profileLabel_2.setGeometry(QtCore.QRect(160, 350, 151, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.profileLabel_2.setFont(font)
        self.profileLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.profileLabel_2.setObjectName("profileLabel_2")
        self.accountBox = QtWidgets.QComboBox(self.centralwidget)
        self.accountBox.setGeometry(QtCore.QRect(340, 350, 231, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.accountBox.setFont(font)
        self.accountBox.setAcceptDrops(False)
        self.accountBox.setStyleSheet("QComboBox{\n"
"    background: rgb(0, 55, 128);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding-left: 95px;\n"
"}\n"
"")
        self.accountBox.setEditable(False)
        self.accountBox.setFrame(True)
        self.accountBox.setObjectName("accountBox")
        self.accountBox.addItem("")
        self.accountBox.addItem("")
        self.accountBox.addItem("")
        self.profileLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.profileLabel_3.setGeometry(QtCore.QRect(180, 470, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.profileLabel_3.setFont(font)
        self.profileLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.profileLabel_3.setObjectName("profileLabel_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 470, 240, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background: rgb(0, 55, 128);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.profileButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton_2.setGeometry(QtCore.QRect(400, 600, 150, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.profileButton_2.setFont(font)
        self.profileButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.profileButton_2.setStyleSheet("QPushButton{\n"
"    background: rgb(245, 243, 251);\n"
"    color: #003780;\n"
"    border-radius: 15px;\n"
"    border: 2px solid #003780\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(235, 233, 241);\n"
"    color: #003780;\n"
"    border-radius: 15px;\n"
"    border: 2px solid #003780;\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(226, 224, 231);\n"
"    color: #003780;\n"
"    border-radius: 15px;\n"
"    border: 2px solid #003780;\n"
"}")
        self.profileButton_2.setObjectName("profileButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 350, 72, 50))
        self.label.setStyleSheet("QLabel{\n"
"    background: rgb(0, 55, 128);\n"
"    border-radius: 10px;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.small_logo.raise_()
        self.transferTitleLabel.raise_()
        self.profileButton.raise_()
        self.scrollArea_2.raise_()
        self.logoutButton.raise_()
        self.profileLabel.raise_()
        self.lineEdit.raise_()
        self.profileLabel_2.raise_()
        self.accountBox.raise_()
        self.profileLabel_3.raise_()
        self.lineEdit_2.raise_()
        self.profileButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iKYC"))
        self.transferTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#003780;\">Transfer</span></p></body></html>"))
        self.profileButton.setText(_translate("MainWindow", "Transfer"))
        self.profileLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#003780;\">User ID:</span></p></body></html>"))
        self.recentLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#003780;\">Recent Transfer</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p>1 Guo Ruo Xuan 12:00:00 01-01-1970 HKD600</p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.profileLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#003780;\">Account:</span></p></body></html>"))
        self.accountBox.setItemText(0, _translate("MainWindow", "HKD"))
        self.accountBox.setItemText(1, _translate("MainWindow", "USD"))
        self.accountBox.setItemText(2, _translate("MainWindow", "CNY"))
        self.profileLabel_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#003780;\">Amount:</span></p><p><br/></p></body></html>"))
        self.lineEdit_2.setText(_translate("MainWindow", "666"))
        self.profileButton_2.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
