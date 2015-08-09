import cv2
import numpy as np
from framework import run_video_capture


def func(frame):
    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    cv2.imshow("image(r)", r)
    cv2.imshow("image(g)", g)
    cv2.imshow("image(b)", b)

run_video_capture(func)
