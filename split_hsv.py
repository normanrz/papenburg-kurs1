import cv2
import numpy as np
capture = cv2.VideoCapture(0)
while True:
  _, frame = capture.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  h = frame[:,:,0]
  s = frame[:,:,1]
  v = frame[:,:,2]
  cv2.imshow("image(h)", h)
  cv2.imshow("image(s)", s)
  cv2.imshow("image(v)", v)
  cv2.waitKey(1)