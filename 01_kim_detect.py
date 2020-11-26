import cv2
import numpy as np
import face_recognition
import dlib
import os
import datetime
from imutils import face_utils
from collections import OrderedDict

def uniq3(aList):
    d = OrderedDict()
    for i in aList:
        d[i] = True
    return list(d.keys())

detector = dlib.get_frontal_face_detector()

# Load a sample picture and learn how to recognize it.
sagaf_img = face_recognition.load_image_file("images/Sagaf.jpg")
sagaf_encodings = face_recognition.face_encodings(sagaf_img)[0]

# Load a second sample picture and learn how to recognize it.
sakina_img = face_recognition.load_image_file("images/Ellon.jpg")
sakina_encodings = face_recognition.face_encodings(sagaf_img)[0]
    
# Create arrays of known face encodings and their names
known_face_encodings = [
    sagaf_encodings,
    sakina_encodings
]
    
known_face_names = [
    "Sagaf",
    "Ellon"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_name = []
process_this_frame = True

cap = cv2.VideoCapture(0)
Start_Time = datetime.datetime.now()

while True:
    # Getting out image by webcam
    ret, frame = cap.read()
    if ret == True:
        Time = datetime.datetime.now().time()
        
        # Converting the image to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Get faces into webcam's image
        rects = detector(gray, 0)
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=2)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                    
                # Use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    face_names.append(name)
                    face_name.append(name)
                    new_face_name = uniq3(face_name)
        process_this_frame = not process_this_frame
        
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 255), 2)
            
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 255), cv2.FILLED), 
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    # Show the image
    cv2.imshow('Video', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

End_Time = datetime.datetime.now()
duration = ((End_Time - Start_Time).total_seconds())

# Release handle to the webcam
# cap.release()
cv2.destroyWindow('Video')
cv2.destroyAllWindows()  