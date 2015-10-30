#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib,urllib2,re 

for i in range(471):
# for i in range(1):
	url = "http://www.qiubaichengnian.com/index_"+str(i+1)+".html"
	content = urllib.urlopen(url).read()
	soup = BeautifulSoup(content)
	# print content
	result = soup.find_all('img')
	for pic in result:
		# print pic
		if str(pic).find("alt")!=-1:
			try:
				# print pic
				print pic["src"]
			except Exception, e:
				print "error : ", pic
				pass
			else:
				pass
			finally:
				pass
			
