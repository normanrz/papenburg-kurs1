import numpy as np
import cv2

lowerB = 60
upperB = 220

def nothing(x):
  pass

i = 1

cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.createTrackbar("lowerBorder","frame",lowerB,255,nothing)
cv2.createTrackbar("upperBorder","frame",upperB,255,nothing)

while(True):
  lowerB = cv2.getTrackbarPos("lowerBorder","frame")
  upperB = cv2.getTrackbarPos("upperBorder","frame")
  ret, raw = cap.read()
  frame = raw.copy()
  raw = cv2.cvtColor(raw,cv2.COLOR_BGR2GRAY)
  frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  frame = cv2.GaussianBlur(frame,(5,5),1,1)
  frame2 = cv2.inRange(frame,(250,lowerB,lowerB),(255,upperB,upperB))
  frame = cv2.inRange(frame,(0,lowerB,lowerB),(15,upperB,upperB))
  frame = frame + frame2
  frame = cv2.erode(frame,(85,85))
  frame = cv2.dilate(frame,(85,85))
  frame = threshold(frame,100,100,cv2.TRESH_BINARY)
  frame = raw & frame;
  cv2.imshow('frame',frame)
  
  res = cv2.waitKey(1)
  if res & 0xFF == ord('q'):
    break
  elif res & 0xFF == ord('s'):
    cv2.imwrite("C:\\Test"+str(i)+".bmp",frame)
    i = i +1

print("Beendet...")
cap.release()
cv2.destroyAllWindows()
