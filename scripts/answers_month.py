#!/usr/bin/python
"""
Horizontal bar chart.
"""
from pylab import *
font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

answers = ( 51, 33, 31, 48, 54, 51 )
pos = arange(len(answers))+.5    # the bar centers on the y axis
month = ('May 2014', 'June 2014',  'July 2014',  'August 2014',  'September 2014',
         'October 2014')

colors = ['c','c','c','c','r','c']

figure(1)
barh(pos, answers, align='center', color=colors, alpha=0.7)
yticks(pos, month)
xlabel('Number of Answers')
title('Answers per month')
grid(True)
show()
