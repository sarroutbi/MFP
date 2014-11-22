#!/usr/bin/python
"""
Horizontal bar chart.
"""
from pylab import *
font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

questions = ( 51, 39, 32, 47, 65, 69 )
pos = arange(len(questions))+.5    # the bar centers on the y axis
month = ('May 2014', 'June 2014',  'July 2014',  'August 2014',  'September 2014',
         'October 2014')

colors = ['y','y','y','y','r','y']

figure(1)
barh(pos, questions, align='center', color=colors, alpha=0.7)
yticks(pos, month)
xlabel('Number of Questions')
title('Questions per month')
grid(True)
show()
