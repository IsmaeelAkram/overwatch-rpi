import pycamera
from pycamera import camera
import numpy as np
from log import *
from utils import *
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import time

DEVICE_INDEX = 1
CAM_RESOLUTION = (1920, 1080)
CAM_FPS = 60

info("THE OVERWATCH PROGRAM")
cam = camera.Camera(DEVICE_INDEX)
cam.set_resolution(1920, 1080)
cam.set_fps(60)

consolas = ImageFont.truetype("consolas.ttf", 50)
consolas_outline = ImageFont.truetype("consolas.ttf", 50)

while True:
    frame = cam.read()
    frame = camera.Frame(flip_horizontal(frame.to_numpy()))

    image = frame.rgb().to_pillow()
    draw = ImageDraw.Draw(image)
    white = (255, 255, 255)
    black = (0, 0, 0)

    timestamp = str(datetime.now()).split(".")[0]
    draw.text((2, 2), timestamp, align="left", font=consolas_outline, fill=black)
    draw.text((0, 0), timestamp, align="left", font=consolas, fill=white)

    cv2.imshow("", np.array(image))
    time.sleep(1 / CAM_FPS)
    waitForKey()