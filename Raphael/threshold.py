import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
  frame2 = frame
  _, frame = cv2.threshold(frame2, 100, 255, cv2.THRESH_BINARY_INV)
  frame = cv2.erode(frame, (30,30))
  frame = cv2.dilate(frame, (30,30))
  print(frame)
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('r'):
    break

cap.release()
cv2.destroyAllWindows()
