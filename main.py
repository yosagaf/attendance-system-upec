# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1204, 851)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, -10, 1181, 851))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.logoLabel = QtWidgets.QLabel(self.groupBox)
        self.logoLabel.setGeometry(QtCore.QRect(20, 30, 151, 91))
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.videoGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.videoGroupBox.setGeometry(QtCore.QRect(370, 130, 791, 711))
        self.videoGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.videoGroupBox.setObjectName("videoGroupBox")
        self.videoLabel = QtWidgets.QLabel(self.videoGroupBox)
        self.videoLabel.setGeometry(QtCore.QRect(0, 20, 801, 641))
        self.videoLabel.setText("")
        self.videoLabel.setObjectName("videoLabel")
        self.startBtn = QtWidgets.QPushButton(self.groupBox)
        self.startBtn.setGeometry(QtCore.QRect(140, 170, 89, 25))
        self.startBtn.setObjectName("startBtn")
        self.processBtn = QtWidgets.QPushButton(self.groupBox)
        self.processBtn.setGeometry(QtCore.QRect(140, 210, 89, 25))
        self.processBtn.setObjectName("processBtn")
        self.labelTheme = QtWidgets.QLabel(self.groupBox)
        self.labelTheme.setGeometry(QtCore.QRect(470, 50, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelTheme.setFont(font)
        self.labelTheme.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelTheme.setObjectName("labelTheme")
        self.resultGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.resultGroupBox.setGeometry(QtCore.QRect(20, 300, 331, 541))
        self.resultGroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.resultGroupBox.setObjectName("resultGroupBox")
        self.resultLabel = QtWidgets.QLabel(self.resultGroupBox)
        self.resultLabel.setGeometry(QtCore.QRect(0, 20, 331, 521))
        self.resultLabel.setText("")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.logLabel = QtWidgets.QLabel(self.groupBox)
        self.logLabel.setGeometry(QtCore.QRect(10, 20, 281, 111))
        self.logLabel.setText("")
        self.logLabel.setTextFormat(QtCore.Qt.RichText)
        self.logLabel.setPixmap(QtGui.QPixmap("../../Pictures/upec.png"))
        self.logLabel.setObjectName("logLabel")
        self.quitBtn = QtWidgets.QPushButton(self.groupBox)
        self.quitBtn.setGeometry(QtCore.QRect(140, 250, 89, 25))
        self.quitBtn.setObjectName("quitBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.videoGroupBox.setTitle(_translate("Dialog", "DISPLAY"))
        self.startBtn.setText(_translate("Dialog", "START"))
        self.processBtn.setText(_translate("Dialog", "PROCESS"))
        self.labelTheme.setText(_translate("Dialog", "FACE RECOGNITION FOR ATTENDANCE MANAGEMENT"))
        self.resultGroupBox.setTitle(_translate("Dialog", "RESULTS"))
        self.quitBtn.setText(_translate("Dialog", "QUIT"))

    def quit(self):
        sys.exit()

    def Display(self, frame, label):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frameb = QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
        pix = QPixmap.fromImage(frameb)
        resized = pix.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
        label.setPixmap(resized)

    def capturing(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, self.frame = self.cap.read()
            if ret == True:
                self.Display(self.frame, self.ui.label_Frame)
                cv2.waitKey(1)
            else:
                break

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
