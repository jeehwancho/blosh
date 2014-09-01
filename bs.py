#todo
#learn pandas

#http://pandas.pydata.org/pandas-docs/stable/tutorials.html
#OLS regression: http://stackoverflow.com/questions/19991445/run-an-ols-regression-with-pandas-data-frame
#Time series (old example): http://nbviewer.ipython.org/github/changhiskhan/talks/blob/master/pydata2012/pandas_timeseries.ipynb
#How to get stock data and plot: http://pythonio.com/blog/2013/01/07/python-time-series-showing-stock-price-trading-volume/

#http://pandas.pydata.org/pandas-docs/stable/api.html
#to append: close_px.loc[pd.Timestamp('2012-06-30 00:00:00')] = 300

#feature:
# 1. deviation from average curve
# 2. high/low in a one-month window

#download
#http://ichart.finance.yahoo.com/table.csv?s=YHOO&d=0&e=28&f=2010&g=d&a=3&b=12&c=1996&ignore=.csv
#sn = TICKER
# a = fromMonth-1
# b = fromDay (two digits)
# c = fromYear
# d = toMonth-1
# e = toDay (two digits)
# f = toYear
# g = d for day, m for month, y for yearly

import csv
import calendar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import urllib
import os

class BuyLow(object):
	
	# testData - a list of tuple (date in str, price in float)
	def __init__ (self):
		self.test = 0
		self.testData = []

	# def __init__ (self, fileName):
	# 	self.test = 0
	# 	self.testData = []
	# 	self.df = pd.read_csv(fileName, index_col='date', parse_dates=True)
	# 	self.close_px = self.df['close']
	# 	self.close_px = self.close_px.sort_index (ascending=True)

	def IsReadyToBuy (self):
		print("self.test: %d" % self.test)
		return False

	def PrintTestData (self):
		# for (date, price) in self.testData:
		# 	print ("date: %s price: %f" % (date, price))
		df = pd.read_csv("GOOGL_history.csv", index_col='date', parse_dates=True)
		print df.head()
		#get the closing price
		close_px = df['close']
		close_px.loc[pd.Timestamp('2012-06-30 00:00:00')] = 300
		# print close_px[pd.Timestamp('2014-08-18 00:00:00')]
		print close_px.head()
		#reverse index
		close_px = close_px.sort_index (ascending=True)
		print close_px.head()
		close_px.plot(label='Close')
		mavg = pd.rolling_mean(close_px, 40)
		mavg.plot(label='mavg')
		print mavg.tail()
		print close_px.tail()
		print close_px.loc[pd.Timestamp(time.strftime("%Y-%m-%d") + " 00:00:00")]
		print pd.Timestamp(time.strftime("%Y-%m-%d") + " 00:00:00")
		# plt.legend()
		# plt.show()

	def Test (self):
		urllib.urlretrieve ("http://ichart.finance.yahoo.com/table.csv?s=YHOO&d=0&e=28&f=2010&g=d&a=3&b=12&c=1996&ignore=.csv", "blah.csv")
		df = pd.read_csv("blah.csv", index_col='Date', parse_dates=True)
		print df.head()
		try:
			os.remove("blah.csv")
		except OSError:
			pass

	# returns score of current state
	# the higher score, the better chance to buy!
	# higher score means it's local minimum
	def Evaluate (self):
		return self.FeaturePredictedPrice () + self.Feature2 (price)

	# Feature: difference from predicted price as of now!
	# compare predicted price and the actual price
	def FeaturePredictedPrice (self):
		mavg = pd.rolling_mean(self.close_px, 40)
		return 0

	def Feature2 (self, price):
		return 0
