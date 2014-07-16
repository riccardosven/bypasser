#! /usr/bin/env python
###############################################################################
##
## robot_hand.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import serial

class RobotHand:

    def __init__(self,device,baudrate):
        try:
            self.port = serial.Serial(device,baudrate)
        except:
            print('Could not open serial port')

    def send(self,command):
        try:
            self.port.write(command)
        except:
            print('Cannot write to Arduino')

    def close(self):
        try:
            self.port.close()
        except:
            pass
