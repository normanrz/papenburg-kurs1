import numpy as np
import cv2
cap = cv2.VideoCapture(0)
b = True
upper = np.array([40, 255, 255])
lower = np.array([0, 20, 0])
blur1 = np.array([[1/16.0,2/16.0,1/16.0],[2/16.0,4/16.0,2/16.0],[1/16.0,2/16.0,1/16.0]])
blur2 = np.ones((20,20),dtype=np.int)/400.0
while(True):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    img = cv2.inRange(img, lower, upper)
    img2 = cv2.filter2D(img, -1, blur2)
    img2 = cv2.inRange(img2, 50, 255)

    
    frame[img > 0] = [255, 255, 0]
    cv2.imshow('frame2', img2)
    
    cv2.imshow('frame', img)
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        b = True
    while(b):
        if cv2.waitKey(1) & 0xFF == ord('s'):
            b = False
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
