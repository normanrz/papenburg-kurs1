import cv2
import numpy as np
from framework import run_video_capture


subtractFrame = None


def func(frame):
    global subtractFrame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if subtractFrame is None:
        subtractFrame = gray
        displayFrame = frame
    else:
        mask = cv2.subtract(gray, subtractFrame) > 10
        displayFrame = frame * mask[..., np.newaxis]

    cv2.imshow("original", frame)
    cv2.imshow("masked", displayFrame)


run_video_capture(func)
