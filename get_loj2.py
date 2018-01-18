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
from PIL import Image
#from io import StringIO
import io
from urllib import request
import base64

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

	def getImageToBase64(self,url):
		base64_data='data:image/png;base64,'+base64.b64encode(request.urlopen(url).read()).decode('utf-8')
		return(base64_data)

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
		return(problemlist)

	def getpage(self,url):
		try:
			#url="https://loj.ac/problem/"+str(problemid)
			page=session.get(url)
		except Exception as e:
			print(e)

		# def getImageToBase64(self,url):
		# 	file=cStringIO.StringIO(urllib2.urlopen(url).read())
		# 	img=Image.open(file)
		# 	base64_data=base64.b64encode(img)
		# 	return(base64_data)

p=Problem()
print(p.getImageToBase64("https://ooo.0o0.ooo/2017/06/10/593bcc13da98c.png"))