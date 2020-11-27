# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
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
        self.groupBox.setGeometry(QtCore.QRect(-40, -100, 1351, 891))
        self.groupBox.setObjectName("groupBox")
        self.startPushButton = QtWidgets.QPushButton(self.groupBox)
        self.startPushButton.setGeometry(QtCore.QRect(180, 250, 111, 31))
        self.startPushButton.setObjectName("startPushButton")
        self.stopPushButton = QtWidgets.QPushButton(self.groupBox)
        self.stopPushButton.setGeometry(QtCore.QRect(180, 290, 111, 31))
        self.stopPushButton.setObjectName("stopPushButton")
        self.displayFrameGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.displayFrameGroupBox.setGeometry(QtCore.QRect(490, 200, 851, 681))
        self.displayFrameGroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayFrameGroupBox.setTitle("")
        self.displayFrameGroupBox.setObjectName("displayFrameGroupBox")
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
        self.startPushButton.setText(_translate("MainWindow", "START"))
        self.stopPushButton.setText(_translate("MainWindow", "STOP"))
        self.displayResultGoupBox.setTitle(_translate("MainWindow", "RESULTS"))
        self.textLabel.setText(_translate("MainWindow", "ATTENDANCE MANAGEMENT SYSTEM"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
