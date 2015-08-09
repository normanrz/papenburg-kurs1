import cv2
from framework import run_video_capture


def func(frame):
    frame = cv2.bitwise_not(frame)
    cv2.imshow("frame", frame)
    cv2.imwrite("test.png", frame)

run_video_capture(func)
