#! /usr/bin/env python
###############################################################################
##
## fastest_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import cv2
from behaviours.fastest import Fastest

cv2.namedWindow('test')
cv2.waitKey(20)

fast = Fastest('test')

fast.push((1,100))
print(fast.condition()) # Returns true... is the fastest
fast.push((1,49))
print(fast.condition()) # Returns false... speed lower than before!
fast.show()

