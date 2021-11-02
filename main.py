import pickle
import sys
import time

import cv2
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PyQt5.uic import loadUi

WIDTH = 1200
HEIGHT = 800

CONF = 50

WELCOME = 0
FACE = 1
HOME = 2


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
        self.leaveButton.clicked.connect(lambda: exit(0))

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
        self.slot_init()
        self.get_data()
        self.set_content()

    def slot_init(self):
        self.logoutButton.clicked.connect(lambda: switch_to(WELCOME))

    def get_data(self):
        pass

    def set_content(self):
        self.homeTitleLabel.setText(
            f'<html><head/><body><p><span style=" color:#003780;">Welcome back, {self.user_id}!</span></p></body></html>')

    def activate(self):
        self.get_data()
        self.set_content()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    winList = [WelcomeWindow(), FaceWindow(), None]

    mainWin = QStackedWidget()
    mainWin.setFixedWidth(WIDTH)
    mainWin.setFixedHeight(HEIGHT)
    mainWin.setWindowTitle('iKYC')
    mainWin.setWindowIcon(QtGui.QIcon('resources/small_logo.png'))
    mainWin.addWidget(winList[WELCOME])

    mainWin.show()
    sys.exit(app.exec_())
