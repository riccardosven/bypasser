#! /usr/bin/env python
###############################################################################
##
## graphsave.py -- part of the bypasser program
##
## Copyright (c) 2014 Riccardo Sven Risuleo 
##
## This software may be modified and distributed under the terms
## of the MIT license.  See the LICENSE file for details.
##
###############################################################################

import matplotlib.pyplot as plt
import datetime

class Graphsave:

    PLOT_WIDTH = 1
    PLOT_HEIGHT = 500
    def __init__(self,folder_name):
        self.folder = folder_name
    
    def save(self,x,y,slope,intercept):
        self.fig = plt.figure()
        self.axis = self.fig.add_subplot(111)
        self.line = self.axis.plot(x,y)

        self.regressionline = self.axis.plot([0,self.PLOT_WIDTH], [intercept,self.PLOT_WIDTH*slope + intercept])
        plt.xlim((0,self.PLOT_WIDTH))
        plt.ylim((0,self.PLOT_HEIGHT))

        self.fig.canvas.draw()
        self.fig.savefig(self.folder+'/'+str(datetime.datetime.now())+'_plot.jpg')
        plt.close(self.fig)
