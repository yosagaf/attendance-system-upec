from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from register import Ui_MainWindow1 
from random import randrange
import datetime
import time
import csv
import os
import cv2
from knn_classifier import train

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
        
        # Using QTimer to update the time in the GUI and students informations
        timer1 = QTimer(self, interval=1000, timeout=self.show_date_time)
        timer2 = QTimer(self, interval=10, timeout=self.display_data)
        
        timer1.start()
        timer2.start()

        self.take_image_button.clicked.connect(self.register_infos)
        self.registration_button.clicked.connect(self.train_model)
        self.save_image_button.clicked.connect(self.save_students_informations)
    
    # fire up thread for opening video
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
    
    def train_model(self):
        pass
        '''
        print("Training KNN classifier...")
        classifier = train("knn_examples/train", model_save_path="models/trained_knn_model.clf", n_neighbors=2)
        print("Training complete!")

        
        for i in range(101): 
            # slowing down the loop 
            time.sleep(0.05) 
            # setting value to progress bar 
            self.progress_bar.setValue(i) 
        '''

    
    def save_students_informations(self):
        pass

    def register_infos(self):
        path = "/home/xps/devs/attendance-system-upec/knn_examples/train/"
        last_name = self.last_name_line_edit.text()
        first_name = self.first_name_line_edit.text()
        identifier = self.student_id_line_edit.text()
        img = self.Video.image 
        full_path = path+last_name

        print("Last name  = ",last_name)
        print("First name = ", first_name)
        print("ID         = ", identifier)

        # Create target directory if don't exist
        if not os.path.exists(full_path):
            os.mkdir(full_path)
            print("Directory " , full_path ,  " Created ")
        else:    
            print("Directory " , full_path ,  " already exists")       
            cv2.imwrite(full_path+'/'+last_name+str(randrange(200))+'.jpg', img)

    # Following slots receive signal and execute routine.    
    @pyqtSlot()
    def on_start_pushbutton_clicked(self):
        # When the start button is pressed, face recognition start (bounding box)
        self.Video.face_reco_flag = True
        self.display_data()
        
    
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
    def on_finish_pushbutton_clicked(self):
        self.close()
        
    # Set an display the time in the corresponding label
    @pyqtSlot()
    def show_date_time(self): 
        time = QTime.currentTime()
        time_text = time.toString("HH:mm" if time.second() % 2 == 0 else "HH:mm")
        self.time_label.setText(time_text)
        
        date = QDate.currentDate()
        date_text = date.toString("MM/dd/yyyy")
        self.date_label.setText(date_text)

    # function used to load informations from csv file
    def display_data(self):
        infos_students = []
        with open('attendance.csv') as ff:
            reader = csv.reader(ff)
            line = next(reader)
            for line in reader:
                infos_students.append(line) 
        
        for row_number, row_data in enumerate(infos_students):
            for column_number, data in enumerate( row_data):
                self.table_widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            
            
        
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
    
