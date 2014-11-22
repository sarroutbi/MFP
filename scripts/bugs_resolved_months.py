#!/usr/bin/python
"""
Horizontal bar chart.
"""
from pylab import *
font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

bugs_resolved = (1, 2, 15, 23, 29, 36, 53, 115, 57, 73, 213, 144, 122, 197, 186, 401, 151)

pos = arange(len(bugs_resolved))+.5    # the bar centers on the y axis
month = ('June 2013',  'July 2013',  'August 2013',  'September 2013' ,
         'October 2013',  'November 2013',  'December 2013',  'January 2014',
         'February 2014',  'March 2014',  'April 2014',  'May 2014',
         'June 2014',  'July 2014',  'August 2014',  'September 2014',
         'October 2014')

colors = ['g','g','g','g','g','g','g','r','g','g','g','g','g','g','g','r','g']

figure(1)
barh(pos, bugs_resolved, align='center', color=colors, alpha=0.7)
yticks(pos, month)
xlabel('Number of Bugs Resolved')
title('Bugs Resolved per month')
grid(True)
show()
