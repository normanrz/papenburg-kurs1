import cv2
capture = cv2.VideoCapture(0)
subtractFrame = None
while True:
  b, frame = capture.read()
  if subtractFrame != None:
    displayFrame = 255 - cv2.subtract(subtractFrame, frame)
  else:
    displayFrame = frame
  cv2.imshow("image", displayFrame)
  key = cv2.waitKey(1)
  if key%256 == 32:
    subtractFrame = frame
  if key%256 == 27:
    exit()
