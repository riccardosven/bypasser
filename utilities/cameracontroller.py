#! /usr/bin/env python
###############################################################################
##
## cameracontroller.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################
import cv2
import numpy as np
import threading
from time import time


class CameraController(threading.Thread):
    """Generic Motion detector class"""
    # Constants to be used
    SINGLE_PX_THRESHOLD = 20
    IMAGE = 1
    FRAME = 2
    DIFFERENCE = 3

    def __init__(self):
        """Activate Thread with camera control"""
        super(CameraController,self).__init__()
        self.active = True # Camera activation control
        self.stream = cv2.VideoCapture(1) # Open video stream
        while not self.stream.isOpened():
            pass
        _,self.image = self.stream.read()# Save the first frame
        cv2.waitKey(10)
        self.frame = self.image[196:304,:546,:]# Cropped frame
        self.diff_frame = self.frame
        self.tic = time()
        self.frame_rate = 0

    def run(self):
        """Activate camera thread"""
        self.frame_count = 1 # Used for framerate estimation
        while self.active: # If we don not deactivate camera with deactivate()...
        # Framerate Estimation code snippet
            if self.frame_count == 50:
                self.frame_rate = 50/(time() -self.tic)
                self.frame_count = 1
                self.tic = time()

            self.frame_count +=1
            # End Framerate snippet

            self.prevframe = self.frame
            _,self.image = self.stream.read() # Save an image from the steam
            cv2.waitKey(10) # Allow for camera update... needed?
            self.frame = self.image[196:304,:546,:]# Cropped frame
            cv2.absdiff(self.frame,self.prevframe,self.diff_frame)
            self.diff_frame = cv2.threshold(self.diff_frame,self.SINGLE_PX_THRESHOLD,255,cv2.THRESH_TOZERO)[1]
            
    def fetch(self,image_type):
        """Return IMAGE, FRAME or DIFFERENCE"""
        if image_type == self.IMAGE:
            return self.image
        elif image_type == self.FRAME:
            return self.frame
        elif image_type ==self.DIFFERENCE:
            return self.diff_frame
        else:
            print("Error defining frame to be fetched!!!")

    def deactivate(self):
        """Deactivate camera"""
        self.active = False

    def framerate(self):
        """Return framerate [float]"""
        return self.frame_rate
