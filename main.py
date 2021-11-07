import sys
import time

import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

WIDTH = 1200
HEIGHT = 800

CONF = 50

WELCOME = 0
FACE = 1
HOME = 2
PROFILE = 3
ACCOUNT = 4
TRANSFER = 5
TRANSACTION = 6
LOAN = 7
ACCOUNT_DETAIL = 8
APPLY_LOAN = 9
PAY_LOAN = 10

CURRENCY = ["HKD", "Deposit", "USD", "CNY"]


def switch_to(idx):
    currentWin = mainWin.currentWidget()
    currentWin.deactivate()
    mainWin.removeWidget(currentWin)
    mainWin.addWidget(winList[idx])
    mainWin.currentWidget().activate()


class StackedWindow(QMainWindow):
    def __init__(self):
        super(StackedWindow, self).__init__()

    def activate(self):
        pass

    def deactivate(self):
        pass


class WelcomeWindow(StackedWindow):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        loadUi("welcome.ui", self)
        self.slot_init()
        self.set_greeting()

    def slot_init(self):
        self.loginButton.clicked.connect(lambda: switch_to(FACE))
        self.leaveButton.clicked.connect(self.leave)

    def activate(self):
        self.set_greeting()

    def set_greeting(self):
        current_time = time.localtime()
        if current_time.tm_hour < 6:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Night!</span></p></body></html>")
        elif current_time.tm_hour < 12:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Morning!</span></p></body></html>")
        elif current_time.tm_hour < 18:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Afternoon!</span></p></body></html>")
        else:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Evening!</span></p></body></html>")

    def leave(self):
        cursor.close()
        conn.close()
        exit(0)


