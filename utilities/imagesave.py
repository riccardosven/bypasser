#! /usr/bin/env python
###############################################################################
##
## imagesave.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from cv2 import imwrite
import datetime

class Imagesave:

    def __init__(self,folder):
        self.filefolder = folder

    def save(self,im_file):
        imwrite(self.filefolder+'/'+str(datetime.datetime.now())+'.jpg',im_file)
