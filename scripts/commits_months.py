#!/usr/bin/python
"""
Horizontal bar chart.
"""
from pylab import *
font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

commits = ( 143,  258,  328,  520,  717,  1065,  805,
            1360,  530,  330,  587,  915,  944,  1195,
            1180,  1306)
pos = arange(len(commits))+.5    # the bar centers on the y axis
month = ('June 2013',  'July 2013',  'August 2013',  'September 2013' ,
         'October 2013',  'November 2013',  'December 2013',  'January 2014',
         'February 2014',  'March 2014',  'April 2014',  'May 2014',
         'June 2014',  'July 2014',  'August 2014',  'September 2014')

colors = ['b','b','b','b','b','b','b','r','b','b','b','b','b','b','b','r']

figure(1)
barh(pos, commits, align='center', color=colors, alpha=0.7)
yticks(pos, month)
xlabel('Number of Commits')
title('Commits per month')
grid(True)
show()
