import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import face_recognition
import cv2

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from face_reco import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Camera.clicked.connect(self.capturing)

    def capturing(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, self.frame = self.cap.read()
            if ret == True:
                self.Display(self.frame, self.ui.label_Frame)
                cv2.waitKey(1)
            else:
                break
    def Display(self, frame, label):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frameb = QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
        pix = QPixmap.fromImage(frameb)
        resized = pix.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
        label.setPixmap(resized)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())