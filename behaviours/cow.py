###############################################################################
##
## cow.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from cv2 import imread, imshow, waitKey, CV_LOAD_IMAGE_COLOR
from numpy.random import uniform
from utilities.sound import Sound

class Cow:
    COW_PROBABILITY = 0.05

    def __init__(self, display):
        self.output_port = display
        self.image_cow = imread('behaviours/images/cow.jpg',CV_LOAD_IMAGE_COLOR)
        self.image_black = imread('behaviours/images/black_background.jpg',CV_LOAD_IMAGE_COLOR)
        self.moo = Sound('behaviours/sounds/cow_moo.wav')
        self.nextiscow = False

    def push(self,data):
        self.nextiscow = uniform() < self.COW_PROBABILITY # Update cow event
        return True

    def condition(self):
        return self.nextiscow # Do we have a cow pending?

    def show(self): # Show the cow!
        self.moo.play()
        imshow(self.output_port,self.image_cow)
        waitKey(5000)
        imshow(self.output_port,self.image_black)
        waitKey(20)
        self.nextiscow = False # Clear the pending cow...

