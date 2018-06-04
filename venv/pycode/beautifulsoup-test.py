"""
BeatifulSoup
库解析器：

bs4的HTML解析器 BeautifulSoup(mk,"html.parser") 安装sb4
lxml的HTML解析器    BeautifulSoup(mk,"lxml")    pip install lxml
lxml的XML解析器     BeautifulSoup(mk,"xml")     pip install lxml
html5lib的解析器    BeautifulSoup(mk,"html5lib")    pipinstall html5lib


-BeautifulSoup 类的基本元素：
    Tag             标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
    Name            标签的名字，<p>...</p>的名字是“p”，格式：<tag>.name
    Attribute       标签的属性，字典的形式，格式：<tag>.arrts
    NavigableString 标签内非属性字符串，<>...</>中字符串，格式：<tag>.string
    Comment         标签内字符串的注释部分，一种特殊的Comment类型

C:\\E-Data-File\\腾讯课堂\\Python入门\\spider-v1.0\\venv\\files\\baidu_index.html

>>> import bs4
>>> import requests
>>> baidu_index_url = "http://www.baidu.com/index.html"
>>> baidu_index_html_r = requests.get(baidu_index_url)
>>> baidu_index_html_r.status_code
200
>>> baidu_index_demo = baidu_index_html_r.text
>>> baidu_index_demo
>>> baidu_index_soup =bs4.BeautifulSoup(baidu_index_demo,"html.parser")


实例：提取HTML中所有的URL链接
    思路：
        1）搜索到所有<a>标签
        2）解析<a>标签格式，提取herf的的链接内容

>>> import requests
>>> import bs4
>>> url = "http://www.baidu.com"
>>> r = requests.get(url)
>>> r.status_code
200
>>> baidu_html = r.text
>>> baidu_html.head
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'head'
>>> baidu_soup = bs4.BeautifulSoup(baidu_html,"html.parser")

>>> for link in baidu_soup.find_all('a'):
...     print(link.get("href"))
...
http://news.baidu.com
http://www.hao123.com
http://map.baidu.com
http://v.baidu.com
http://tieba.baidu.com
http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1
//www.baidu.com/more/
http://home.baidu.com
http://ir.baidu.com
http://www.baidu.com/duty/
http://jianyi.baidu.com/


>>> for tag in baidu_soup.find_all(True): #列出所有标签名称
...     print(tag.name)
...
html
head
meta
meta
meta
link
title
body
div
div
div
div
div
div
img
form
input
input
input
input
input
input
span
input
span
input
div
a
a
a
a
a
noscript
a
script
a
div
div
p
a
a
p
a
a
img

>>> import re
>>> for tag in baidu_soup.find_all(re.compile("b")): #列出所有标签名称以b开头的标签
...     print(tag.name)
...
body




<>.find_all(name,attrs,recursive,string,**kvargs)
    name:对标签名称的检索字符串
    attrs:对标签属性值的检索字符串，可标注属性检索
    recursive:是否对子孙全部检索，默认True
    string:<>...</>中字符串区域的检索字符串

<tag>(...) 等价于 <tag>.find_all(...)
soup(...) 等价于 soup.find_all(...)

find_all() 的扩展方法：
<>.find()   搜索且只返回一个结果，字符串类型，同.find_all()参数
<>.find_parents()   在先辈节点中搜索，返回列表类型，同.find_all()参数
<>.find_parent()    在先辈节点返回一个结果，字符串类型，同.find_all()参数
<>.find_next_siblings() 在后续平行节点中搜索，返回列表类型，同.find_all()参数
<>.find_next_sibling()  在后续平行节点中返回一个结果，字符串类型，同.find_all()参数
<>.find_previous_siblings() 在前序平行节点中搜索，返回列表类型，同.find_all()参数
<>.find_previous_sibling()  在前序平行节点中返回一个结果，字符串类型，同.find_all()参数





"""
