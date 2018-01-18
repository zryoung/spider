#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-17 15:58:28
# @Author  : zry (riyang@qq.com)
# @Link    : ${link}
# @Version : $Id$

'''
get problem from loj		https://loj.ac
problem list url:			https://loj.ac/problems
problem page url:			https://loj.ac/problem/{pid}
problem test data url:		https://loj.ac/problem/{pid}/testdata
problem additional_file url:https://loj.ac/problem/{pid}/additional_file
'''

import re
from urllib import request
import base64
from bs4 import BeautifulSoup
#from io import StringIO
import requests


class Problem(object):
    """docstring for Problem"""

    def __init__(self):
        pass
        # self.title = ''
        # self.description = ''
        # self.inputFormat = ''
        # self.outputFormat = ''
        # self.sample = []
        # self.dataRange = ''
        # self.hint = ''
        # self.tag = []
        # self.source = ''
        # self.workPath = ''
        # self.session = requests.Session()


def write_fps(ProblemCount=10):
    pass


def get_image_to_base64(url):
    '''get image and change to base64,from url'''
    base64_data = 'data:image/png;base64,' + \
        base64.b64encode(request.urlopen(url).read()).decode('utf-8')
    return base64_data


def get_problem_id_list():
    '''get problem IDs list from page's url
       TODO:use argument 'url' '''
    page = 1
    problemlist = []
    reg = '<a style="vertical-align: middle; " href="/problem/([0-9]+)">'
    com = re.compile(reg)
    while page <= 7:
        response = session.get("https://loj.ac/problems?page=" + str(page))
        if response.status_code == 200:
            problemlist += re.findall(com, page)
            page += 1
        else:
            print("ERROR")
    return problemlist


def get_page(url):
    try:
        # url="https://loj.ac/problem/"+str(problemid)
        page = session.get(url)
    except Exception as e:
        print(e)


def get_data(url):
    '''get test data from url'''
    data = request.urlopen(url).read().decode('utf-8')
    return data


def get_test_info(url):
    '''get test cases' info from url
    return list like [[a1.in,a1.out]]'''
    page = request.urlopen(url).read()

    soup = BeautifulSoup(page, 'lxml')
    table = soup.find('table', class_='ui celled table')
    trow = table.findAll('tr')
    test_info = []
    for row in trow[1:]:
        col = row.findAll('td')
        inf = col[0].getText()
        outf = col[1].getText()
        test_info.append([inf, outf])
    return test_info

def get_problem(url):
    '''get problem from url'''
    p=Problem()

    page=request.urlopen(url).read()
    soup=BeautifulSoup(page,'lxml')
    # get title
    title=soup.find_all('h1',class_='ui header')
    title=re.sub(r'#\d*?\.','',title[0].text).strip()
    # get info
    info=soup.find_all('span',class_='ui label')
    memory_limit=re.search(u'\d+',info[0].text)
    print(memory_limit.group(0))
    print(info[0].text)


get_problem('https://loj.ac/problem/502')
# print(p.getImageToBase64("https://ooo.0o0.ooo/2017/06/10/593bcc13da98c.png"))
# print(get_test_info('https://loj.ac/problem/506/testdata'))
# p.getData('https://loj.ac/problem/506/testdata/download/a1.in')
