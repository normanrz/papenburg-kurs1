import numpy as np
import cv2

loB = np.array([7, 0, 0])

upB = np.array([18, 255, 255])

cam = cv2.VideoCapture(0)

while(True):
     work,frame = cam.read()

     if(not work):
         print("Sorry, something did not work")
         break
     
     tohsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
     
     skin = cv2.inRange(tohsv, loB, upB)
     
     cv2.imshow("skindet", skin)
     
     if cv2.waitKey(1) & 0xFF == ord("q"):
         break

cam.release()	
cv2.destroyAllWindows()
