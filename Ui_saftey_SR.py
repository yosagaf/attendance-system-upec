# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saftey_SR.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 785)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SR_label = QtWidgets.QLabel(self.centralWidget)
        self.SR_label.setGeometry(QtCore.QRect(130, 470, 480, 270))
        self.SR_label.setText("")
        self.SR_label.setObjectName("SR_label")
        self.Bic_label = QtWidgets.QLabel(self.centralWidget)
        self.Bic_label.setGeometry(QtCore.QRect(90, 110, 551, 301))
        self.Bic_label.setText("")
        self.Bic_label.setObjectName("Bic_label")
        self.SR_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.SR_pushButton.setGeometry(QtCore.QRect(340, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.SR_pushButton.setFont(font)
        self.SR_pushButton.setObjectName("SR_pushButton")
        self.Bic_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.Bic_pushButton.setGeometry(QtCore.QRect(200, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.Bic_pushButton.setFont(font)
        self.Bic_pushButton.setObjectName("Bic_pushButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SR_pushButton.setText(_translate("MainWindow", "STOP"))
        self.Bic_pushButton.setText(_translate("MainWindow", "START"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
