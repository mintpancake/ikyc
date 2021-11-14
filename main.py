import sys
import time

import cv2
import mysql.connector
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

WIDTH = 1200
HEIGHT = 800

CONF = 40

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
        self.recognizer.read("train.yml")
        self.labels = {"user_id": 1}
        with open("labels.pickle", "rb") as f:
           self.labels = pickle.load(f)
           self.labels = {v: k for k, v in self.labels.items()}
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

        if self.user_id == -1:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                id_, conf = self.recognizer.predict(roi_gray)
                if conf >= CONF:
                    self.user_id = self.labels[id_]

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
            winList[APPLY_LOAN] = ApplyLoanWindow(self.user_id)
            winList[PAY_LOAN] = PayLoanWindow(self.user_id)
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
        self.login_history = result
        if len(result) > 1:
            self.last_login_time = result[1][0]
        else:
            self.last_login_time = 'No record'

        # TODO: get loans
        sql = "SELECT loan_id, loan_amount, due_date FROM Loan WHERE user_id='%s' AND is_settled=0 ORDER BY due_date ASC" % self.user_id
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
        if len(result) > 1:
            self.last_login_time = result[1][0]
        else:
            self.last_login_time = 'No record'

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
        self.titleLabel.setText(CURRENCY[self.account_id - 1] + ' Account')

        self.income_labels = []
        self.expenditure_labels = []

        self.tickButton_2.clicked.connect(self.search_income)
        self.tickButton.clicked.connect(self.search_expenditure)
        self.refreshButton.clicked.connect(self.activate)

        if self.account_id == 2:
            self.outScrollArea.setVisible(False)
            self.titleLabel_2.setVisible(False)
            self.TimeLabel_2.setVisible(False)
            self.fromDate.setVisible(False)
            self.TimeLabel_3.setVisible(False)
            self.toDate.setVisible(False)
            self.TimeLabel_6.setVisible(False)
            self.fromAmount.setVisible(False)
            self.TimeLabel_7.setVisible(False)
            self.toAmount.setVisible(False)
            self.tickButton.setVisible(False)
            self.hintLabel.setVisible(False)

            self.inScrollArea.setVisible(False)
            self.titleLabel_3.setVisible(False)
            self.TimeLabel_4.setVisible(False)
            self.fromDate_2.setVisible(False)
            self.TimeLabel_9.setVisible(False)
            self.toDate_2.setVisible(False)
            self.TimeLabel_11.setVisible(False)
            self.fromAmount_2.setVisible(False)
            self.TimeLabel_8.setVisible(False)
            self.toAmount_2.setVisible(False)
            self.tickButton_2.setVisible(False)
            self.hintLabel_2.setVisible(False)
            self.refreshButton.setVisible(False)
            self.balanceWidge.setGeometry(500, 230, 200, 200)

        # self.remittanceTable.setShowGrid(False)
        # self.receivedTable.setShowGrid(False)
        # self.remittanceTable.verticalHeader().setVisible(False)
        # self.receivedTable.verticalHeader().setVisible(False)
        # self.remittanceTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.receivedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

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

        # sql = "SELECT to_user, amount, transaction_time FROM transaction WHERE from_user='" + str(
        #    self.user_id) + "' AND currency_type='" + CURRENCY[self.account_id - 1] + "'"
        sql = "SELECT T.to_account,\
                    T.currency_type,\
                    T.amount,\
                    T.transaction_time,\
                    U.name\
                    FROM Transaction T,\
                    User U\
                    WHERE T.from_user = " + str(self.user_id) + "\
                    AND T.to_user = U.user_id\
                    AND T.currency_type='" + CURRENCY[self.account_id - 1] + "'\
                    ORDER BY T.transaction_time DESC;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for label in self.expenditure_labels:
            self.verticalLayout_4.removeWidget(label)
        self.expenditure_labels = []
        if len(result) == 0 and self.account_id != 2:
            self.hintLabel.setVisible(True)
            self.hintLabel.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            self.hintLabel.setVisible(False)
            for i, trans in enumerate(result):
                label = self.create_label(area=self.outScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">From:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_4.insertWidget(i, label)
                self.expenditure_labels.append(label)
        # for i in range(len(result)):
        #    newItem = QTableWidgetItem(str(i))
        #    self.remittanceTable.setItem(i, 0, newItem)
        #    newItem = QTableWidgetItem(str(result[i][2]))
        #    self.remittanceTable.setItem(i, 1, newItem)
        #    newItem = QTableWidgetItem(str(result[i][1]))
        #    self.remittanceTable.setItem(i, 2, newItem)
        #    newItem = QTableWidgetItem(CURRENCY[self.account_id - 1])
        #    self.remittanceTable.setItem(i, 3, newItem)
        #    uid = result[i][0]
        #    sql = "SELECT name FROM user WHERE user_id='" + str(uid) + "'"
        #    cursor.execute(sql)
        #    name_result = cursor.fetchall()
        #    newItem = QTableWidgetItem(name_result[0][0])
        #    self.remittanceTable.setItem(i, 4, newItem)

        # sql = "SELECT from_user, amount, transaction_time FROM transaction WHERE to_user='" + str(
        #    self.user_id) + "' AND currency_type='" + CURRENCY[self.account_id - 1] + "'"
        sql = "SELECT T.to_account,\
                    T.currency_type,\
                    T.amount,\
                    T.transaction_time,\
                    U.name\
                    FROM Transaction T,\
                    User U\
                    WHERE T.to_user = " + str(self.user_id) + "\
                    AND T.from_user = U.user_id\
                    AND T.currency_type='" + CURRENCY[self.account_id - 1] + "'\
                    ORDER BY T.transaction_time DESC;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for label in self.income_labels:
            self.verticalLayout_5.removeWidget(label)
        self.income_labels = []
        if len(result) == 0 and self.account_id != 2:
            self.hintLabel_2.setVisible(True)
            self.hintLabel_2.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            self.hintLabel_2.setVisible(False)
            for i, trans in enumerate(result):
                label = self.create_label(area=self.inScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">To:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_5.insertWidget(i, label)
                self.income_labels.append(label)
        # for i in range(len(result)):
        #    newItem = QTableWidgetItem(str(i))
        #    self.receivedTable.setItem(i, 0, newItem)
        #    newItem = QTableWidgetItem(str(result[i][2]))
        #    self.receivedTable.setItem(i, 1, newItem)
        #    newItem = QTableWidgetItem(str(result[i][1]))
        #    self.receivedTable.setItem(i, 2, newItem)
        #    newItem = QTableWidgetItem(CURRENCY[self.account_id - 1])
        #    self.receivedTable.setItem(i, 3, newItem)
        #    uid = result[i][0]
        #    sql = "SELECT name FROM user WHERE user_id='" + str(uid) + "'"
        #    cursor.execute(sql)
        #    name_result = cursor.fetchall()
        #    newItem = QTableWidgetItem(name_result[0][0])
        #    self.receivedTable.setItem(i, 4, newItem)

    def search_expenditure(self):
        from_date = self.fromDate.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        to_date = self.toDate.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        from_amount = int(self.fromAmount.text().zfill(1))
        to_amount = int(self.toAmount.text().zfill(1))

        sql = "SELECT T.from_account,\
                    T.currency_type,\
                    T.amount,\
                    T.transaction_time,\
                    U.name\
                    FROM Transaction T,\
                    User U\
                    WHERE T.from_user = '%s'\
                    AND T.to_user = U.user_id\
                    AND T.amount >= %s\
                    AND T.amount <= %s\
                    AND T.transaction_time >= '%s'\
                    AND T.transaction_time <= '%s'\
                    AND T.currency_type='%s'\
                    ORDER BY T.transaction_time DESC;" % (
        str(self.user_id), from_amount, to_amount, from_date, to_date, CURRENCY[self.account_id - 1])
        cursor.execute(sql)
        result = cursor.fetchall()

        for label in self.expenditure_labels:
            self.verticalLayout_4.removeWidget(label)
        self.expenditure_labels = []
        if len(result) == 0:
            self.hintLabel.setVisible(True)
            self.hintLabel.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            self.hintLabel.setVisible(False)
            for i, trans in enumerate(result):
                label = self.create_label(area=self.inScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">To:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_4.insertWidget(i, label)
                self.expenditure_labels.append(label)

    def search_income(self):
        from_date = self.fromDate_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        to_date = self.toDate_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        from_amount = int(self.fromAmount_2.text().zfill(1))
        to_amount = int(self.toAmount_2.text().zfill(1))

        sql = "SELECT T.to_account,\
            T.currency_type,\
            T.amount,\
            T.transaction_time,\
            U.name\
            FROM Transaction T,\
            User U\
            WHERE T.to_user = '%s'\
            AND T.from_user = U.user_id\
            AND T.amount >= %s\
            AND T.amount <= %s\
            AND T.transaction_time >= '%s'\
            AND T.transaction_time <= '%s'\
            AND T.currency_type='%s'\
            ORDER BY T.transaction_time DESC;" % (
        str(self.user_id), from_amount, to_amount, from_date, to_date, CURRENCY[self.account_id - 1])
        cursor.execute(sql)
        result = cursor.fetchall()

        for label in self.income_labels:
            self.verticalLayout_5.removeWidget(label)
        self.income_labels = []
        if len(result) == 0:
            self.hintLabel_2.setVisible(True)
            self.hintLabel_2.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            self.hintLabel_2.setVisible(False)
            for i, trans in enumerate(result):
                label = self.create_label(area=self.outScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">From:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_5.insertWidget(i, label)
                self.income_labels.append(label)

    def create_label(self, area, height):
        new_label = QtWidgets.QLabel(area)
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
        self.hintLabel.setText('')
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
        self.hintLabel.setText('')
        self.clear()
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
        sql = "SELECT T.currency_type,\
            T.amount,\
            T.transaction_time,\
            U.name,\
            U.user_id\
            FROM Transaction T,\
            User U\
            WHERE T.to_user = U.user_id\
            AND T.from_user = '%s'\
            ORDER BY T.transaction_time DESC;" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.transfers = result

    def set_content(self):
        for label in self.transfer_labels:
            self.verticalLayout_4.removeWidget(label)
        self.transfer_labels = []
        for i, transfer in enumerate(self.transfers):
            label = self.create_label(height=70)
            label.setText(
                f'<html><head/><body><p><span style=" font-weight:600;">To:</span> {transfer[3]} ({transfer[4]})&nbsp;&nbsp;&nbsp;&nbsp;<span style=" '
                f'font-weight:600;">Amount:</span> {transfer[0]} {transfer[1]}<br/><span style=" '
                f'font-weight:600;">Time:</span> {transfer[2]}</p></body></html>')
            self.verticalLayout_4.insertWidget(i, label)
            self.transfer_labels.append(label)

    def clear(self):
        self.idEdit.setText('')
        self.accountBox.setCurrentIndex(0)
        self.amountEdit.setText('')

    def transfer(self):
        self.to_id = int(self.idEdit.text().zfill(1))
        currency = self.accountBox.currentText()
        if currency == 'HKD':
            self.account = 1
        elif currency == 'USD':
            self.account = 3
        elif currency == 'CNY':
            self.account = 4
        self.amount = int(self.amountEdit.text().zfill(1))

        if self.to_id == self.user_id:
            self.hintLabel.setText('<html><head/><body><p><span style=" font-size:16pt; color:#003780;">Failed: '
                                   'Cannot transfer to yourself</span></p></body></html>')
            self.clear()
            return

        sql = "SELECT user_id FROM User;"
        cursor.execute(sql)
        ids = cursor.fetchall()
        not_in = True
        for i in ids:
            if self.to_id == i[0]:
                not_in = False
                break
        if not_in:
            self.hintLabel.setText(
                '<html><head/><body><p><span style=" font-size:16pt; color:#003780;">Failed: User does not '
                'exist</span></p></body></html>')
            self.clear()
            return

        sql = "SELECT balance FROM Account WHERE user_id='%s' AND account_id='%s';" % (self.user_id, self.account)
        cursor.execute(sql)
        my_balance = cursor.fetchall()[0][0]
        if self.amount > int(my_balance):
            self.hintLabel.setText(
                '<html><head/><body><p><span style=" font-size:16pt; color:#003780;">Failed: Insufficient '
                'balance</span></p></body></html>')
            self.clear()
            return

        sql = "UPDATE account SET balance=balance-'%s' WHERE user_id='%s' AND account_id='%s';"
        val = (self.amount, self.user_id, self.account)
        cursor.execute(sql, val)
        conn.commit()

        sql = "UPDATE account SET balance=balance+'%s' WHERE user_id='%s' AND account_id='%s';"
        val = (self.amount, self.to_id, self.account)
        cursor.execute(sql, val)
        conn.commit()

        sql = "SELECT MAX(transaction_id) FROM Transaction"
        cursor.execute(sql)
        max_trans_id = cursor.fetchall()[0][0]

        now = time.localtime()
        year = str(now.tm_year).zfill(4)
        mon = str(now.tm_mon).zfill(2)
        mday = str(now.tm_mday).zfill(2)
        hour = str(now.tm_hour).zfill(2)
        min = str(now.tm_min).zfill(2)
        sec = str(now.tm_sec).zfill(2)
        now_str = f'{year}-{mon}-{mday} {hour}:{min}:{sec}'

        sql = "INSERT INTO Transaction VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (max_trans_id + 1, self.user_id, self.to_id, self.account, self.account, currency, self.amount, now_str)
        cursor.execute(sql, val)
        conn.commit()

        self.hintLabel.setText(
            '<html><head/><body><p><span style=" font-size:16pt; color:#003780;">Transferred!</span></p></body></html>')
        self.clear()
        self.get_data()
        self.set_content()


class TransactionWindow(StackedWindow):
    def __init__(self, user_id):
        super(TransactionWindow, self).__init__()
        loadUi('transaction.ui', self)
        self.fromAmount.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.fromAmount_2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.toAmount.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.toAmount_2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*")))
        self.user_id = user_id
        self.income_labels = []
        self.expenditure_labels = []
        self.slot_init()

    def slot_init(self):
        self.backButton.clicked.connect(lambda: switch_to(HOME))
        self.tickButton.clicked.connect(self.search_income)
        self.tickButton_2.clicked.connect(self.search_expenditure)
        self.refreshButton.clicked.connect(self.activate)

    def activate(self):
        self.hintLabel.setText('')
        self.hintLabel_2.setText('')
        self.fromAmount.setText('')
        self.fromAmount_2.setText('')
        self.toAmount.setText('')
        self.toAmount_2.setText('')
        self.get_data()

    def get_data(self):
        sql = "SELECT T.to_account,\
                    T.currency_type,\
                    T.amount,\
                    T.transaction_time,\
                    U.name\
                    FROM Transaction T,\
                    User U\
                    WHERE T.to_user = '%s'\
                    AND T.from_user = U.user_id\
                    ORDER BY T.transaction_time DESC;" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        for label in self.income_labels:
            self.verticalLayout_4.removeWidget(label)
        self.income_labels = []
        if len(result) == 0:
            self.hintLabel.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            for i, trans in enumerate(result):
                label = self.create_label(area=self.outScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">From:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_4.insertWidget(i, label)
                self.income_labels.append(label)

        sql = "SELECT T.from_account,\
                            T.currency_type,\
                            T.amount,\
                            T.transaction_time,\
                            U.name\
                            FROM Transaction T,\
                            User U\
                            WHERE T.from_user = '%s'\
                            AND T.to_user = U.user_id\
                            ORDER BY T.transaction_time DESC;" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        for label in self.expenditure_labels:
            self.verticalLayout_5.removeWidget(label)
        self.expenditure_labels = []
        if len(result) == 0:
            self.hintLabel_2.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            for i, trans in enumerate(result):
                label = self.create_label(area=self.inScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">To:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_5.insertWidget(i, label)
                self.expenditure_labels.append(label)

    def search_income(self):
        self.hintLabel.setText('')
        from_date = self.fromDate.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        to_date = self.toDate.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        from_amount = int(self.fromAmount.text().zfill(1))
        to_amount = int(self.toAmount.text().zfill(1))

        sql = "SELECT T.to_account,\
            T.currency_type,\
            T.amount,\
            T.transaction_time,\
            U.name\
            FROM Transaction T,\
            User U\
            WHERE T.to_user = '%s'\
            AND T.from_user = U.user_id\
            AND T.amount >= %s\
            AND T.amount <= %s\
            AND T.transaction_time >= '%s'\
            AND T.transaction_time <= '%s'\
            ORDER BY T.transaction_time DESC;" % (self.user_id, from_amount, to_amount, from_date, to_date)
        cursor.execute(sql)
        result = cursor.fetchall()

        for label in self.income_labels:
            self.verticalLayout_4.removeWidget(label)
        self.income_labels = []
        if len(result) == 0:
            self.hintLabel.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            for i, trans in enumerate(result):
                label = self.create_label(area=self.outScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">From:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_4.insertWidget(i, label)
                self.income_labels.append(label)

    def search_expenditure(self):
        self.hintLabel_2.setText('')
        from_date = self.fromDate_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        to_date = self.toDate_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        from_amount = int(self.fromAmount_2.text().zfill(1))
        to_amount = int(self.toAmount_2.text().zfill(1))

        sql = "SELECT T.from_account,\
                    T.currency_type,\
                    T.amount,\
                    T.transaction_time,\
                    U.name\
                    FROM Transaction T,\
                    User U\
                    WHERE T.from_user = '%s'\
                    AND T.to_user = U.user_id\
                    AND T.amount >= %s\
                    AND T.amount <= %s\
                    AND T.transaction_time >= '%s'\
                    AND T.transaction_time <= '%s'\
                    ORDER BY T.transaction_time DESC;" % (self.user_id, from_amount, to_amount, from_date, to_date)
        cursor.execute(sql)
        result = cursor.fetchall()

        for label in self.expenditure_labels:
            self.verticalLayout_5.removeWidget(label)
        self.expenditure_labels = []
        if len(result) == 0:
            self.hintLabel_2.setText(
                '<html><head/><body><p><span style=" font-weight:600; color:#003780;">No record!</span></p></body></html>')
        else:
            for i, trans in enumerate(result):
                label = self.create_label(area=self.inScrollArea, height=40)
                if trans[0] == 1:
                    account = 'HKD'
                elif trans[0] == 2:
                    account = 'Deposit'
                elif trans[0] == 3:
                    account = 'USD'
                else:
                    account = 'CNY'
                label.setText(
                    f'<html><head/><body><p><span style=" font-weight:600;">Account:</span> {account}&nbsp;&nbsp;&nbsp'
                    f';&nbsp;<span style=" font-weight:600;">Amount:</span> {trans[1]} '
                    f'{trans[2]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Time:</span> '
                    f'{trans[3]}&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">To:</span> '
                    f'{trans[4]}</p></body></html>')
                self.verticalLayout_5.insertWidget(i, label)
                self.expenditure_labels.append(label)

    def create_label(self, area, height):
        new_label = QtWidgets.QLabel(area)
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


class LoanWindow(StackedWindow):
    def __init__(self, user_id):
        super(LoanWindow, self).__init__()
        loadUi('loanHome.ui', self)
        self.user_id = user_id
        self.slot_init()

    def slot_init(self):
        self.applyButton.clicked.connect(lambda: switch_to(APPLY_LOAN))
        self.payButton.clicked.connect(lambda: switch_to(PAY_LOAN))
        self.backButton.clicked.connect(lambda: switch_to(HOME))


class ApplyLoanWindow(StackedWindow):
    def __init__(self, user_id):
        super(ApplyLoanWindow, self).__init__()
        loadUi('loanApplication.ui', self)
        self.amount.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]*")))
        self.user_id = user_id
        self.credit_level = 0
        self.loan_amount = 0
        self.used_amount = 0
        self.usable_amount = 0
        self.slot_init()

    def slot_init(self):
        self.backButton.clicked.connect(lambda: switch_to(LOAN))
        self.applyButton.clicked.connect(self.apply_loan)
        self.clearButton.clicked.connect(self.clear)

    def activate(self):
        self.hintLabel.setText('')
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.set_content()

    def apply_loan(self):
        amount = int(self.amount.text().zfill(1))
        pay_date = self.dateEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        current_date = QtCore.QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')

        sql = "SELECT credit_level FROM User WHERE user_id='%s';" % self.user_id
        cursor.execute(sql)
        self.credit_level = int(cursor.fetchall()[0][0])

        sql = "SELECT loan_amount FROM CreditLevels WHERE credit_level='%s';" % self.credit_level
        cursor.execute(sql)
        self.loan_amount = int(cursor.fetchall()[0][0])

        sql = "SELECT SUM(loan_amount) FROM Loan WHERE user_id='%s' AND is_settled=0 GROUP BY user_id;" % self.user_id
        cursor.execute(sql)
        self.used_amount = int(cursor.fetchall()[0][0])
        self.usable_amount = self.loan_amount - self.used_amount

        if amount > self.usable_amount:
            self.hintLabel.setText(f'<html><head><body><p><span style="font-size:16pt; color:#003780;">Failed: EXCEED! (Remaining amount: {self.usable_amount})</span></p></body></html>')
            self.clear_amount()
            if pay_date < current_date:
                self.clear_date()
            return

        if pay_date < current_date:
            self.hintLabel.setText('<html><head/><body><p><span style="font-size:16pt; color:#003780;"> Failed: Incorrect due date.</span></p></body></html>')
            self.clear_date()
            return

        sql = "SELECT MAX(loan_id) FROM Loan WHERE user_id='%s' GROUP BY user_id;" % self.user_id
        cursor.execute(sql)
        max_loan_id = cursor.fetchall()[0][0]

        sql = "INSERT INTO Loan VALUES (%s, %s, %s, %s, %s, 0, NULL);"
        val = (self.user_id, max_loan_id + 1, amount, current_date, pay_date)
        cursor.execute(sql, val)
        conn.commit()

        sql = "UPDATE account SET balance=balance+'%s' WHERE user_id='%s' AND account_id=1;"
        val = (amount, self.user_id)
        cursor.execute(sql, val)
        conn.commit()

        sql = "SELECT MAX(transaction_id) FROM Transaction"
        cursor.execute(sql)
        max_trans_id = cursor.fetchall()[0][0]

        sql = "INSERT INTO Transaction VALUES (%s, -1, %s, 1, 1, 'HKD', %s, %s)"
        val = (max_trans_id + 1, self.user_id, amount, current_date)
        cursor.execute(sql, val)
        conn.commit()
        self.set_content()

        self.hintLabel.setText(
            '<html><head/><body><p><span style="font-size:16pt; color:#003780;"> Successful!</span></p></body></html>')
        self.clear_date()
        self.clear_amount()

    def set_content(self):
        sql = "SELECT credit_level FROM User WHERE user_id='%s';" % self.user_id
        cursor.execute(sql)
        self.credit_level = int(cursor.fetchall()[0][0])

        sql = "SELECT loan_amount FROM CreditLevels WHERE credit_level='%s';" % self.credit_level
        cursor.execute(sql)
        self.loan_amount = int(cursor.fetchall()[0][0])

        sql = "SELECT SUM(loan_amount) FROM Loan WHERE user_id='%s' AND is_settled=0 GROUP BY user_id;" % self.user_id
        cursor.execute(sql)
        used_amount = int(cursor.fetchall()[0][0])
        self.usable_amount = self.loan_amount - used_amount
        self.infoLabel.setText(
            f'<html><head/><body><p><span style="font-size:16pt; color:#B0C4DE;">Your credit level: {self.credit_level}&nbsp;&nbsp;&nbsp;&nbsp;Total loan amount: {self.loan_amount}&nbsp;&nbsp;&nbsp;&nbsp;Used: {used_amount}  </span></p></body></html>')

    def clear_amount(self):
        self.amount.setText('')

    def clear_date(self):
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    def clear(self):
        self.clear_amount()
        self.clear_date()
        self.hintLabel.setText("")


class PayLoanWindow(StackedWindow):
    def __init__(self, user_id):
        super(PayLoanWindow, self).__init__()
        loadUi('loanPayBack.ui', self)
        self.idEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]*")))
        self.user_id = user_id
        self.loan_id = 0
        self.loan_amount = 0
        self.balance = 0
        self.credit_level = 0
        self.loan_amount = 0
        self.usable_amount = 0
        self.loans = None
        self.loan_labels = []
        self.slot_init()

    def slot_init(self):
        self.backButton.clicked.connect(lambda: switch_to(LOAN))
        self.payButton.clicked.connect(self.pay)
        self.clearButton.clicked.connect(self.clear)

    def activate(self):
        self.hintLabel.setText('')
        self.clear()
        self.get_data()
        self.set_content()

    def create_label(self, height):
        new_label = QtWidgets.QLabel(self.loanScrollAreaWidget)
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
        sql = "SELECT loan_id, loan_amount, due_date FROM Loan WHERE user_id='%s' AND is_settled=0 ORDER BY due_date ASC" % self.user_id
        cursor.execute(sql)
        self.loans = cursor.fetchall()

    def set_content(self):
        for label in self.loan_labels:
            self.verticalLayout_4.removeWidget(label)
        self.loan_labels = []

        for i, loan in enumerate(self.loans):
            label = self.create_label(height=70)
            label.setText(
                f'<html><head/><body><p><span style=" font-weight:600;">Loan ID:</span> {loan[0]}<br><span style=" font-weight:600;">Amount:</span> HKD {loan[1]} &nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-weight:600;">Due Date:</span> {loan[2]}</p></body></html>')
            self.verticalLayout_4.insertWidget(i, label)
            self.loan_labels.append(label)

    def pay(self):
        current_date = QtCore.QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.loan_id = int(self.idEdit.text().zfill(1))

        is_valid = False
        for loan in self.loans:
            if self.loan_id == loan[0]:
                is_valid = True

        if not is_valid:
            self.hintLabel.setText(
                '<html><head/><body><p><span style="font-size:16pt; color:#003780;">Failed: Incorrect loan id.</span></p></body></html>')
            return

        sql = "SELECT loan_amount from Loan WHERE user_id='%s' AND loan_id='%s'" % (self.user_id, self.loan_id)
        cursor.execute(sql)
        self.loan_amount = int(cursor.fetchall()[0][0])

        sql = "SELECT balance from Account WHERE user_id='%s' AND account_id=1" % self.user_id
        cursor.execute(sql)
        self.balance = int(cursor.fetchall()[0][0])

        if self.loan_amount > self.balance:
            self.hintLabel.setText(
                '<html><head/><body><p><span style="font-size:16pt; color:#003780;">Failed: Insufficient balance.</span></p></body></html>')
            return

        self.hintLabel.setText(
            '<html><head/><body><p><span style="font-size:16pt; color:#003780;">Successful!</span></p></body></html>')
        self.idEdit.setText('')


        sql = "UPDATE Loan SET is_settled=1 WHERE user_id='%s' AND loan_id='%s';"
        val = (self.user_id, self.loan_id)
        cursor.execute(sql, val)
        conn.commit()

        sql = "UPDATE Loan SET settled_date=%s WHERE user_id='%s' AND loan_id='%s';"
        val = (current_date, self.user_id, self.loan_id)
        cursor.execute(sql, val)
        conn.commit()

        sql = "UPDATE account SET balance=balance-'%s' WHERE user_id='%s' AND account_id=1;"
        val = (self.loan_amount, self.user_id)
        cursor.execute(sql, val)
        conn.commit()

        sql = "SELECT MAX(transaction_id) FROM Transaction"
        cursor.execute(sql)
        max_trans_id = cursor.fetchall()[0][0]

        sql = "INSERT INTO Transaction VALUES (%s, %s, -1, 1, 1, 'HKD', %s, %s)"
        val = (max_trans_id + 1, self.user_id, self.loan_amount, current_date)
        cursor.execute(sql, val)
        conn.commit()

        self.get_data()
        self.set_content()

    def clear(self):
        self.hintLabel.setText('')
        self.idEdit.setText('')


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
