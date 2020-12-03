# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_saftey_SR import Ui_MainWindow

from Read_video import VideoThread

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.Video = VideoThread()
        
        if not self.Video.isRunning():
            self.Video.start()
            self.Video.CameraFram.connect(self.Fresh_Camera)
            self.Video.OpenVideoFlage.connect(self.Un_Open)
    
    def OpenVideo(self):
        
        if self.Video.isRunning():
            self.Video.start()
            self.Run_Camera = 1
            print("Reco d'actions")
            #self.Bic_pushButton.setText('Close video')
        
        #else:
            #self.Video.Stop_Video()
            #self.Bic_pushButton.setText('Open Video')
            #self.Camer_label.setPixmap(QPixmap.fromImage())  #Définir la restauration d'image
    
    def Fresh_Camera(self, show_pic):
        self.Bic_label.setScaledContents(True) # Picture adaptive size
        self.Bic_label.setPixmap(QPixmap.fromImage(show_pic))
    
    def Un_Open(self):
        QtWidgets.QMessageBox.warning(self, '警告',  'Failed to open video')
        
    
    @pyqtSlot()
    def on_Bic_pushButton_clicked(self):
        self.OpenVideo()
        self.Video.CameraFram.connect(self.Fresh_Camera)
        self.Video.OpenVideoFlage.connect(self.Un_Open)
    
    
    @pyqtSlot()
    def on_SR_pushButton_clicked(self):
        self.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
