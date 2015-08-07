import numpy as np
import cv2
cap=cv2.VideoCapture(0)
cv2.namedWindow("Original")
while(True):
        ret,frame=cap.read()    
        kernel=np.array(
        [
        [-20.0,20.0,-20.0],
        [20.0,0.0,20.0],
        [-20.0,20.0,-20.0]])
        sharpened= cv2.filter2D(frame,-1,kernel)
        sharpened = cv2.cvtColor(sharpened,cv2.COLOR_BGR2GRAY)
        kernel = np.ones((5,5),np.uint8)
        cv2.imshow('Original',frame)
        cv2.imshow('Sharpened',sharpened)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                

cap.release()
cv2.destroyAllWindows()

