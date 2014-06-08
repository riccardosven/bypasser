#! /usr/bin/env python
###############################################################################
##
## hand_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import cv2
from behaviours.handwave import Handwave

cv2.namedWindow('test')
cv2.waitKey(20)

hand = Handwave('test')

print(hand.condition()) # Returns if not between three and whatever...
hand.show()

