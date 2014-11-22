#!/usr/bin/python
"""
Horizontal bar chart.
"""
from pylab import *
font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

bugs_opened = (3, 6, 27, 34, 35, 56, 80, 134, 
               75, 152, 306, 187, 150, 193, 195, 464, 170)
pos = arange(len(bugs_opened))+.5    # the bar centers on the y axis
month = ('June 2013',  'July 2013',  'August 2013',  'September 2013' ,
         'October 2013',  'November 2013',  'December 2013',  'January 2014',
         'February 2014',  'March 2014',  'April 2014',  'May 2014',
         'June 2014',  'July 2014',  'August 2014',  'September 2014',
         'October 2014')

colors = ['b','b','b','b','b','b','b','r','b','b','b','b','b','b','b','r','b']

figure(1)
barh(pos, bugs_opened, align='center', color=colors, alpha=0.7)
yticks(pos, month)
xlabel('Number of Bugs Opened')
title('Bugs Opened per month')
grid(True)
show()
