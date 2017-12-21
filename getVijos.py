#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 15:04:11
# @Author  : zry (riyang@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os

tagdic={'title':'title.txt',\
#'time_limit':'time_limit unit="s"',\
#'memory_limit':'memory_limit unit="mb"',\
'description':'Description.txt',\
#'img':'img',\
'input':'InputFormat.txt',\
'output':'OutputFormat.txt',\
'sample_input':'SampleInput.txt',\
'sample_output':'SampleOutput.txt',\
#{'test_input'},\
#{'test_output'},\
'hint':'Hint.txt',\
'source':'Source.txt'
}
xml='''
<?xml version="1.0" encoding="UTF-8"?>
<fps version="1.2" url="https://github.com/zhblue/freeproblemset/">
	<generator name="HUSTOJ" url="https://github.com/zhblue/hustoj/"/>
'''
rootpath=r'e:/work/myoi/vijos/新建文件夹/'
# print(os.listdir(rootpath))
for dirname in os.listdir(rootpath):
	probPath=rootpath+dirname
	# print(probPath)
	if os.path.isdir(probPath):
		probText='<item>'
		fname=os.listdir(probPath)
		for tag in tagdic:
			# print(tag,tagdic[tag])
			fxname=probPath+'/'+tagdic[tag]
			#print(fxname)
			if os.path.exists(fxname):
				ftext=open(fxname,'r').read()
				data='<'+tag+'><![CDATA['+ftext+']]></'+tag+'>'
				print(data)
		infiles=[]
		oufiles=[]
		if os.path.exists(probPath+'/Config.ini'):
			cfgtext=open(probPath+'/Config.ini','r').readlines()			
			#print(cfgtext)
			for i in cfgtext[1:]:
				s=i.split('|')
				infiles.append(s[0])
				oufiles.append(s[1])
		# print(infiles)
		# print(oufiles)
		indatas=[]
		oudatas=[]

		break
