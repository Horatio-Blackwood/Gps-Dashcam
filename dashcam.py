# Author:  Adam Anderson
# Date:    September 26, 2014
# Module:  dashcam.py
# Python:  2.7.3

import pygame
import pygame.camera

def initialize():
    pygame.init
    pygame.camera.init()

    cam = find_cam()
    cam.start()
    #print cam.get_controls()

    return cam


def find_cam():
    camlist = pygame.camera.list_cameras()
    #print camlist
    if camlist:
        return pygame.camera.Camera(camlist[0], (1280, 720))


def take_picture(cam, filename):
    img = cam.get_image()
    #print "Capturing:  " + filename
    pygame.image.save(img, filename)
