#!/usr/bin/python
"""
Horizontal bar chart.
"""
from pylab import *
font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

messages = (1255, 1423, 2523, 4809, 8662, 10807, 8576, 13168, 6612, 4671, 11407, 12605, 14515, 17314, 18745, 18823)

pos = arange(len(messages))+.5    # the bar centers on the y axis
month = ('June 2013',  'July 2013',  'August 2013',  'September 2013' ,
         'October 2013',  'November 2013',  'December 2013',  'January 2014',
         'February 2014',  'March 2014',  'April 2014',  'May 2014',
         'June 2014',  'July 2014',  'August 2014',  'September 2014')

colors = ['g','g','g','g','g','g','g','r','g','g','g','g','g','g','g','r']

figure(1)
barh(pos, messages, align='center', color=colors, alpha=0.7)
yticks(pos, month)
xlabel('Number of Mail Messages')
title('Messages per month')
grid(True)
show()
