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
mpl.rcParams['font.size'] = 20.0

# make a square figure and axes
figure(2, figsize=(5,5))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Resolved', 'Verified', 'Waiting for \nReview', 'In Progress', 'Confirmed'
fracs = [75.08, 2.58, 2.12, 1.10, 19.12]

explode=(0, 0, 0, 0, 0)
colors = ['red', 'blue', 'green', 'orange', 'gold',]

patches, texts, autotexts = pie(fracs, explode=explode, labels=labels, colors=colors,
                                autopct='%1.1f%%', shadow=True, startangle=90)

title('Bug Status Distribution', bbox={'facecolor':'0.8', 'pad':4})

show()
