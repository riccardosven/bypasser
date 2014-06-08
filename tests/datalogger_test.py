#! /usr/bin/env python
###############################################################################
##
## datalogger_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from utilities.datalogger import Datalogger

log = Datalogger('log.txt')

log.update((1,2,3,4),True) # iscow!
log.update((5,6,7,8),False) # iscow!

