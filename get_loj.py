#TODO: get image,markdown 
import requests
import re
import sys
from bs4 import BeautifulSoup

session = requests.Session()

def getproblemid(page):
    reg = '<a style="vertical-align: middle; " href="/problem/([0-9]+)">'
    com = re.compile(reg)
    return re.findall(com, page)

page = 1
problemlist = []
print('开始抓取数据，请稍候！')
while page<=7:
    response = session.get("https://loj.ac/problems?page=" + str(page))
    if response.status_code == 200:
        problemlist += getproblemid(response.text)
        page+=1
        #print(page)
    else:
        break

for each in problemlist:
    page = session.get("https://loj.ac/problem/" + str(each))
    data = session.get("https://loj.ac/problem/" + str(each) + "/testdata/download")
    #print(data)
    with open(str(each) + ".zip", "wb") as code:
        code.write(data.content)
    soup = BeautifulSoup(page.text, "lxml")
    title=soup.find_all("h1",class_="ui header")
    p=re.compile(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+')#去除特殊字符
    #filename="".join(title[0].text.split())
    filename=re.sub(p,'',title[0].text)
    #print(filename)
    #break
    info=soup.find_all("span",class_="ui label")#获取内存限制等信息
    p_tag=re.compile(r'ui medium \w* label')
    tag=soup.find_all("a",attrs={"class":p_tag})
    #print(tag)
    #break
    ti = soup.find_all("h4", class_="ui top attached block header")#获取题头，如“题目描述”
    an = soup.find_all("div", class_="ui bottom attached segment font-content")#获取内容
    try:
        with open(filename+".txt", "w", encoding="utf-8") as text:
            text.write("TAG:\n")
            for k in range(len((tag))):
                text.write(tag[k].text)
            text.write("\n")
            for j in range(len(info)):
                text.write(info[j].text)
            text.write("\n")
            for i in range(len(ti)):
                text.write(ti[i].text + " : " + an[i].text)
                #print(an[i])
    except :
        print(sys.exc_info()[0])
    #break
