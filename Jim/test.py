import numpy as np
import cv2

# Kamera oeffnen
camera = cv2.VideoCapture(0)
lower = np.array([7,0,0])
upper = np.array([17,255,255])
#cernel = np.array([[1,1,1][1,1,1,][1,1,1]])

#cv2.createtrackbar
#blur cv2.ones?

# Immer wieder
while(True):
	# Kamerabild lesen
	_, frame = camera.read()
	frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	frame2 = cv2.inRange(frame2, lower, upper)
	kernel = np.ones((2,2), np.uint8)/4
	frame2 = cv2.erode(frame2,kernel, iterations=3)
	frame2 = cv2.dilate(frame2,kernel, iterations=3)
	cv2.imshow("frame", frame2)
	#cv2.imshow("frame2", frame2)
	#print(frame2[:,:,2])
	# bei q abbrechen
	if cv2.waitKey(1) & 0xFF == ord("q"):
		#print(frame2[:,:,0] < 30)
		break
	elif 0xFF == ord("s"): # wait for "s" key to save and exit
                cv2.imwrite("messigray.png",img)
                cv2.destroyAllWindows()


#Aufraeumen: Fenster und Kamera schliessen
camera.release()
cv2.destroyAllWindows()
