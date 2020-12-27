from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_saftey_SR import Ui_MainWindow

from Read_video import VideoThread
from face_reco import display_information

class MainWindow(QMainWindow, Ui_MainWindow):
    
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.Video = VideoThread()
                
        #if not self.Video.i(!:,hyuyikkigoh )
        '''
        if not self.Video.isRunning():
            self.Video.start()
            #self.start_pushbutton.setText('STOP')
        else:
            self.Video.Stop_Video()
            #self.start_pushbutton.setText('START')
            #self.display_video_label.setPixmap(QPixmap.fromImage())  #Définir la restauration d'image
        '''
    def OpenVideo(self):
        
        if not self.Video.isRunning():
            self.Video.start()
        else:
           self.Video.Stop_Video()

    def Fresh_Camera(self, show_pic):
        self.display_video_label.setScaledContents(True) # Picture adaptive size
        self.display_video_label.setPixmap(QPixmap.fromImage(show_pic))
    
    def Un_Open(self):
        QtWidgets.QMessageBox.warning(self, 'Warning', 'Failed to open video')

    # les deux slos suivants reçoivent un signal et exécute une routine.    
    @pyqtSlot()
    def on_start_pushbutton_clicked(self):
        #self.Video.Stop_Video()
        self.OpenVideo()

        # Binds signal of CameraFram to the slot self.Fresh_Camera
        self.Video.CameraFram.connect(self.Fresh_Camera)
        self.Video.OpenVideoFlag.connect(self.Un_Open)
        #self.display_statistics_label.setText(display_information())
    
    @pyqtSlot() # decorate a Python method to create a Qt slot.
    def on_quit_pushbutton_clicked(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
