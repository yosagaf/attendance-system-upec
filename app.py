"""
Module implementing MainWindow.
"""

from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from reco import Ui_MainWindow

from read_video import VideoThread


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

    def OpenVideo(self):
        if not self.Video.isRunning():
            self.Video.start()
            self.startBtn.setText('Close video')
        else:
            self.Video.Stop_Video()
            self.startBtn.setText('Open Video')
            #self.Camer_label.setPixmap(QPixmap.fromImage())  #Définir la restauration d'image
    
    def Fresh_Camera(self, show_pic):
        self.displayFrameLabel.setScaledContents(True) 
        self.displayFrameLabel.setPixmap(QPixmap.fromImage(show_pic))

    
    @pyqtSlot()
    def on_start_pushButton_clicked(self):
        self.OpenVideo()
        self.Video.CameraFram.connect(self.Fresh_Camera)
        self.Video.OpenVideoFlage.connect(self.Un_Open)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        