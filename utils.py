import cv2
import numpy as np
from PIL import Image


def waitForKey(delay=15, key=27):
    """Returns if key (Escape, by default) is pressed"""
    if cv2.waitKey(delay) == key:
        raise "User has quit, this is perfectly normal."


def flip_horizontal(frame: np.ndarray):
    return np.flip(frame, 1)


def to_rgb(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def to_bgr(frame):
    return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


def to_pillow(frame):
    return Image.fromarray(frame)
