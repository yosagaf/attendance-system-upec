from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
import datetime

from read_video import VideoThread
from knn_classifier import display_information

class MainWindow(QMainWindow, Ui_MainWindow):
    # This class will have access to all of the properties of QThread and Ui_MainWindow
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.Video = VideoThread()
        self.open_video()
        
        # Using QTimer to update the time in the GUI
        timer = QTimer(self, interval=1000, timeout=self.show_date_time)
        timer.start()
        self.show_date_time()
       
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

    # set an display the time in the corresponding label
    @pyqtSlot()
    def show_date_time(self): 
        time = QTime.currentTime()
        time_text = time.toString("HH:mm" if time.second() % 2 == 0 else "HH:mm")
        self.time_label.setText(time_text)
        
        date = QDate.currentDate()
        date_text = date.toString("MM/dd/yyyy")
        self.date_label.setText(date_text)
        
        
if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setWindowTitle("ATTENDANCE MANAGEMENT SYSTEM")
    ui.show()
    
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
    
