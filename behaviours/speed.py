###############################################################################
##
## speed.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from cv2 import putText, imread, imshow, waitKey, FONT_HERSHEY_PLAIN, CV_LOAD_IMAGE_COLOR
from utilities.sound import Sound

class Speed:

    GREEN_SPEED = 5
    SPEED_CONVERSION = 0.015517241

    def __init__(self,display):
        self.output_port = display
        self.image_black = imread('behaviours/images/black_background.jpg',CV_LOAD_IMAGE_COLOR)
        self.fail = Sound('behaviours/sounds/fail.wav')
        self.tada = Sound('behaviours/sounds/tada.wav')


    def push(self,data):
        self.speed = data[1]
        self.speed = self.SPEED_CONVERSION*self.speed # Convert from px/sec to km/h
        print(self.speed)
        return True

    def condition(self):
        return True

    def show(self):
        # Image with no text
        self.image_text = self.image_black.copy()

        if abs(self.speed -  self.GREEN_SPEED) < 0.05: # If we are going at the right speed
            self.tada.play()
            self.textcolor = (0, 255, 0) # GREEN
            putText(self.image_text,'You walk:',(50,200),FONT_HERSHEY_PLAIN,10,self.textcolor,10)
            putText(self.image_text,'Exactly',(50,400),FONT_HERSHEY_PLAIN,10,self.textcolor,10)
            putText(self.image_text,"{:.1f}".format(self.GREEN_SPEED)+' km/h',(50,600),FONT_HERSHEY_PLAIN,10,self.textcolor,10)
            for i in range(5):
                imshow(self.output_port, self.image_text)
                waitKey(600)
                imshow(self.output_port, self.image_black)
                waitKey(300)
        else: # ...do something else
            if self.speed > self.GREEN_SPEED: # if too fast...
                self.textcolor = (0,0,255) # RED
                putText(self.image_text,'Walk slower!',(50,600),FONT_HERSHEY_PLAIN,9,self.textcolor,10)
            if self.speed < self.GREEN_SPEED: # if too fast...
                self.textcolor = (255,0,0) # BLUE
                putText(self.image_text,'Walk faster!',(50,600),FONT_HERSHEY_PLAIN,9,self.textcolor,10)
            self.fail.play()
            putText(self.image_text,'You walk:',(50,200),FONT_HERSHEY_PLAIN,10,self.textcolor,10)
            putText(self.image_text,"{:.1f}".format(self.speed)+' km/h',(50,400),FONT_HERSHEY_PLAIN,10,self.textcolor,10)
            imshow(self.output_port,self.image_text)
            waitKey(5000)
            imshow(self.output_port,self.image_black)