class FaceWindow(StackedWindow):
    def __init__(self):
        super(FaceWindow, self).__init__()
        loadUi("face.ui", self)

        self.user_id = -1
        self.image = None
        self.timer = QtCore.QTimer()
        self.CAM_NUM = 0
        self.cap = cv2.VideoCapture()

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        # self.recognizer.read("train.yml")
        self.labels = {"user_id": 1}
        # with open("labels.pickle", "rb") as f:
        #    self.labels = pickle.load(f)
        #    self.labels = {v: k for k, v in self.labels.items()}
        self.face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

        self.slot_init()

    def slot_init(self):
        self.timer.timeout.connect(self.display)
        self.backButton.clicked.connect(lambda: switch_to(WELCOME))
        self.verifyButton.clicked.connect(self.verify)

    def activate(self):
        self.hintLabel.setText(
            '<html><head/><body><p><span style=" color:#646464;">Please keep your face displayed in the circle and click </span><span style=" font-weight:600; color:#646464;">Verify</span></p></body></html>'
        )
        self.user_id = -1
        self.start()

    def deactivate(self):
        self.stop()

    def start(self):
        self.cap.open(self.CAM_NUM, cv2.CAP_DSHOW)
        self.timer.start(50)

    def stop(self):
        self.timer.stop()
        self.cap.release()

    def display(self):
        flag, self.image = self.cap.read()
        h, w = self.image.shape[:2]
        l = int((w - h) / 2)
        square_image = self.image[:, l:l + h]
        square_image = cv2.flip(square_image, 1)
        square_image = cv2.resize(square_image, (400, 400))
        square_image = cv2.cvtColor(square_image, cv2.COLOR_BGR2RGB)
        show_image = QtGui.QImage(square_image.data, square_image.shape[1], square_image.shape[0],
                                  QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(show_image)
        self.camera.setPixmap(pixmap)

        # TODO: for debug
        self.user_id = 1

        # if self.user_id == -1:
        #     gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        #     faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
        #     for (x, y, w, h) in faces:
        #         roi_gray = gray[y:y + h, x:x + w]
        #         id_, conf = self.recognizer.predict(roi_gray)
        #         if conf >= CONF:
        #             self.user_id = self.labels[id_]

    def verify(self):
        if self.user_id != -1:
            # TODO
            self.stop()
            winList[HOME] = HomeWindow(self.user_id)
            winList[PROFILE] = ProfileWindow(self.user_id)
            winList[ACCOUNT] = AccountWindow(self.user_id)
            winList[TRANSFER] = TransferWindow(self.user_id)
            winList[TRANSACTION] = TransactionWindow(self.user_id)
            winList[LOAN] = LoanWindow(self.user_id)
            switch_to(HOME)
        else:
            self.hintLabel.setText(
                '<html><head/><body><p align="center"><span style=" font-weight:600; color:#646464;">Unrecognized</span><span style=" font-weight:600; color:#646464;"><br/></span><span style=" color:#646464;">Please adjust your posture and try again</span></p></body></html>'
            )


class HomeWindow(StackedWindow):
    def __init__(self, user_id):
        super(HomeWindow, self).__init__()
        loadUi('home.ui', self)
        self.user_id = user_id
        self.name = ''
        self.last_login_time = ''
        self.login_history = []
        self.loans = []
        self.login_history_labels = []
        self.loan_labels = []
        self.slot_init()
        self.update_login_time()

    def slot_init(self):
        self.logoutButton.clicked.connect(lambda: switch_to(WELCOME))
        # TODO
        self.profileButton.clicked.connect(lambda: switch_to(PROFILE))
        self.accountButton.clicked.connect(lambda: switch_to(ACCOUNT))
        self.transferButton.clicked.connect(lambda: switch_to(TRANSFER))
        self.transactionButton.clicked.connect(lambda: switch_to(TRANSACTION))
        self.loanButton.clicked.connect(lambda: switch_to(LOAN))

    def create_label(self, height):
        new_label = QtWidgets.QLabel(self.historyScrollAreaWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(new_label.sizePolicy().hasHeightForWidth())
        new_label.setSizePolicy(sizePolicy)
        new_label.setMinimumSize(QtCore.QSize(0, height))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        new_label.setFont(font)
        return new_label

    def get_data(self):
        sql = "SELECT name FROM User WHERE user_id='%s'" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.name = result[0][0]

        sql = "SELECT login_time FROM LoginTime WHERE user_id='%s' ORDER BY login_time DESC" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.last_login_time = result[1][0]
        self.login_history = result

        # TODO: get loans
        sql = "SELECT loan_id, loan_amount, due_date FROM Loan WHERE user_id='%s' ORDER BY due_date DESC" % self.user_id
        cursor.execute(sql)
        self.loans = cursor.fetchall()

    def set_content(self):
        self.homeTitleLabel.setText(
            f'<html><head/><body><p><span style=" color:#003780;">Welcome back, {self.name}!</span></p></body></html>')
        self.lastLoginTimeLabel.setText(
            f'<html><head/><body><p><span style=" font-size:12pt; color:#646464;">Last login time:<br/>{self.last_login_time}</span></p></body></html>')
        for label in self.login_history_labels:
            self.verticalLayout_4.removeWidget(label)
        self.login_history_labels = []
        for label in self.loan_labels:
            self.verticalLayout.removeWidget(label)
        self.loan_labels = []
        for i, history in enumerate(self.login_history[1:]):
            label = self.create_label(height=40)
            label.setText(f'<html><head/><body><p>{history[0]}</p></body></html>')
            self.verticalLayout_4.insertWidget(i, label)
            self.login_history_labels.append(label)
        for i, loan in enumerate(self.loans):
            label = self.create_label(height=70)
            label.setText(
                f'<html><head/><body><p><span style=" font-weight:600;">Amount:</span> HKD {loan[1]}<br/><span style=" font-weight:600;">Due Date:</span> {loan[2]}</p></body></html>')
            self.verticalLayout.insertWidget(i, label)
            self.loan_labels.append(label)

    def activate(self):
        self.get_data()
        self.set_content()

    def update_login_time(self):
        now = time.localtime()
        year = str(now.tm_year).zfill(4)
        mon = str(now.tm_mon).zfill(2)
        mday = str(now.tm_mday).zfill(2)
        hour = str(now.tm_hour).zfill(2)
        min = str(now.tm_min).zfill(2)
        sec = str(now.tm_sec).zfill(2)
        now_str = f'{year}-{mon}-{mday} {hour}:{min}:{sec}'
        sql = "INSERT INTO LoginTime VALUES (%s, %s)"
        val = (self.user_id, now_str)
        cursor.execute(sql, val)
        conn.commit()


class ProfileWindow(StackedWindow):
    def __init__(self, user_id):
        super(ProfileWindow, self).__init__()
        loadUi('profile.ui', self)
        self.user_id = user_id
        self.name = ''
        self.last_login_time = ''
        self.slot_init()

    def slot_init(self):
        self.backButton.clicked.connect(lambda: switch_to(HOME))

    def activate(self):
        self.get_data()
        self.set_content()

    def get_data(self):
        sql = "SELECT name FROM User WHERE user_id='%s'" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.name = result[0][0]

        sql = "SELECT login_time FROM LoginTime WHERE user_id='%s' ORDER BY login_time DESC" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.last_login_time = result[1][0]

    def set_content(self):
        self.uid_value.setText(
            f'<html><head/><body><p><span style=" font-size:22pt; font-weight:400; color:#476089;">{self.user_id}</span></p></body></html>')
        self.name_value.setText(
            f'<html><head/><body><p><span style=" font-size:22pt; font-weight:400; color:#476089;">{self.name}</span></p></body></html>')
        self.log_value.setText(
            f'<html><head/><body><p><span style=" font-size:22pt; font-weight:400; color:#476089;">{self.last_login_time}</span></p></body></html>')


class AccountWindow(StackedWindow):
    def __init__(self, user_id):
        super(AccountWindow, self).__init__()
        loadUi('accounts.ui', self)
        self.user_id = user_id

        self.slot_init()

    def slot_init(self):
        self.backButton.clicked.connect(lambda: switch_to(HOME))
        self.HKDButton.clicked.connect(self.hkd_clicked)
        self.depositButton.clicked.connect(self.deposit_clicked)
        self.USDButton.clicked.connect(self.usd_clicked)
        self.CNYButton.clicked.connect(self.cny_clicked)

    def activate(self):
        self.get_data()

    def get_data(self):
        sql = "SELECT user_id, account_id, balance FROM account WHERE user_id='%s' ORDER BY account_id" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        hkd_balance = result[0][2]
        deposit_balance = result[1][2]
        usd_balance = result[2][2]
        cny_balance = result[3][2]
        self.HKDButton.setText("$" + str(hkd_balance))
        self.depositButton.setText("$" + str(deposit_balance))
        self.USDButton.setText("$" + str(usd_balance))
        self.CNYButton.setText("￥" + str(cny_balance))

    def hkd_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 1)
        switch_to(ACCOUNT_DETAIL)

    def deposit_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 2)
        switch_to(ACCOUNT_DETAIL)

    def usd_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 3)
        switch_to(ACCOUNT_DETAIL)

    def cny_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 4)
        switch_to(ACCOUNT_DETAIL)


