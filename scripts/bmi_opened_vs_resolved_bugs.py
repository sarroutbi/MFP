#!/usr/bin/python
"""
Graph chart.
"""
from pylab import *
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

font = {'weight' : 'bold',
        'size'   : 18}

matplotlib.rc('font', **font)

bugs_resolved = (1.00, 2.00, 15.00, 23.00, 29.00, 36.00, 53.00, 115.00,
                 57.00, 73.00, 213.00, 144.00, 122.00, 197.00, 186.00, 401.00, 151.00)
bugs_opened = (3.00, 6.00, 27.00, 34.00, 35.00, 56.00, 80.00, 134.00, 
               75.00, 152.00, 306.00, 187.00, 150.00, 193.00, 195.00, 464.00, 170.00)
bmi = []

bmi_test = [15.00, 12.00]

month_dates = ['06/2013', '07/2013', '08/2013', '09/2013', '10/2013', 
               '11/2013', '12/2013', '01/2014', '02/2014', '03/2014',
               '04/2014', '05/2014', '06/2014', '07/2014', '08/2014',
               '09/2014', '10/2014']

month = ('June 2013',  'July 2013',  'August 2013',  'September 2013' ,
         'October 2013',  'November 2013',  'December 2013',  'January 2014',
         'February 2014',  'March 2014',  'April 2014',  'May 2014',
         'June 2014',  'July 2014',  'August 2014',  'September 2014',
         'October 2014')

counter = 0
for elem in bugs_resolved:
    bmi_index = (elem / bugs_opened[counter]) * 100
    print "Adding resolved:%f opened:%f bmi:%f" % (elem, bugs_opened[counter], bmi_index)
    bmi.insert(counter, bmi_index)
    counter += 1

print "BMI:", bmi
print "Months:", month

x = [dt.datetime.strptime(d,'%m/%Y').date() for d in month_dates]
y = bmi

colors = ['g','g','g','g','g','g','g','r','g','g','g','g','g','g','g','r','g']

figure(1)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(x, month_dates, rotation='vertical')
plt.plot(x, y)
title('BMI [(Resolved/Opened)*100]')
grid(True)
show()
