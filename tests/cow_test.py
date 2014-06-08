#! /usr/bin/env python
###############################################################################
##
## cow_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import cv2
from behaviours.cow import Cow

cv2.namedWindow('test')
cv2.waitKey(20)

moo = Cow('test')
moo.push((0,0))
print moo.condition() # Returns true 5% of the time XD
moo.show()

