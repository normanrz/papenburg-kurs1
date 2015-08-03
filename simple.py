import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame = cv2.bitwise_not(frame)
cv2.imshow('frame', frame)
cv2.imwrite('test.png', frame)