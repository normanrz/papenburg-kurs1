import numpy as np
import cv2

cap = cv2.VideoCapture(0)

upper1=np.array([20, 255, 255])
lower1=np.array([5, 80, 0])

blur1=np.ones((10,10), dtype=np.int)/100.0

while(True):
  ret, frame = cap.read()
  frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  frame=cv2.inRange(frame, lower1, upper1)
  frame=255.0*(cv2.filter2D(frame, -1, blur1)>100.0)
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

