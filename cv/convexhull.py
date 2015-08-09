import numpy as np
import cv2

camera = cv2.VideoCapture(0)

lower = np.array([0, 18, 18], dtype="uint8")
upper = np.array([25, 255, 255], dtype="uint8")

while True:

    returnCode, frame = camera.read()
    if not returnCode:
        print("Camera could not be read!")
        break

    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)

    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    cv2.imshow("mask", skinMask)
    contours, _ = cv2.findContours(skinMask,
                                   cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)

    skin = cv2.bitwise_and(frame, frame, mask=skinMask)

    for i, c in enumerate(contours):

        if(cv2.contourArea(c) < 100):
            continue

        cv2.drawContours(frame, contours[i], -1, (0, 0, 255), 3)
        hull = cv2.convexHull(contours[i])

        # print cv2.moments(contours[i])

        if(len(hull) > 3):
            cv2.drawContours(frame, hull, -1, (0, 255, 0), 3, lineType=8)

        for i, p in enumerate(hull[:-1]):
            cv2.line(frame,
                     tuple(hull[i][0]),
                     tuple(hull[i+1][0]),
                     color=(0, 255, 0))

    cv2.imshow("images", frame)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
