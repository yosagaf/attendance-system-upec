from Ui_saftey_SR import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2
import os
from datetime import datetime
from face_reco import predict, show_prediction_labels_on_image, markAttendance

class VideoThread(QThread, Ui_MainWindow):
    
    # define new signals with pyqtSignal 
    camera_frame = pyqtSignal(QImage)
    open_video_flag = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()

    def run(self):
        
        self.run_camera = True
        
        #self.video_path = 'videos/test.mp4'
        self.cap = cv2.VideoCapture(0)  # read video from the webcam
        fps = self.cap.get(cv2.CAP_PROP_FPS) # get the number of frames

        #get the size of each frame of the cap video stream  
        size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),  
                int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  

        h = size[1]
        w = size[0]        
        
        COUNT = 0
        total_number_frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT) 
        
        if (self.cap.isOpened()):
            while self.run_camera:                # while using the webcam
            #while COUNT < total_number_frame:      # while using video stored in the pc
                ret,  self.img_read = self.cap.read()
                if self.img_read.all:
                    h, w = self.img_read.shape[:2]
                                
                cv2.waitKey(1)       

                if ret !=None :
                    
                    input_img = cv2.resize(self.img_read, (0, 0), fx=0.5, fy=0.5)
                    input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                    
                    predictions = predict(input_img, model_path = "models/trained_knn_model.clf")
                    input_img = show_prediction_labels_on_image(input_img, predictions)
                    
                    show_pic = QImage(input_img.data,  w, h, QImage.Format_RGB888)       
                    
                    #markAttendance(predictions)

                    if self.run_camera:
                        self.camera_frame.emit(show_pic)
                    else:
                        break
                    #time.sleep(0.005)
                else:
                    print('Video opened')
                COUNT = COUNT + 1
            self.cap.release()
            self.quit()
        else:
            self.open_video_flag.emit(self.cap.isOpened()) 

    def stop_video(self):
        self.run_camera = 0
        self.terminate()