class AccountDetailWindow(StackedWindow):
    def __init__(self, user_id, account_id):
        super(AccountDetailWindow, self).__init__()
        loadUi('accountsDetail.ui', self)
        self.user_id = user_id
        self.account_id = account_id

        self.slot_init()

    def slot_init(self):
        self.backButton.clicked.connect(lambda: switch_to(ACCOUNT))
        self.HKDButton.clicked.connect(self.hkd_clicked)
        self.depositButton.clicked.connect(self.deposit_clicked)
        self.USDButton.clicked.connect(self.usd_clicked)
        self.CNYButton.clicked.connect(self.cny_clicked)
        self.titleLabel.setText(CURRENCY[self.account_id-1]+' Account')

        if self.account_id==2:
            self.remittanceTable.setVisible(False)
            self.receivedTable.setVisible(False)
            self.remittanceLabel.setVisible(False)
            self.receivedLabel.setVisible(False)
            self.balanceWidge.setGeometry(500,230,200,200)
        
        self.remittanceTable.setShowGrid(False)
        self.receivedTable.setShowGrid(False)
        self.remittanceTable.verticalHeader().setVisible(False)
        self.receivedTable.verticalHeader().setVisible(False)
        self.remittanceTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.receivedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def activate(self):
        self.get_data()

    def get_data(self):
        sql = "SELECT balance FROM account WHERE user_id='" + str(self.user_id) + "' AND account_id='" + str(
            self.account_id) + "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        balance = result[0][0]
        if self.account_id == 4:
            self.balanceAmountLabel.setText("￥" + str(balance))
        else:
            self.balanceAmountLabel.setText("$" + str(balance))

        sql = "SELECT to_user, amount, transaction_time FROM transaction WHERE from_user='"+str(self.user_id)+"' AND current_type='"+CURRENCY[self.account_id-1]+"'"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in range(len(result)):
            newItem=QTableWidgetItem(str(i))
            self.remittanceTable.setItem(i,0,newItem)
            newItem=QTableWidgetItem(str(result[i][2]))
            self.remittanceTable.setItem(i,1,newItem)
            newItem=QTableWidgetItem(str(result[i][1]))
            self.remittanceTable.setItem(i,2,newItem)
            newItem=QTableWidgetItem(CURRENCY[self.account_id-1])
            self.remittanceTable.setItem(i,3,newItem)
            uid = result[i][0]
            sql = "SELECT name FROM user WHERE user_id='"+str(uid)+"'"
            cursor.execute(sql)
            name_result = cursor.fetchall()
            newItem=QTableWidgetItem(name_result[0][0])
            self.remittanceTable.setItem(i,4,newItem)

        sql = "SELECT from_user, amount, transaction_time FROM transaction WHERE to_user='"+str(self.user_id)+"' AND current_type='"+CURRENCY[self.account_id-1]+"'"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in range(len(result)):
            newItem=QTableWidgetItem(str(i))
            self.receivedTable.setItem(i,0,newItem)
            newItem=QTableWidgetItem(str(result[i][2]))
            self.receivedTable.setItem(i,1,newItem)
            newItem=QTableWidgetItem(str(result[i][1]))
            self.receivedTable.setItem(i,2,newItem)
            newItem=QTableWidgetItem(CURRENCY[self.account_id-1])
            self.receivedTable.setItem(i,3,newItem)
            uid = result[i][0]
            sql = "SELECT name FROM user WHERE user_id='"+str(uid)+"'"
            cursor.execute(sql)
            name_result = cursor.fetchall()
            newItem=QTableWidgetItem(name_result[0][0])
            self.receivedTable.setItem(i,4,newItem)


    def hkd_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 1)
        switch_to(ACCOUNT_DETAIL)

    def deposit_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 2)
        switch_to(ACCOUNT_DETAIL)

    def usd_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 3)
        switch_to(ACCOUNT_DETAIL)

    def cny_clicked(self):
        winList[ACCOUNT_DETAIL] = AccountDetailWindow(self.user_id, 4)
        switch_to(ACCOUNT_DETAIL)


