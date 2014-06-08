#! /usr/bin/env python
###############################################################################
##
## sound.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import pygame 

class Sound:
	def __init__(self, soundfile):
		pygame.mixer.init()
		self.sound = pygame.mixer.Sound(soundfile)

	def play(self):
		if pygame.mixer.music.get_busy()==0:
	            self.sound.play()
