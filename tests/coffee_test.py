#! /usr/bin/env python
###############################################################################
##
## coffee_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import cv2
from behaviours.coffee import Coffee

cv2.namedWindow('test')
cv2.waitKey(20)

cup = Coffee('test')

print(cup.condition()) # Returns if not between three and whatever...
cup.show()

