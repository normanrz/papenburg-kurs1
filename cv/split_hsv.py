import cv2
import numpy as np
from framework import run_video_capture


def func(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h = frame[:, :, 0]
    s = frame[:, :, 1]
    v = frame[:, :, 2]
    cv2.imshow("image(h)", h)
    cv2.imshow("image(s)", s)
    cv2.imshow("image(v)", v)

run_video_capture(func)
