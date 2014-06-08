#! /usr/bin/env python
###############################################################################
##
## graph_test.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

from utilities.graph import Graph
from numpy.random import uniform

data = uniform(0,500,100) 

plt = Graph('.')

plt.saveplot(range(100),data,5,500)

