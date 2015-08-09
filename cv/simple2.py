import cv2
import numpy as np
from framework import run_video_capture


def func(frame):
    frame = np.fliplr(frame)
    cv2.imshow("frame", frame)

run_video_capture(func)
