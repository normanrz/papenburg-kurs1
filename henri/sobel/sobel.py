import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame_x = cv2.Sobel(frame, -1, 1, 0)
  frame_y = cv2.Sobel(frame, -1, 0, 1)
  frame = frame.astype(np.uint32)
  frame_x = frame_x.astype(np.uint32)
  frame_y = frame_y.astype(np.uint32)

  frame = np.sqrt(np.square(frame_x) + np.square(frame_y))

  frame = frame.astype(np.uint8)
  _, frame = cv2.threshold(frame, 200, 255, cv2.THRESH_BINARY)
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
