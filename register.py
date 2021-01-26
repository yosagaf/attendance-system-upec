# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 709)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.register_video_frame = QtWidgets.QFrame(self.centralWidget)
        self.register_video_frame.setGeometry(QtCore.QRect(290, 160, 671, 431))
        self.register_video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_video_frame.setObjectName("register_video_frame")
        self.register_video_label = QtWidgets.QLabel(self.register_video_frame)
        self.register_video_label.setGeometry(QtCore.QRect(10, 10, 651, 411))
        self.register_video_label.setText("")
        self.register_video_label.setObjectName("register_video_label")
        self.logo_label = QtWidgets.QLabel(self.centralWidget)
        self.logo_label.setGeometry(QtCore.QRect(710, 20, 241, 101))
        self.logo_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(410, 610, 411, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_pushbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.register_pushbutton.setObjectName("register_pushbutton")
        self.horizontalLayout.addWidget(self.register_pushbutton)
        self.finish_pushbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.finish_pushbutton.setObjectName("finish_pushbutton")
        self.horizontalLayout.addWidget(self.finish_pushbutton)
        self.students_infos_groupbox = QtWidgets.QGroupBox(self.centralWidget)
        self.students_infos_groupbox.setGeometry(QtCore.QRect(10, 140, 261, 451))
        self.students_infos_groupbox.setTitle("")
        self.students_infos_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self.students_infos_groupbox.setObjectName("students_infos_groupbox")
        self.instructions_group_box = QtWidgets.QGroupBox(self.students_infos_groupbox)
        self.instructions_group_box.setGeometry(QtCore.QRect(10, 40, 241, 81))
        self.instructions_group_box.setObjectName("instructions_group_box")
        self.instructions_text_browser = QtWidgets.QTextBrowser(self.instructions_group_box)
        self.instructions_text_browser.setGeometry(QtCore.QRect(0, 20, 241, 61))
        self.instructions_text_browser.setObjectName("instructions_text_browser")
        self.student_detauls_group_box_2 = QtWidgets.QGroupBox(self.students_infos_groupbox)
        self.student_detauls_group_box_2.setGeometry(QtCore.QRect(10, 180, 241, 141))
        self.student_detauls_group_box_2.setObjectName("student_detauls_group_box_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.student_detauls_group_box_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 241, 120))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.si_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.si_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.si_grid_layout.setObjectName("si_grid_layout")
        self.last_name_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.last_name_lineEdit.setObjectName("last_name_lineEdit")
        self.si_grid_layout.addWidget(self.last_name_lineEdit, 0, 1, 1, 1)
        self.last_name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.last_name_label.setObjectName("last_name_label")
        self.si_grid_layout.addWidget(self.last_name_label, 0, 0, 1, 1)
        self.fisrt_name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fisrt_name_label.setObjectName("fisrt_name_label")
        self.si_grid_layout.addWidget(self.fisrt_name_label, 2, 0, 1, 1)
        self.first_name_line_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.first_name_line_edit.setObjectName("first_name_line_edit")
        self.si_grid_layout.addWidget(self.first_name_line_edit, 2, 1, 1, 1)
        self.identifier_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.identifier_label.setObjectName("identifier_label")
        self.si_grid_layout.addWidget(self.identifier_label, 4, 0, 1, 1)
        self.identifier_line_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.identifier_line_edit.setObjectName("identifier_line_edit")
        self.si_grid_layout.addWidget(self.identifier_line_edit, 4, 1, 1, 1)
        self.age_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.age_label.setObjectName("age_label")
        self.si_grid_layout.addWidget(self.age_label, 5, 0, 1, 1)
        self.age_line_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.age_line_edit.setObjectName("age_line_edit")
        self.si_grid_layout.addWidget(self.age_line_edit, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.register_pushbutton.setText(_translate("MainWindow", "REGISTER"))
        self.finish_pushbutton.setText(_translate("MainWindow", "FINISH"))
        self.instructions_group_box.setTitle(_translate("MainWindow", "Instructions :"))
        self.instructions_text_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please submit students informations befor the image data collections.</p></body></html>"))
        self.student_detauls_group_box_2.setTitle(_translate("MainWindow", "Students details"))
        self.last_name_label.setText(_translate("MainWindow", " Last name"))
        self.fisrt_name_label.setText(_translate("MainWindow", " First name"))
        self.identifier_label.setText(_translate("MainWindow", " Identifier"))
        self.age_label.setText(_translate("MainWindow", " Age"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
