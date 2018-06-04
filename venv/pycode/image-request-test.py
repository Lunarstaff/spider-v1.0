"""
网络图片链接的格式：
http://www.example.com/picture.jpg
国家地埋：
http://www.nationalgeographic.com.cn/
选择一个图片Web页面：
http://bizhi.zhuoku.com/wall/200612/1210/jimizuopin/jimi005.jpg
C:\\E-Data-File\\腾讯课堂\\Python入门\\spider-v1.0\\venv\\files\\jimi001.jpg

# 定义图片保存的位置
>>> path = "C:\\E-Data-File\\腾讯课堂\\Python入门\\spider-v1.0\\venv\\files\\jimi006.jpg"
>>> url_jimi = "http://bizhi.zhuoku.com/wall/200612/1210/jimizuopin/jimi006.jpg"
>>> r_jimi = requests.get(url_jimi)
>>> r_jimi.status_code
200
>>> with open(path, "wb") as f:
...     f.write(r_jimi.content)
...
20261
>>> f.close()
"""

import requests
import os
url_jimi = "http://bizhi.zhuoku.com/wall/200612/1210/jimizuopin/jimi006.jpg"
root = "C:\\E-Data-File\\腾讯课堂\\Python入门\\spider-v1.0\\venv\\files\\"
path = root + url_jimi.split("/")[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url_jimi)
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()
            print("{}保存成功！".format(url_jimi.split("/")[-1]))
    else:
        print("文件已存在！")
except:
    print("访问失败！")
