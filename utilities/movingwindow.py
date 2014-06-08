#! /usr/bin/env python
###############################################################################
##
## movingwindow.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from time import time
from numpy import zeros, roll, nonzero

class MovingWindow:
	"""Class implementing a rolling timestamp data structure"""
	def __init__(self, window_length):
		"""Start a moving window with N data points"""
		self.position = zeros(window_length)
		self.timestamp = zeros(window_length)

	def push(self,data):
		"""Push the data to the moving window"""
		self.position = roll(self.position,1)
		self.position[0] = data
		self.timestamp = roll(self.timestamp,1)
		self.timestamp[0] = time()

	def fetch(self,timespan):
		"""Fetch the data that are at most timespan old"""
		basetime = time()
		out_indices = nonzero(self.timestamp > basetime - timespan)
		return basetime - self.timestamp[out_indices], self.position[out_indices], len(out_indices)


