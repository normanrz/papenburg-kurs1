import numpy as np
import cv2

cap = cv2.VideoCapture(0)
upper= np.array([20, 255, 255])
lower= np.array([0, 70, 0])
blur = np.array([[1/16.0,2/16.0,1/16.0], [2/16.0,4/16.0,2/16.0],[1/16.0,2/16.0,1/16.0]])
blur1 = np.ones((20,20),dtype=np.int)/400.0
dilate = np.array((20,20),dtype=np.int)/400.0
while(True):
  ret, frame = cap.read()
  print(frame)
  frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  frame1 = cv2.inRange(frame1, lower, upper)
  frame2 = cv2.filter2D(frame1, -1, blur1)
  frame2 = cv2.inRange(frame2, 5, 255)
  '''frame[frame1 > 0] =[255, 255, 0]'''
  frame[frame2 < 1] =[0,0,0]
  '''frame2 = cv2.dilate(frame2, dilate)'''
  '''cv2.imshow('frame',frame)'''
  cv2.imshow('frame',frame)
  cv2.imshow('frame2',frame2)
  '''font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(frame1,"Hallo Welt",(5,25), font, 4, (0, 255, 0), 2, cv2.LINE_AA
              )'''
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

