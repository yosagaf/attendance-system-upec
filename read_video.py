from gui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2
import os
from datetime import datetime
from knn_classifier import predict, show_prediction_labels_on_image, get_attendance, mark_attendance

class VideoThread(QThread, Ui_MainWindow):
   
    # define new signals with pyqtSignal 
    camera_frame = pyqtSignal(QImage)
    open_video_flag = pyqtSignal(bool)
    face_reco_flag = False
    
    students_name = []
    
    def __init__(self):
        super().__init__()

    def run(self):
        
        self.run_camera = True
        self.image = 0
        
        #self.video_path = 'videos/test.mp4'
        #self.cap = cv2.VideoCapture(self.video_path)
        self.cap = cv2.VideoCapture(0)  # read video from the webcam
        fps = self.cap.get(cv2.CAP_PROP_FPS) # get the number of frames
           
        COUNT = 0
        total_number_frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT) 
        
        if (self.cap.isOpened()):
            while self.run_camera:                  # while using the webcam
            #while COUNT < total_number_frame:      # while using video stored in the pc
                ret,  self.img_read = self.cap.read()
                if self.img_read.all:
                    h, w = self.img_read.shape[:2]
                                
                cv2.waitKey(1)       

                if ret !=None :
                    
                    input_img = cv2.resize(self.img_read, (0, 0), fx=0.5, fy=0.5)
                    self.image = input_img
                    input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                    
                    if self.face_reco_flag:
                        predictions = predict(input_img, model_path = "models/trained_knn_model.clf")
                                                                    
                        if len(predictions) >= 1:
                            records_info = get_attendance(predictions)
                            mark_attendance(records_info)
                        input_img = show_prediction_labels_on_image(input_img, predictions)
                        
                    show_pic = QImage(input_img.data,  w, h, QImage.Format_RGB888)       

                    if self.run_camera: # send every time the frame to show
                        self.camera_frame.emit(show_pic) # emit the signal
                    else:
                        break
                else:
                    print('Video opened')
                COUNT = COUNT + 1
            self.cap.release()
            self.quit()
        else:
            # if the camera is not open, the signal is emitted
            self.open_video_flag.emit(self.cap.isOpened()) 

    def stop_video(self):
        self.run_camera = False
        self.terminate()
