#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-17 15:58:28
# @Author  : zry (riyang@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import re
import sys
from bs4 import BeautifulSoup

class Problem(object):
	"""docstring for Problem"""
	def __init__(self):
		self.title=''
		self.description=''
		self.inputFormat=''
		self.outputFormat=''
		self.sample=[]
		self.dataRange=''
		self.hint=''
		self.tag=[]
		self.source=''
		self.workPath=''
		self.session=requests.Session()

	def writeFps(self,ProblemCount=10):
		pass

	def getProblemID(self):
		page=1
		problemlist=[]
		reg = '<a style="vertical-align: middle; " href="/problem/([0-9]+)">'
		com = re.compile(reg)
		while page<=7:
			response=session.get("https://loj.ac/problems?page="+str(page))
			if response.status_code==200:
				problemlist+=re.findall(com,page)
				page+=1
			else:
				print("ERROR")

	def getpage(self,url):
		try:
			#url="https://loj.ac/problem/"+str(problemid)
			page=session.get(url)

			

