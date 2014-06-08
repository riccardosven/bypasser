#! /usr/bin/env python
###############################################################################
##
## coffee.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from cv2 import imread, imshow, waitKey, CV_LOAD_IMAGE_COLOR
from utilities.sound import Sound
import datetime

class Coffee:
    FIKA_START_HOUR = 14
    FIKA_END_HOUR = 15
    FIKA_START_MIN = 30
    FIKA_END_MIN = 30

    def __init__(self, display):
        self.output_port = display
        self.image_coffee = [imread('behaviours/images/coffee_cup0.jpg',CV_LOAD_IMAGE_COLOR),imread('behaviours/images/coffee_cup1.jpg',CV_LOAD_IMAGE_COLOR),imread('behaviours/images/coffee_cup2.jpg',CV_LOAD_IMAGE_COLOR)]
        self.image_black = imread('behaviours/images/black_background.jpg',CV_LOAD_IMAGE_COLOR)
	self.bell = Sound('behaviours/sounds/airplane_bell.wav')

    def push(self,data):
        return True

    def condition(self):
        """Check if it is fika time!"""
        current_time = datetime.datetime.now()
        return current_time.hour*60+current_time.minute > 60*self.FIKA_START_HOUR+self.FIKA_START_MIN and current_time.hour*60+current_time.minute < 60*self.FIKA_END_HOUR+self.FIKA_END_MIN

    def show(self):
        """Display handwaving animation"""
	self.bell.play()
        for j in range(0,3):
            for i in (1,0,1,2):
                imshow(self.output_port,self.image_coffee[i])
                waitKey(200)
        imshow(self.output_port,self.image_black)
        waitKey(20)
