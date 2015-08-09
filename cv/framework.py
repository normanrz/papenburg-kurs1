import cv2
import numpy as np
import inspect


def run_video_capture(func, camera_index=0):
    try:
        cap = cv2.VideoCapture(camera_index)
        while True:
            _, frame = cap.read()
            if frame is None:
                raise ValueError("Couldn't read frame from camera.")

            if func(frame) == False:
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
