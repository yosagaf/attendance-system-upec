from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from register import Ui_MainWindow1 
import datetime
import csv

from register import *
from read_video_rg import VideoThreadRG
from read_video import VideoThread

class MainWindow(QMainWindow, Ui_MainWindow):
    # This class will have access to all of the properties of QThread and Ui_MainWindow
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.Video = VideoThread()
        self.open_video()
        self.Videorg = VideoThreadRG()
        
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
    
    def registration(self):
        self.hide()
        self.window=QtWidgets.QMainWindow()
        self.ui1=Ui_MainWindow1()
        self.ui1.setup(self.window)
        self.window.show()
        self.cap.release()
        
        #self.Video.stop_video()
        #self.Video.cap.release()

        #self.Videorg = VideoThreadRG()
        #self.open_video_rg()
        #self.Videorg.stop_video_rg()
        
    def fresh_camera(self, show_pic):   
        # Scale the contents of the label to fill all available space
        self.display_video_label.setScaledContents(True)

        # Convert the QImage object to QPixmap and how images in PyQt window
        self.display_video_label.setPixmap(QPixmap.fromImage(show_pic))

    def fresh_camera_rg(self, show_pic):   
        # Scale the contents of the label to fill all available space
        self.register_video_frame.setScaledContents(True)
        
        # Convert the QImage object to QPixmap and how images in PyQt window
        self.register_video_frame.setPixmap(QPixmap.fromImage(show_pic))
    
    # Following slots receive signal and execute routine.    
    @pyqtSlot()
    def on_start_pushbutton_clicked(self):
        # When the start button is pressed, face recognition start (bounding box)
        self.Video.face_reco_flag = True
        self.display_information()
    
    # Following slots receive signal and execute routine.    
    @pyqtSlot()
    def on_stop_pushbutton_clicked(self):
        # When the stop button is pressed, face recognition stop (bounding box)
        self.Video.face_reco_flag = False

    @pyqtSlot() # Decorate a Python method to create a Qt slot.
    def on_quit_pushbutton_clicked(self):
        #self.close()
        #self.close_event()
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit the application ?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass

    @pyqtSlot() # Decorate a Python method to create a Qt slot.
    def on_registration_pushbutton_clicked(self):
        self.registration()

    
    @pyqtSlot() # Decorate a Python method to create a Qt slot.
    def on_finish_pushbutton_clicked(self):
        #self.close()
        print("Bonjour")

    # Set an display the time in the corresponding label
    @pyqtSlot()
    def show_date_time(self): 
        time = QTime.currentTime()
        time_text = time.toString("HH:mm" if time.second() % 2 == 0 else "HH:mm")
        self.time_label.setText(time_text)
        
        date = QDate.currentDate()
        date_text = date.toString("MM/dd/yyyy")
        self.date_label.setText(date_text)
    
    def display_information(self):
        infos_students = []

        with open('attendance.csv') as ff:
            reader = csv.reader(ff)
            line = next(reader)
            for line in reader:
                infos_students.append(line)
                infos_students = line  
            info = infos_students
            print(info)
            
        #self.display_statistics_label.setText(str(info[0])+"  " + str(info[1])+"  "+ str(info[2]))
        
if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setWindowTitle("ATTENDANCE MANAGEMENT SYSTEM")
    ui.show()
    
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting the application")
    
