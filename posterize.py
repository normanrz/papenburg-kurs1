def nothing(x):
  pass

import cv2
capture = cv2.VideoCapture(0)

cv2.namedWindow("image")
cv2.createTrackbar('R lower Threshold','image',0,255,nothing)
cv2.createTrackbar('R upper Threshold','image',0,255,nothing)
cv2.createTrackbar('G lower Threshold','image',0,255,nothing)
cv2.createTrackbar('G upper Threshold','image',0,255,nothing)
cv2.createTrackbar('B lower Threshold','image',0,255,nothing)
cv2.createTrackbar('B upper Threshold','image',0,255,nothing)

 
while True:
  _, frame = capture.read()
  b,g,r = cv2.split(frame)
  r = cv2.inRange(r, cv2.getTrackbarPos('R lower Threshold','image'), cv2.getTrackbarPos('R upper Threshold','image') )
  g = cv2.inRange(g, cv2.getTrackbarPos('G lower Threshold','image'), cv2.getTrackbarPos('G upper Threshold','image') )
  b = cv2.inRange(b, cv2.getTrackbarPos('B lower Threshold','image'), cv2.getTrackbarPos('B upper Threshold','image') ) 

  
  frame = cv2.merge([b,g,r])
  cv2.imshow("image", frame)
  key = cv2.waitKey(1)
  if key%256 == 27:
    exit()