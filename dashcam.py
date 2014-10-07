# Author:  Adam Anderson
# Date:    September 26, 2014
# Module:  dashcam.py
# Python:  2.7.3

import picamera

def initialize(img_width, img_height):
    cam = picamera.PiCamera()
    cam.resolution = (img_width, img_height)
    return cam


def cleanup_camera(cam):
    cam.close()


def take_picture(cam, filename):
    cam.capture(filename)
