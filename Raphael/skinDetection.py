import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  frame = cv2.inRange(frame, np.array([0,55,80]), np.array([30,200,120]))
  frame = cv2.erode(frame, (3, 3))
  frame = cv2.dilate(frame, (3, 3))
  print(frame[0, 0])
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('r'):
    break

cap.release()
cv2.destroyAllWindows()
