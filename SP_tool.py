# Howdy!
# Below are my attempt to scrape data from google finance and build a program that'll provide 
# accurate stock price index flowing to your screen each minute.
# Data is a bit delayed from server, however works like a charm!
# To use: Please add stock codes into the 'stocks' list. 
#


import urllib2 	#This limits the program to Python 2.7
import re
import json
import time

stocks= ['aapl', 'goog', 'nflx']

def fetchMarketPrice(stock):
	link='http://finance.google.com/finance/info?client=ig&q='
	url = link+"%s" % (stock)
	u = urllib2.urlopen(url)
	content = u.read()
	data = json.loads(content[3:])
	info = data[0]
	l = float(info["l_fix"])
	p = float(info["el_cur"])
	t = str(info["elt"])
	return(l,p,t)


while True:
	i=0
	while i<len(stocks):
		print(stocks[i])
		l,p,t = fetchMarketPrice(stocks[i])
		print("%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (t, l, p, p-l,(p/l-1)*100.))
		i+=1
	time.sleep(60)
