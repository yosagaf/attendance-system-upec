# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_widgetui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(721, 493)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(590, 430, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 671, 381))
        self.tableView.setObjectName("tableView")
        self.pushButton.clicked.connect(self.load_data)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "LOAD DATA"))

    def load_data(self):
        infos_students = []
        with open('attendance.csv') as ff:
            reader = csv.reader(ff)
            line = next(reader)
            for line in reader:
                infos_students.append(line) 
        print(infos_students)

        for row_number, row_data in enumerate(infos_students):
            for column_number, data in enumerate( row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QtWidgetItem(str(data)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
