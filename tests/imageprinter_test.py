#! /usr/bin/env python
###############################################################################
##
## imageprinter_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from utilities import cameracontroller
from utilities import imagesave

camera = CameraController()
printer = Imagesave('.')

camera.start()
image = camera.fetch(camera.IMAGE)

printer.save(image)

camera.deactivate()
