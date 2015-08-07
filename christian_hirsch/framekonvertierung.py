import numpy as np
import cv2

cap = cv2.VideoCapture(0)
lower = np.array([6,70, 0])
upper = np.array([20,255, 255])
blur = np.array([[1/9.0, 1/9.0, 1/9.0],[1/9.0 , 1/9.0, 1/9.0],[1/9.0, 1/9.0, 1/9.0]])

while(True):
  
  ret, frame = cap.read()
  
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  frame = cv2.inRange (frame, lower, upper)
  frame = cv2.filter2D (frame, -1, blur)              
#  frame = cv2.erode (frame, [10, 10])
#  frame = cv2.delate (frame, [10, 10])
  
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
