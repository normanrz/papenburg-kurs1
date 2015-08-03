import cv2
import numpy as np
capture = cv2.VideoCapture(0)
while True:
  _, frame = capture.read()
  b = frame[:,:,0]
  g = frame[:,:,1]
  r = frame[:,:,2]
  cv2.imshow("image(r)", r)
  cv2.imshow("image(g)", g)
  cv2.imshow("image(b)", b)
  cv2.waitKey(1)