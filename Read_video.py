from Ui_saftey_SR import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2
from face_reco import predict, show_prediction_labels_on_image

class VideoThread(QThread, Ui_MainWindow):
    CameraFram = pyqtSignal(QImage)
    OpenVideoFlage = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()

    def run(self):
        
        self.Run_Camera = 1
        #self.video_path = 'video.mp4'
        self.cap = cv2.VideoCapture(0)  # read video
        fps = self.cap.get(cv2.CAP_PROP_FPS) # get the number of frames
        print(fps)
        #Get the size of each frame of the cap video stream  
        size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),  
                int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  

        h = size[1]
        w = size[0]        
        
        COUNT = 0
        totalFrameNumber = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)   
        process_this_frame = 9
        print(size)
        
        if (self.cap.isOpened()):
            while self.Run_Camera:                # while using the webcam
            #while COUNT < totalFrameNumber:      # while using video stored in the pc
                ret,  self.img_read = self.cap.read()
                if self.img_read.all:
                    h, w = self.img_read.shape[:2]
                
                cv2.waitKey(1) #延时1s
                
                if ret !=None :
                    
                    process_this_frame = process_this_frame + 1
                    
                    #input_img = cv2.resize(self.img_read, (0, 0), fx=1, fy=1)
                    input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                    show_pic = QImage(input_img.data,  w, h, QImage.Format_RGB888)       
                            
                    if self.Run_Camera:
                        self.CameraFram.emit(show_pic)
                    else:
                        break
                    #time.sleep(0.005)
                else:
                    print('Video opened')
                COUNT = COUNT + 1
            self.cap.release()
            self.quit()
        else:
            self.OpenVideoFlage.emit(self.cap.isOpened()) # 
    
    def Stop_Video(self):
        self.Run_Camera = 0
        self.terminate()
        