import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame2 = cv2.Sobel(frame, -1,0,1)
  frame = cv2.Sobel(frame, -1, 1,0)
  frame = frame.astype(np.uint32)
  frame2 = frame2.astype(np.uint32)
  f = np.square(frame) + np.square(frame2)
  frame = np.sqrt(f)
  frame = frame.astype(np.uint8)
  _, frame = cv2.threshold(frame, 180, 255, cv2.THRESH_BINARY)
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
