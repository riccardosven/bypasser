#! /usr/bin/env python
###############################################################################
##
## speed_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import cv2
from behaviours.speed import Speed

cv2.namedWindow('test')
cv2.waitKey(20)

speed  = Speed('test')

print(speed.condition()) # Returns true

speed.push((1,422.22))
speed.show()

speed.push((1,322.22))
speed.show()

speed.push((1,122.22))
speed.show()
