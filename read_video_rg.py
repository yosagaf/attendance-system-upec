from gui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2
import os
import numpy as np
from datetime import datetime
from knn_classifier import predict, show_prediction_labels_on_image, get_attendance

class VideoThreadRG(QThread, Ui_MainWindow):
   
    # define new signals with pyqtSignal 
    camera_frame = pyqtSignal(QImage)
    face_reco_flag = False
    capture_flag = False

    image = 0

    def __init__(self):
        super().__init__()

    def run(self):
        
        self.run_camera_rg = True
        
        #self.video_path = 'videos/test.mp4'
        #self.caprg = cv2.VideoCapture(self.video_path)
        self.caprg = cv2.VideoCapture(0)  # read video from the webcam
        fps = self.caprg.get(cv2.CAP_PROP_FPS) # get the number of frames

        #get the size of each frame of the caprg video stream  
        size = (int(self.caprg.get(cv2.CAP_PROP_FRAME_WIDTH)),  
                int(self.caprg.get(cv2.CAP_PROP_FRAME_HEIGHT)))  

        h = size[1]
        w = size[0]   
        image = np.zeros((h,w,3), np.uint8)     
        
        COUNT = 0
        total_number_frame = self.caprg.get(cv2.CAP_PROP_FRAME_COUNT) 
        
        if (self.caprg.isOpened()):
            while self.run_camera_rg:                # while using the webcam
            #while COUNT < total_number_frame:      # while using video stored in the pc
                ret,  self.img_read = self.caprg.read()
                if self.img_read.all:
                    h, w = self.img_read.shape[:2]
                                
                cv2.waitKey(1)       

                if ret !=None :
                    
                    input_img = cv2.resize(self.img_read, (0, 0), fx=0.5, fy=0.5)
                    image = input_img

                    input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                                            
                    show_pic = QImage(input_img.data,  w, h, QImage.Format_RGB888)

                    if self.run_camera_rg: # send every time the frame to show
                        # emit the signal
                        self.camera_frame.emit(show_pic)
                    else:
                        break
                    #time.sleep(0.005)
                else:
                    print('Video opened')
                COUNT = COUNT + 1
            self.caprg.release()
            self.quit()
        else:
            # if the camera is not open, the signal is emitted
            self.open_video_flag.emit(self.caprg.isOpened()) 

    def stop_video_rg(self):
        self.run_camera_rg = False
        self.terminate()