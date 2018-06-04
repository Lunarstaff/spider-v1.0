# newsToPNG.py
import requests as rqt
import re

Tencent_new_url = "http://news.qq.com/"
Tencent_new_html = ".\\..\\files\\Tencent_news.html"

def getHTML(url,path_f): # 把url返回的text保存在 path 的文件中
    r = rqt.get(url)   # 获取响应
    # r.raise_for_status() #如果状态不是200，引发HTTPError异常
    r.encoding = r.apparent_encoding    # 响应报文的编码
    path_fo = open(path_f,"wt",encoding=r.encoding) # 打开或新建path_f文件
    path_fo.seek(0)
    path_fo.write(r.text)   # 写入文件
    path_fo.close() # 关闭文件
    print("已将{}的text写入到{}中！".format(url,path_f))

getHTML(Tencent_new_url,Tencent_new_html)