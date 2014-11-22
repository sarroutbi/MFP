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
mpl.rcParams['font.size'] = 30.0

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Java', 'C++', 'ANSI-C', 'XML', 'Python'
fracs = [53.63, 19.84, 10.56, 9.16, 5.68]
explode=(0, 0, 0, 0, 0)

patches, texts, autotexts = pie(fracs, explode=explode, labels=labels,
                                autopct='%1.1f%%', shadow=True, startangle=90)

title('Programming Language Distribution', bbox={'facecolor':'0.8', 'pad':5})

show()
