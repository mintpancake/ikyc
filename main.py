import pickle
import sys
import time

import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
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
ACCOUNT_DETAIL = 7


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

        # TODO: for debug
        self.user_id = 1

        if self.user_id == -1:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                id_, conf = self.recognizer.predict(roi_gray)
                if conf >= CONF:
                    self.user_id = self.labels[id_]

    def verify(self):
        self.stop()
        if self.user_id != -1:
            winList[HOME] = HomeWindow(self.user_id)
            switch_to(HOME)
        else:
            self.hintLabel.setText(
                '<html><head/><body><p align="center"><span style=" font-weight:600; color:#646464;">Unrecognized</span><span style=" font-weight:600; color:#646464;"><br/></span><span style=" color:#646464;">Please adjust your posture and try again</span></p></body></html>'
            )
            self.start()


class HomeWindow(StackedWindow):
    def __init__(self, user_id):
        super(HomeWindow, self).__init__()
        loadUi('home.ui', self)
        self.user_id = user_id
        self.name = ''
        self.last_login_time = ''
        self.login_history = []
        self.login_history_labels = []
        self.slot_init()
        # TODO: for debug
        # self.update_login_time()

    def slot_init(self):
        self.logoutButton.clicked.connect(lambda: switch_to(WELCOME))

    def create_label(self):
        new_label = QtWidgets.QLabel(self.historyScrollAreaWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(new_label.sizePolicy().hasHeightForWidth())
        new_label.setSizePolicy(sizePolicy)
        new_label.setMinimumSize(QtCore.QSize(0, 40))
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

        sql = "SELECT login_time FROM Login WHERE user_id='%s' ORDER BY login_time DESC" % self.user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        self.last_login_time = result[1][0]
        self.login_history = result

    def set_content(self):
        self.homeTitleLabel.setText(
            f'<html><head/><body><p><span style=" color:#003780;">Welcome back, {self.name}!</span></p></body></html>')
        self.lastLoginTimeLabel.setText(
            f'<html><head/><body><p><span style=" font-size:12pt; color:#646464;">Last login time:<br/>{self.last_login_time}</span></p></body></html>')
        for i, history in enumerate(self.login_history):
            label = self.create_label()
            label.setText(f'<html><head/><body><p>{history[0]}</p></body></html>')
            self.verticalLayout_4.insertWidget(i, label)
            self.login_history_labels.append(label)

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
        now_str = f'{year}-{mon}-{mday}-{hour}-{min}-{sec}'
        sql = "INSERT INTO Login VALUES (%s, %s)"
        val = (self.user_id, now_str)
        cursor.execute(sql, val)
        conn.commit()


if __name__ == "__main__":
    conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="ikyc")
    cursor = conn.cursor()
    app = QApplication(sys.argv)

    winList = [WelcomeWindow(), FaceWindow(), None, None, None, None, None]

    mainWin = QStackedWidget()
    mainWin.setFixedWidth(WIDTH)
    mainWin.setFixedHeight(HEIGHT)
    mainWin.setWindowTitle('iKYC')
    mainWin.setWindowIcon(QtGui.QIcon('resources/small_logo.png'))
    mainWin.addWidget(winList[WELCOME])

    mainWin.show()
    sys.exit(app.exec_())
