from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from register import Ui_MainWindow1
import datetime
import csv

from read_video import VideoThread

class MainWindow1(QMainWindow, Ui_MainWindow1):
    # This class will have access to all of the properties of QThread and Ui_MainWindow
    
    def __init__(self, parent=None):
        super(MainWindow1, self).__init__(parent)
        self.setup(self)
    
        self.Video = VideoThread()
        self.open_video()
        
    
    def open_video(self):
        if not self.Video.isRunning():
            self.Video.start()
            self.Video.camera_frame.connect(self.fresh_camera)
        else:
           self.Video.stop_video()
           self.cap.release()

    def fresh_camera(self, show_pic):   
        # Scale the contents of the label to fill all available space
        self.register_video_label.setScaledContents(True)

        # Convert the QImage object to QPixmap and how images in PyQt window
        self.register_video_label.setPixmap(QPixmap.fromImage(show_pic))
    '''
    # Following slots receive signal and execute routine.    
    @pyqtSlot()
    def on_start_pushbutton_clicked(self):
        # When the start button is pressed, face recognition start (bounding box)
        self.Video.face_reco_flag = True
        self.display_information()
    '''

    @pyqtSlot() # Decorate a Python method to create a Qt slot.
    def on_finish_pushbutton_clicked(self):
        self.close()
        
if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui1 = MainWindow1()
    ui1.setWindowTitle("ATTENDANCE MANAGEMENT SYSTEM")
    ui1.show()
    
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting the application")
    
