# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1319, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, -60, 1351, 891))
        self.groupBox.setObjectName("groupBox")
        self.displayResultGoupBox = QtWidgets.QGroupBox(self.groupBox)
        self.displayResultGoupBox.setGeometry(QtCore.QRect(50, 320, 421, 561))
        self.displayResultGoupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayResultGoupBox.setObjectName("displayResultGoupBox")
        self.displayResultLabel = QtWidgets.QLabel(self.displayResultGoupBox)
        self.displayResultLabel.setGeometry(QtCore.QRect(10, 30, 401, 511))
        self.displayResultLabel.setText("")
        self.displayResultLabel.setObjectName("displayResultLabel")
        self.textLabel = QtWidgets.QLabel(self.groupBox)
        self.textLabel.setGeometry(QtCore.QRect(660, 170, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textLabel.setFont(font)
        self.textLabel.setObjectName("textLabel")
        self.frameGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.frameGroupBox.setGeometry(QtCore.QRect(490, 220, 851, 661))
        self.frameGroupBox.setTitle("")
        self.frameGroupBox.setObjectName("frameGroupBox")
        self.displayFrameLabel = QtWidgets.QLabel(self.frameGroupBox)
        self.displayFrameLabel.setGeometry(QtCore.QRect(10, 20, 841, 641))
        self.displayFrameLabel.setText("")
        self.displayFrameLabel.setObjectName("displayFrameLabel")
        self.startBtn = QtWidgets.QPushButton(self.groupBox)
        self.startBtn.setGeometry(QtCore.QRect(210, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        self.quitBtn = QtWidgets.QPushButton(self.groupBox)
        self.quitBtn.setGeometry(QtCore.QRect(210, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.quitBtn.setFont(font)
        self.quitBtn.setObjectName("quitBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1319, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.displayResultGoupBox.setTitle(_translate("MainWindow", "RESULTS"))
        self.textLabel.setText(_translate("MainWindow", "ATTENDANCE MANAGEMENT SYSTEM"))
        self.startBtn.setText(_translate("MainWindow", "START"))
        self.quitBtn.setText(_translate("MainWindow", "STOP"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
