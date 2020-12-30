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
    
    # This class will have access to all of the properties of QThread and Ui_MainWindow
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
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
        self.display_video_label.setScaledContents(True)

        # Convert the QImage object to QPixmap and how images in PyQt window
        self.display_video_label.setPixmap(QPixmap.fromImage(show_pic))
    
    # Following slots receive signal and execute routine.    
    @pyqtSlot()
    def on_start_pushbutton_clicked(self):
        # When the start button is pressed, face recognition start (bounding box)
        self.Video.face_reco_flag = True
    
    # Following slots receive signal and execute routine.    
    @pyqtSlot()
    def on_stop_pushbutton_clicked(self):
        # When the stop button is pressed, face recognition stop (bounding box)
        self.Video.face_reco_flag = False

    @pyqtSlot() # decorate a Python method to create a Qt slot.
    def on_quit_pushbutton_clicked(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
