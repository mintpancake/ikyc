import sys
import time

import cv2
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PyQt5.uic import loadUi

WIDTH = 1200
HEIGHT = 800

WELCOME = 0
FACE = 1
HOME = 2


def switch_to(idx):
    if mainWin.currentIndex() == FACE:
        faceWin.stop()
    if idx == FACE:
        faceWin.start()

    mainWin.setCurrentIndex(idx)


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        loadUi("welcome.ui", self)
        self.slot_init()
        self.set_greeting(time.localtime())

    def slot_init(self):
        self.loginButton.clicked.connect(lambda: switch_to(FACE))
        self.leaveButton.clicked.connect(lambda: exit(0))

    def set_greeting(self, time):
        if time.tm_hour < 6:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Night!</span></p></body></html>")
        elif time.tm_hour < 12:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Morning!</span></p></body></html>")
        elif time.tm_hour < 18:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Afternoon!</span></p></body></html>")
        else:
            self.greetingLabel.setText(
                "<html><head/><body><p><span style=\" color:#003780;\">Good Evening!</span></p></body></html>")


class FaceWindow(QMainWindow):
    def __init__(self):
        super(FaceWindow, self).__init__()
        loadUi("face.ui", self)

        self.timer = QtCore.QTimer()
        self.CAM_NUM = 0
        self.cam = cv2.VideoCapture()

        self.image = None

        self.slot_init()

    def slot_init(self):
        self.timer.timeout.connect(self.display)
        self.backButton.clicked.connect(lambda: switch_to(WELCOME))
        self.verifyButton.clicked.connect(self.verify)

    def start(self):
        self.cam.open(self.CAM_NUM, cv2.CAP_DSHOW)
        self.timer.start(30)

    def stop(self):
        self.timer.stop()
        self.cam.release()

    def display(self):
        flag, self.image = self.cam.read()
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

    def verify(self):
        self.stop()
        user_id = -1
        # TODO: use self.image to get user_id
        user_id = -1
        if user_id != -1:
            homeWin = HomeWindow(user_id)
            mainWin.addWidget(homeWin)
            switch_to(HOME)
        else:
            self.hintLabel.setText(
                '<html><head/><body><p align="center"><span style=" font-weight:600; color:#646464;">Unrecognized</span><span style=" font-weight:600; color:#646464;"><br/></span><span style=" color:#646464;">Please adjust your posture and try again</span></p></body></html>'
            )
            self.start()


class HomeWindow(QMainWindow):
    def __init__(self, user_id):
        super(HomeWindow, self).__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    welcomeWin = WelcomeWindow()
    faceWin = FaceWindow()

    mainWin = QStackedWidget()

    mainWin.setFixedWidth(WIDTH)
    mainWin.setFixedHeight(HEIGHT)
    mainWin.setWindowTitle('iKYC')
    mainWin.setWindowIcon(QtGui.QIcon('resources/small_logo.png'))

    mainWin.addWidget(welcomeWin)
    mainWin.addWidget(faceWin)

    mainWin.show()
    sys.exit(app.exec_())
