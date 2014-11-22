#!/usr/bin/python
"""
Make a pie chart - see
http://matplotlib.sf.net/matplotlib.pylab.html#-pie for the docstring.

This example shows a basic pie chart with labels optional features,
like autolabeling the percentage, offsetting a slice with "explode",
adding a shadow, and changing the starting angle.

"""
from pylab import *
import pylab as mpl
mpl.rcParams['font.size'] = 25.0

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'vtn', 'controller', 'oscp', 'opendove', 'yangtools',\
         'defense4all', 'bgpcep', 'openflowplugin', 'sdninterfaceapp', '(rest of projects)'
fracs = [37.51, 16.40, 8.08, 5.65, 4.69,
         3.34, 3.14, 2.67, 2.11, 17.40]

explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red',
          'blue', 'green', 'brown', 'grey', 'orange']

patches, texts, autotexts = pie(fracs, explode=explode, labels=labels, colors=colors,
                                autopct='%1.1f%%', shadow=True, startangle=90)

title('Project LOC Distribution', bbox={'facecolor':'0.8', 'pad':4})

show()
