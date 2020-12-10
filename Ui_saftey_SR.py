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
        MainWindow.resize(1156, 785)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(650, 180, 291, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_pushbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.start_pushbutton.setFont(font)
        self.start_pushbutton.setObjectName("start_pushbutton")
        self.horizontalLayout.addWidget(self.start_pushbutton)
        self.stop_pushbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.stop_pushbutton.setFont(font)
        self.stop_pushbutton.setObjectName("stop_pushbutton")
        self.horizontalLayout.addWidget(self.stop_pushbutton)
        self.quit_pushbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(12)
        self.quit_pushbutton.setFont(font)
        self.quit_pushbutton.setObjectName("quit_pushbutton")
        self.horizontalLayout.addWidget(self.quit_pushbutton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 40, 481, 34))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.display_video_frame = QtWidgets.QFrame(self.centralWidget)
        self.display_video_frame.setGeometry(QtCore.QRect(450, 240, 671, 431))
        self.display_video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display_video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display_video_frame.setObjectName("display_video_frame")
        self.display_video_label = QtWidgets.QLabel(self.display_video_frame)
        self.display_video_label.setGeometry(QtCore.QRect(10, 10, 651, 411))
        self.display_video_label.setText("")
        self.display_video_label.setObjectName("display_video_label")
        self.display_statistics_frame = QtWidgets.QFrame(self.centralWidget)
        self.display_statistics_frame.setGeometry(QtCore.QRect(20, 240, 391, 431))
        self.display_statistics_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display_statistics_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display_statistics_frame.setObjectName("display_statistics_frame")
        self.display_statistics_label = QtWidgets.QLabel(self.display_statistics_frame)
        self.display_statistics_label.setGeometry(QtCore.QRect(10, 10, 371, 411))
        self.display_statistics_label.setText("")
        self.display_statistics_label.setObjectName("display_statistics_label")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_pushbutton.setText(_translate("MainWindow", "START"))
        self.stop_pushbutton.setText(_translate("MainWindow", "STOP"))
        self.quit_pushbutton.setText(_translate("MainWindow", "QUIT"))
        self.label.setText(_translate("MainWindow", "ATTENDANCE MANAGEMENT SYSTEM"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
