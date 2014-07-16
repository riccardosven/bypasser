###############################################################################
##
## robot_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from utilities.robot_hand import RobotHand

serial = RobotHand('/dev/ttyACM0',9600)

serial.send('test')