class TransferWindow(StackedWindow):
    def __init__(self, user_id):
        super(TransferWindow, self).__init__()
        loadUi('transfer.ui', self)
        self.idEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.amountEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]*")))
        self.user_id = user_id
        self.to_id = -1
        self.account = ''
        self.amount = 0
        self.transfers = []
        self.transfer_labels = []
        self.slot_init()

    def slot_init(self):
        self.backButton.clicked.connect(lambda: switch_to(HOME))
        self.clearButton.clicked.connect(self.clear)
        self.transferButton.clicked.connect(self.transfer)

    def activate(self):
        self.get_data()
        self.set_content()

    def create_label(self, height):
        new_label = QtWidgets.QLabel(self.transferScrollAreaWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(new_label.sizePolicy().hasHeightForWidth())
        new_label.setSizePolicy(sizePolicy)
        new_label.setMinimumSize(QtCore.QSize(0, height))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        new_label.setFont(font)
        return new_label

    def get_data(self):
        return
        sql = "SELECT user_id, account_id, balance FROM account WHERE user_id='%s' ORDER BY account_id" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.transfers = result

    def set_content(self):
        for label in self.transfer_labels:
            self.verticalLayout_4.removeWidget(label)
        self.transfer_labels = []
        for i, transfer in enumerate(self.transfers):
            label = self.create_label(height=40)
            label.setText(f'<html><head/><body><p>{transfer[0]} {transfer[1]}</p></body></html>')
            self.verticalLayout_4.insertWidget(i, label)
            self.transfer_labels.append(label)

    def clear(self):
        self.idEdit.setText('')
        self.accountBox.setCurrentIndex(0)
        self.amountEdit.setText('')

    def transfer(self):
        self.to_id = int(self.idEdit.text().zfill(1))
        self.account = self.accountBox.currentText()
        self.amount = int(self.amountEdit.text().zfill(1))
        # TODO: Do more on transfer
        self.clear()
        self.activate()


class TransactionWindow(StackedWindow):
    def __init__(self, user_id):
        super(TransactionWindow, self).__init__()
        loadUi('transaction.ui', self)
        self.user_id = user_id

        self.slot_init()

    def slot_init(self):
        self.backButton_2.clicked.connect(lambda: switch_to(HOME))


class LoanWindow(StackedWindow):
    def __init__(self, user_id):
        super(LoanWindow, self).__init__()
        loadUi('loanHome.ui', self)
        self.user_id = user_id


if __name__ == "__main__":
    conn = mysql.connector.connect(host="localhost", user="root", passwd="123456",
                                   database="project")  # Modify if needed
    cursor = conn.cursor()
    app = QApplication(sys.argv)

    winList = [WelcomeWindow(), FaceWindow(), None, None, None, None, None, None, None, None, None]

    mainWin = QStackedWidget()
    mainWin.setFixedWidth(WIDTH)
    mainWin.setFixedHeight(HEIGHT)
    mainWin.setWindowTitle('iKYC')
    mainWin.setWindowIcon(QtGui.QIcon('resources/small_logo.png'))
    mainWin.addWidget(winList[WELCOME])

    mainWin.show()
    sys.exit(app.exec_())
