import cv2
import numpy as np
from framework import run_video_capture


def nothing(*args):
    pass


def func(frame):
    hValue = cv2.getTrackbarPos("H", "mask")
    lower = np.array([hValue - 15.0 % 255.0, 80, 100], dtype="uint8")
    upper = np.array([hValue + 15.0 % 255.0, 255, 255], dtype="uint8")

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blueMask = cv2.inRange(frame, lower, upper)
    cv2.imshow("mask", blueMask)

cv2.namedWindow("mask")
cv2.createTrackbar("H", "mask", 0, 255, nothing)

run_video_capture(func)
