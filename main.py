#! /usr/bin/env python
###############################################################################
##
## main.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

#from utilities.nonthreading_cameracontroller import CameraController
from utilities.nonthreading_cameracontroller import CameraController
from utilities.motiondetector import MotionDetector
from utilities.datalogger import Datalogger
from utilities.imagesave import Imagesave
from utilities.graphsave import Graphsave
from behaviours.handwave import Handwave
from behaviours.cow import Cow
from behaviours.coffee import Coffee
from behaviours.speed import Speed
from behaviours.fastest import Fastest
import sys
from cv2 import namedWindow, waitKey 
from time import sleep

# Initialize a new motion controller object
camera = CameraController()
detector = MotionDetector()

# Start main output display
namedWindow('Display')
waitKey(20)

# Start the dataloggers
log = Datalogger('detection_log.log')
imageprinter = Imagesave('captured_images')
plotprinter = Graphsave('captured_plots')

# Initialize output behaviours, the argument is the viewport they are going to use to display the output
handwaves = Handwave('Display')
cow = Cow('Display')
speed = Speed('Display')
coffetime = Coffee('Display')
fastest = Fastest('Display')

# List the effects, in order of precedence
effect_list = [cow, coffetime, fastest, speed, handwaves]

# Start camera controller thread
# camera.start()

key = -1
#while key != 27: # 1048603
while key == -1: # 1048603
    # Update the detector
    camera.update() # For nonthreading camera
    sys.stdout.write('%s fps\r'%camera.framerate())
    sys.stdout.flush()
    difference_image = camera.fetch(camera.DIFFERENCE)
    camera_frame = camera.fetch(camera.IMAGE)
    detector.update(difference_image)
    detector_data = detector.data()
    detector_dump = detector.dump()

    # If we have a detector...
    if detector.detection():
        # ...cycle through the effects...
        for effect in effect_list:
            effect.push(detector_data)
            # ...checking if the conditions for one is true...
            if effect.condition():
                imageprinter.save(camera_frame)
                plotprinter.save(detector_dump[0],detector_dump[1],detector_data[0],detector_data[1])
                log.update(detector_data,cow.condition())
                # ...showing that effect...
                effect.show()
                break #...and that's it for now!

    # Update viewport... maybe not needed...
    key = waitKey(10)

# Kill camera thread
camera.deactivate()

