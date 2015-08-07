import cv2
import numpy as np
from os import path

CLASSIFIER_PATH = path.join("haarcascade_eye.xml")
faceCascade = cv2.CascadeClassifier(CLASSIFIER_PATH)

def detect_face(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
  )
  return faces


cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  frame = cv2.resize(frame,(600,450))
  for (x, y, h, w) in detect_face(frame):
    cv2.rectangle(
      frame, # target
      (x, y), # topleft
      (x + w, y + h), # bottomright
      (255, 0, 0), # blue (BGR)
      2 # lineWidth
    )
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

