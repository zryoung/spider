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

	def writeFps(self,ProblemCount=10):
		pass

	
		
