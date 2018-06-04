"""
百度的关键词接口：
http://www.baidu.com/s?wd=keyword

360的关键词接口：
http://www.so.com/s?q=keyword

>>> import requests
>>> kv = {'wd':'Python'}
>>> url_baidu_kw = "http://www.baidu.com/s"
>>> r_kv = requests.get(url_baidu_kw,params = kv)
>>> r_kv.status_code
200
>>> r_kv.request.url
'http://www.baidu.com/s?wd=Python'
>>> len(r_kv.text)
318170
"""

import requests
keyword = "Python"
url_baidu_kw = "http://www.baidu.com/s"
try:
    kv = {"wd": keyword}
    r = requests.get(url_baidu_kw, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("访问失败")