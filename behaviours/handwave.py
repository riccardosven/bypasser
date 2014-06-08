#! /usr/bin/env python
###############################################################################
##
## handwave.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from cv2 import imread, imshow, waitKey, CV_LOAD_IMAGE_COLOR
from utilities.sound import Sound

class Handwave:
    def __init__(self, display):
        self.output_port = display
        self.image_hand= [imread('behaviours/images/hand_wave0.jpg',CV_LOAD_IMAGE_COLOR),imread('behaviours/images/hand_wave1.jpg',CV_LOAD_IMAGE_COLOR),imread('behaviours/images/hand_wave2.jpg',CV_LOAD_IMAGE_COLOR),imread('behaviours/images/hand_wave1.jpg',CV_LOAD_IMAGE_COLOR)]
        self.image_black = imread('behaviours/images/black_background.jpg',CV_LOAD_IMAGE_COLOR)
	self.bell = Sound('behaviours/sounds/airplane_bell.wav')

    def push(self,data):
        return True

    def condition(self):
        """Return default True condition"""
        return True

    def show(self):
        """Display handwaving animation"""
	self.bell.play()
        for j in range(0,3):
            for i in range(0,4):
                imshow(self.output_port,self.image_hand[i])
                waitKey(200)
        imshow(self.output_port,self.image_black)
        waitKey(20)
