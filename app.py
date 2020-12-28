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
        
        if not self.Video.isRunning():
            self.Video.start()
            # connect the "camera_frame" signal to a slot 
            self.Video.camera_frame.connect(self.fresh_camera)
        else:
            self.cap.release()

    def open_video(self):
        
        if not self.Video.isRunning():
            self.Video.start()
        else:
           self.Video.stop_video()

    def fresh_camera(self, show_pic):
        
        # Scale the contents of the label to fill all available space
        self.display_video_label.setScaledContents(True)

        # Convert the QImage object to QPixmap and how images in PyQt window
        self.display_video_label.setPixmap(QPixmap.fromImage(show_pic))
    
    def un_open(self):
        QtWidgets.QMessageBox.warning(self, 'Warning', 'Failed to open video')

    # Following slots receive signal and execute routine.    
    
    @pyqtSlot()
    def on_start_pushbutton_clicked(self):
        #self.Video.stop_video()
        #self.open_video()
        print("Done")

        # Binds signal of camera_frame to the slot self.fresh_camera
        #self.Video.camera_frame.connect(self.fresh_camera)
        self.Video.open_video_flag.connect(self.un_open)
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
    
