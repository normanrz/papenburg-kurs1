import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  #print frame[0,0]
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
  #ret,frame_thres = cv2.threshold(frame, 10, 10, cv2.THRESH_BINARY)
  print frame[0,0,0] 
  frame_res = cv2.inRange(frame,np.array([120,50,50]),np.array([240,250,250])) 
  frame_res = cv2.erode(frame_res, (85,85))  
  frame_res = cv2.dilate(frame_res, (85,85))

  cv2.imshow('frame',frame_res)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()