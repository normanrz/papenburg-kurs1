#import the necessary packagesimutils
import numpy as np
import argparse
import cv2
import math

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help = "path to the (optional) video file")
args = vars(ap.parse_args())

# if a video path was not supplied, grab the reference
# to the gray
if not args.get("video", False):
	camera = cv2.VideoCapture(0)
	camera.set(3,1080)
	camera.set(4,720)

# otherwise, load the video
else:
	camera = cv2.VideoCapture(args["video"])

# keep looping over the frames in the video
while True:
	# define the upper and lower boundaries of the HSV pixel
	# intensities to be considered 'skin'

	lower = np.array([0, 18, 18], dtype = "uint8")
	upper = np.array([25, 255, 255], dtype = "uint8")

	# grab the current frame
	(grabbed, frame) = camera.read()

	ychan = frame[:,:,:].dot(np.array([0.299/255.0, 0.587/255.0, 0.114/255.0]))
	ychan = ychan * math.pi
	ychan = np.sin(ychan)


	ichan = frame[:,:,:].dot(np.array([0.596, -0.274, -0.322]))
	michan = frame[:,:,:].dot(np.array([-0.596, 0.274, 0.322]))


	if args.get("video") and not grabbed:
		break

	# resize the frame, convert it to the HSV color space,
	# and determine the HSV pixel intensities that fall into
	# the speicifed upper and lower boundaries
	converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	skinMask = cv2.inRange(converted, lower, upper)

	# apply a series of erosions and dilations to the mask
	# using an elliptical kernel
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
	skinMask = cv2.erode(skinMask, kernel, iterations = 2)
	skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

	# blur the mask to help remove noise, then apply the
	# mask to the frame
	skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
	cv2.imshow("mask", skinMask)
	contours,_ = cv2.findContours(skinMask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	skin = cv2.bitwise_and(frame, frame, mask = skinMask)

	areaArray = []

	if(len(contours)>1):
		for i, c in enumerate(contours):
			area = cv2.contourArea(c)
			areaArray.append(area)
			areaArray.append(area)

		sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)

		cv2.drawContours(frame, sorteddata[0][1], -1, (0,0,255), 3)
		hull = cv2.convexHull(sorteddata[0][1])
		cv2.drawContours(frame, hull, -1, (0,255,0), 3, lineType=8)

		for i,p in enumerate(hull[:-1]):
			cv2.line(frame, tuple(hull[i][0]), tuple(hull[i+1][0]), color =(0,255,0))


	cv2.imshow("images", frame)
	cv2.imshow("lol", cv2.merge([ichan,ychan,michan]))
	cv2.imshow("y", ychan)




	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
