#!/user/bin/python
# -*- coding:utf-8 -*-
# Scopus-test.py
# 获取大学排名信息

"""
http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html

功能描述：
    输入：大学排名URL
    输出：大学排名信息的输出（排名，大学名称，地区，总分）
技术路径：requests-bs4
定向爬虫：仅对输入URL进爬取，不扩展爬取其他URL。

步骤1：从网络上获取大学排名网页内容
    getHTMLText()
步骤2：提取网页内容中信息到合适的数据结构
    fillUnivList()
步骤3：利用数据结构展示并输出结果
    printUnivList()

format 方法回顾：【:<><><>,<>,<>】

"""

import requests
import bs4

# 步骤1：从网络上获取大学排名网页内容
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 步骤2：提取网页内容中信息到合适的数据结构
def fillUnivList(ulist,html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            td_trs = []
            for td in tr:
                td_trs.append(td)
            ulist.append([td_trs[0].string, td_trs[1].div.string, td_trs[2].string, td_trs[3].string])

# 步骤3：利用数据结构展示并输出结果
def printUnivList(ulist,num):
    print("{:^10}\t{:^10}\t{:^10}\t{:^10}".format("排名", "学校名称", "地区", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^10}\t{:^10}\t{:^10}".format(u[0], u[1], u[2], u[3]))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 50)    # 打印20个

# 执行
main()

