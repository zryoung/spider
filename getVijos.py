#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-21 15:04:11
# @Author  : zry (riyang@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import codecs

tagdic={#'title':'title.txt',\
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
xml='''<?xml version="1.0" encoding="UTF-8"?>
<fps version="1.2" url="https://github.com/zhblue/freeproblemset/">
	<generator name="HUSTOJ" url="https://github.com/zhblue/hustoj/"/>
'''
rootpath='E:/OI/vijos_spider/'
pNum=0

xmlfile=''
endflag=False
#print(os.listdir(rootpath))
for dirname in os.listdir(rootpath):
	probPath=rootpath+dirname
	#print(probPath)
	if os.path.isdir(probPath):
		
		if pNum%20==0:
			xmlfile=codecs.open(rootpath+'/fps_'+dirname+'_20.xml','w','utf-8')
			xmlfile.write(xml)
			endflag=False
		# xml+='<item>'
		# xml+='<title><![CDATA['+dirname+']]></title>'
		xmlfile.write('<item>')
		xmlfile.write('<title><![CDATA[vijos_'+dirname+']]></title>')
		xmlfile.write('<time_limit unit="s"><![CDATA[1]]></time_limit>')
		xmlfile.write('<memory_limit unit="mb"><![CDATA[256]]></memory_limit>')
		fname=os.listdir(probPath)
		for tag in tagdic:
			# print(tag,tagdic[tag])
			fxname=probPath+'/'+tagdic[tag]
			#print(fxname)
			if os.path.exists(fxname):
				ftext=open(fxname,'r').read()
				# xml+='<'+tag+'><![CDATA['+ftext+']]></'+tag+'>'
				xmlfile.write('<'+tag+'><![CDATA['+ftext+']]></'+tag+'>')
				#print(data)
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
		for f in infiles:
			dtxt=open(probPath+'/Input/'+f,'r').read()
			indatas.append(dtxt)
		for f in oufiles:
			dtxt=open(probPath+'/Output/'+f,'r').read()
			oudatas.append(dtxt)
		for i in range(len(indatas)):
			xmlfile.write('<test_input><![CDATA['+indatas[i]+']]></test_input>')
			xmlfile.write('<test_output><![CDATA['+oudatas[i]+']]></test_output>')
			# xml+='<test_input><![CDATA['+indatas[i]+']]></test_input>'
			# xml+='<test_output><![CDATA['+oudatas[i]+']]></test_output>'
		# xml+='</item>'
		xmlfile.write('</item>')
		if pNum%20==19:
			xmlfile.write('</fps>')
			xmlfile.close()
			endflag=True
		pNum+=1
# xml+='</fps>'
if not endflag:
	xmlfile.write('</fps>')
	xmlfile.close()
	endflag=True
