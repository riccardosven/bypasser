#! /usr/bin/env python
###############################################################################
##
## motiondetector.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from utilities.movingwindow import MovingWindow
from time import time
from scipy import stats
from cv2 import moments
import cv2
import numpy as np

# There is a line in the update method that accounts for the flipped webcam... maybe we should remove it... however it does work.

class MotionDetector():
    """Motion Detector class, gets images and performs a regression"""
    DETECTION_TIME = .7 # Linear regression time
    MOVING_WINDOW_LENGTH = 40 # Number of samples for regression window
    AVERAGE_WINDOW_LENGTH = 20 # Number of samples in moving average window
    MINIMUM_REGRESSION_SAMPLES = 5 # Samples skipped before starting regression
    MEAN_THRESHOLD = 0.3 # Minimum change in image that will trigger detection
    DEVIATION_THRESHOLD = 10 # Maximum deviation from linear behaviour accepted
    Y_THRESHOLD = 90 # Maximum deviation from linear behaviour accepted
    TRIGGER_TIME_THRESHOLD = 5 # Timeout between detection, in seconds
    SPEED_THRESHOLD = 115 # Minimum speed that will trigger detection, in px/sec
    REF_IM_UPDATE_TIME = 3 # time where little change happens until reference image is updated
    REF_IM_WINDOW_LENGTH = 200
    REF_IM_THRESHOLD = 30000
    
    def __init__(self,camera):
        self.regression_window = MovingWindow(self.MOVING_WINDOW_LENGTH) #Start a moving window for the regression
        self.time_change_window = MovingWindow(self.REF_IM_WINDOW_LENGTH)
        self.change_window = np.zeros(self.AVERAGE_WINDOW_LENGTH) # Start the moving average window for the motion detections
        self.last_trigger_time = 0
        self.camera = camera

    def update(self,frame,diff_frame):
        """Update the detection status with a new image"""
        self.gray_frame = np.uint8(np.mean(diff_frame,2))
        self.image_moments = moments(self.gray_frame)

        # Update the moving average window
        self.change_window = np.roll(self.change_window,1)
        self.change_window[0] = self.image_moments['m00']

        self.mom_x =  np.uint(self.image_moments['m10']/(self.image_moments['m00']+1))
        self.mom_y =  np.uint(self.image_moments['m01']/(self.image_moments['m00']+1))

        # Detection window output
        #self.gray_frame[self.mom_y:self.mom_y+5,self.mom_x:self.mom_x+5] = 255
        #cv2.imshow('preview',self.gray_frame)

        # Update the moving regression window with the new measurements
        self.regression_window.push(self.mom_x)
        self.time_change_window.push(self.image_moments['m00'])
        
        # Update regressor variables
        self.t_out,self.p_out,self.n_out = self.regression_window.fetch(self.DETECTION_TIME)
        _,self.change_out,_ = self.time_change_window.fetch(self.REF_IM_UPDATE_TIME)
        if np.max(self.change_out) < self.REF_IM_THRESHOLD:
          self.camera.update_reference_frame(frame)
        print np.max(self.change_out)

        if len(self.t_out) > self.MINIMUM_REGRESSION_SAMPLES:
            self.slope,self.intercept ,_,_,self.std_dev = stats.linregress(self.t_out,self.p_out)

            ############################################################
            ############### Dirty hack! Flipped webcam #################
            ## self.slope = -self.slope 
            ############################################################
            ############################################################

            self.pred_y = self.slope*self.t_out + self.intercept*np.ones(self.t_out.shape)
            self.y_dev = np.sqrt(np.sum((self.p_out-self.pred_y)**2))
            #print(self.y_dev)

    def detection(self):
        """True is a detection has occurred at least TRIGGER_TIME_THRESHOLD ago"""
        if len(self.t_out) >5:
            #if self.change_window.mean() > self.MEAN_THRESHOLD and self.y_dev < self.Y_THRESHOLD and time() - self.last_trigger_time > self.TRIGGER_TIME_THRESHOLD:
            if self.change_window.mean() > self.MEAN_THRESHOLD and self.std_dev < self.DEVIATION_THRESHOLD and time() - self.last_trigger_time > self.TRIGGER_TIME_THRESHOLD:
                if self.slope > self.SPEED_THRESHOLD:
                    self.last_trigger_time = time()
                    return True
        return False

    def data(self):
        """Return regression data"""
        if len(self.t_out) > self.MINIMUM_REGRESSION_SAMPLES:
            return self.slope, self.intercept, self.y_dev, self.std_dev
        else:
            return 0,0,0,0

    def dump(self):
        return self.t_out, self.p_out
