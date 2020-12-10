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
from Read_videoST import VideoThreadST

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
        self.VideoST = VideoThreadST()
        
        
        if not self.Video.isRunning():
            self.Video.start()
            self.Video.CameraFram.connect(self.Fresh_Camera)
            self.Video.OpenVideoFlage.connect(self.Un_Open)
        else:
            self.cap.release()
        
    def OpenVideo(self):
        
        if not self.Video.isRunning():
            self.Video.start()
            #self.start_pushbutton.setText('STOP')
        else:
            self.Video.Stop_Video()
            #self.start_pushbutton.setText('START')
            #self.display_video_label.setPixmap(QPixmap.fromImage())  #Définir la restauration d'image


    def OpenVideoST(self):
        
        if not self.VideoST.isRunning():
            self.VideoST.start()
        else:
           self.VideoST.Stop_Video()

    def Fresh_Camera(self, show_pic):
        self.display_video_label.setScaledContents(True) # Picture adaptive size
        self.display_video_label.setPixmap(QPixmap.fromImage(show_pic))
    
    def Un_Open(self):
        QtWidgets.QMessageBox.warning(self, 'Warning', 'Failed to open video')
        
    
    @pyqtSlot()
    def on_start_pushbutton_clicked(self):
        self.Video.Stop_Video()
        self.OpenVideoST()
        self.VideoST.CameraFram.connect(self.Fresh_Camera)
        #self.VideoST.OpenVideoFlage.connect(self.Un_Open)
    
    
    @pyqtSlot()
    def on_quit_pushbutton_clicked(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
