from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from register import Ui_MainWindow1
import datetime
import time
import csv
import os
import cv2
from random import randrange
from read_video_rg import VideoThreadRG

class MainWindow1(QMainWindow, Ui_MainWindow1):
    # This class will have access to all of the properties of QThread and Ui_MainWindow
    
    def __init__(self, parent=None):

        super(MainWindow1, self).__init__(parent)
        self.setup(self)
    
        self.Videorg = VideoThreadRG()
        self.open_video_rg()

        self.register_pushbutton.clicked.connect(self.register_infos)
        self.finish_pushbutton.clicked.connect(self.train_model)

    def train_model(self):
        for i in range(101): 
            # slowing down the loop 
            time.sleep(0.05) 
            # setting value to progress bar 
            self.progress_bar.setValue(i) 

    def register_infos(self):
        path = "/home/xps/devs/attendance-system-upec/knn_examples/train/"
        last_name = self.last_name_lineEdit.text()
        first_name = self.first_name_line_edit.text()
        identifier = self.identifier_line_edit.text()
        img = self.Videorg.image 
        full_path = path+last_name

        # Create target directory if don't exist
        if not os.path.exists(full_path):
            os.mkdir(full_path)
            print("Directory " , full_path ,  " Created ")
        else:    
            print("Directory " , full_path ,  " already exists")       
            cv2.imwrite(full_path+'/'+last_name+str(randrange(200))+'.jpg', img)
    
    def open_video_rg(self):
        if not self.Videorg.isRunning():
            self.Videorg.start()
            self.Videorg.camera_frame.connect(self.fresh_camera)
        else:
           self.Videorg.stop_video()
           self.caprg.release()

    def fresh_camera(self, show_pic):   
        # Scale the contents of the label to fill all available space
        self.register_video_label.setScaledContents(True)

        # Convert the QImage object to QPixmap and how images in PyQt window
        self.register_video_label.setPixmap(QPixmap.fromImage(show_pic))
    
    @pyqtSlot() # Decorate a Python method to create a Qt slot.
    def on_finish_pushbutton_clicked(self):
        #self.close()
        pass

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
    
