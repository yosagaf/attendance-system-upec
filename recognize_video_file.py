# USAGE
#python3 recognize_video_file.py --detector models --embedding-model models/nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle -i videos/test.mp4

from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import yaml
import pickle
import time
import cv2
import os

with open("configs/config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

print(cfg["files"]["recognizer"])
print(cfg["files"]["embedding_model"])
print(cfg["files"]["reco_model_path"])
print(cfg["files"]["proto_path"])
print(cfg["files"]["le"])

# load the face detector from disk
print("Loading Caffe based face detector...")
protoPath = cfg["files"]["proto_path"]
modelPath = cfg["files"]["reco_model_path"]
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load the face embedding model from disk
print("Loading Openface imlementation of Facenet model...")

embedder = cv2.dnn.readNetFromTorch(cfg["files"]["embedding_model"])

# load the actual face recognition model along with the label encoder
recognizer = pickle.loads(open(cfg["files"]["recognizer"], "rb").read())
le = pickle.loads(open(cfg["files"]["le"], "rb").read())


# initialize the pointer to the video file and the video writer
print("Processing Video file....")
stream = cv2.VideoCapture(0)

'''
# loop over frames from the video file stream
while True:
	# grab the next frame
	(grabbed, frame) = stream.read()

	# if the frame was not grabbed, then we have reached the
	# end of the stream
	if not grabbed:
		break

	# resize the frame to have a width of 600 pixels (while
	# maintaining the aspect ratio), and then grab the image
	# dimensions
	frame = imutils.resize(frame, width=600)
	(h, w) = frame.shape[:2]

	# construct a blob from the image
	imageBlob = cv2.dnn.blobFromImage(
		cv2.resize(frame, (300, 300)), 1.0, (300, 300),
		(104.0, 177.0, 123.0), swapRB=False, crop=False)

	# apply OpenCV's deep learning-based face detector to localize
	# faces in the input image
	detector.setInput(imageBlob)
	detections = detector.forward()

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections with less than 50% confidence
		if confidence > 0.5:
			# compute the (x, y)-coordinates of the bounding box for
			# the face
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# extract the face ROI
			face = frame[startY:endY, startX:endX]
			(fH, fW) = face.shape[:2]

			# ensure the face width and height are sufficiently large
			if fW < 20 or fH < 20:
				continue

			# construct a blob for the face ROI, then pass the blob
			# through our face embedding model to obtain the 128-d
			# quantification of the face
			faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
				(96, 96), (0, 0, 0), swapRB=True, crop=False)
			embedder.setInput(faceBlob)
			vec = embedder.forward()

			# perform classification to recognize the face
			preds = recognizer.predict_proba(vec)[0]
			j = np.argmax(preds)
			proba = preds[j]
			name = le.classes_[j]

			# draw the bounding box of the face along with the
			# associated probability
			text = "{}: {:.2f}%".format(name, proba * 100)
			y = startY - 10 if startY - 10 > 10 else startY + 10
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				(0, 0, 255), 2)
			cv2.putText(frame, text, (startX, y),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

		key = cv2.waitKey(1) & 0xFF
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

# close the video file pointers
stream.release()

'''