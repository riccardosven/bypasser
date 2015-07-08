#! /usr/bin/env python
###############################################################################
##
## fastest.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from cv2 import putText, imread, imshow, waitKey, FONT_HERSHEY_PLAIN, CV_LOAD_IMAGE_COLOR
import datetime
from utilities.sound import Sound

class Fastest:

    SPEED_CONVERSION = 0.015517241

    def __init__(self,display):
        self.output_port = display
        self.image_black = imread('behaviours/images/black_background.jpg',CV_LOAD_IMAGE_COLOR)
        self.fanfare = Sound('behaviours/sounds/formula1.wav') # ADD SOME COOL SOUND
        self.today = datetime.datetime.now().day
        self.max_speed_today = 0

    def push(self,data):
        self.speed = data[0]
        self.speed = self.SPEED_CONVERSION*self.speed # Convert from px/sec to km/h
        return True

    def condition(self):
        # If the current date is different from the one in the last detection reset the maxspeed
        # and the date
        if not datetime.datetime.now().day == self.today:
            self. max_speed_today = 0
            self.today = datetime.datetime.now().day
        # If the speed is highest today
        if self.speed > self.max_speed_today:
            self.max_speed_today = self.speed
            return True
        else:
            return False

    def show(self):
        # Image with no text
        self.image_text = self.image_black.copy()
        self.fanfare.play()
        self.textcolor = (0 , 255, 255) # YELLOW
        putText(self.image_text,'You are the',(70,120),FONT_HERSHEY_PLAIN,8,self.textcolor,10)
        putText(self.image_text,' Fastest',(70,300),FONT_HERSHEY_PLAIN,10,self.textcolor,14)
        putText(self.image_text,'  today',(70,450),FONT_HERSHEY_PLAIN,10,self.textcolor,10)
        putText(self.image_text,"{:.1f}".format(self.speed)+' km/h!',(50,600),FONT_HERSHEY_PLAIN,10,self.textcolor,10)
        for i in range(5):
            imshow(self.output_port, self.image_text)
            waitKey(600)
            imshow(self.output_port, self.image_black)
            waitKey(300)
