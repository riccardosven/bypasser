#! /usr/bin/env python
###############################################################################
##
## datalogger.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import datetime

class Datalogger:
    
    def __init__(self,filename):
        self.logfile = filename
        self.alarm_nr = 0

    def update(self,data,is_cow):
        self.alarm_nr += 1
        self.slope,_,self.y_dev,self.std_dev = data
        if is_cow:
            self.iscow = 1
        else:
            self.iscow = 0
        print('bypasser',self.alarm_nr,'speed',self.slope,'error',self.std_dev,'timestamp',datetime.datetime.now(),'y_dev',self.y_dev)
        with open(self.logfile,'a') as log_file:
            log_file.write('{},{},{:.3f},{:.3f},{:.3f}\n'.format(datetime.datetime.now(),self.iscow,self.slope,self.y_dev,self.std_dev))
