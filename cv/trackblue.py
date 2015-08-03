import cv2
import numpy as np
capture = cv2.VideoCapture(0)

def nothing(x):
  pass

cv2.namedWindow('mask')
cv2.createTrackbar('H','mask',0,255,nothing)

while True:
  hValue = cv2.getTrackbarPos('H','mask')
  lower = np.array([hValue-15.0%255.0, 80, 100], dtype = "uint8")
  upper = np.array([hValue+15.0%255.0, 255, 255], dtype = "uint8")
  _, frame = capture.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  blueMask = cv2.inRange(frame, lower, upper)
  cv2.imshow("mask", blueMask)
  if cv2.waitKey(1) & 0xFF == ord("q"):
		break

capture.release()
cv2.destroyAllWindows()