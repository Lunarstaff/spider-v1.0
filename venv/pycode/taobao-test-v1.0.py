"""
目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格

理解：
    -淘宝的搜索接口
    -翻页处理

技术：
    requests + re

起始页：
https://s.taobao.com/search?q=键盘
&imgfile=
&commend=all
&ssid=s5-e
&search_type=item
&sourceId=tb.index
&spm=a21bo.2017.201856-taobao-item.1
&ie=utf8
&initiative_id=tbindexz_20170306

第2页：
https://s.taobao.com/search?q=键盘
&imgfile=
&commend=all
&ssid=s5-e
&search_type=item
&sourceId=tb.index
&spm=a21bo.2017.201856-taobao-item.1
&ie=utf8
&initiative_id=tbindexz_20170306
&bcoffset=4
&p4ppushleft=%2C48&s=44
&ntoffset=4

第3页：
https://s.taobao.com/search?q=键盘
&imgfile=
&commend=all
&ssid=s5-e&search_type=item
&sourceId=tb.index
&spm=a21bo.2017.201856-taobao-item.1
&ie=utf8
&initiative_id=tbindexz_20170306
&bcoffset=4
&p4ppushleft=%2C48
&s=88
&ntoffset=4

user-agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36

步骤：
-1：提交商品搜索请求，循环获取页面
-2：对于每个页面，提取商品名称和价格信息
-3：将信息输出到屏幕上



"""

import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30, )
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parserPage(ilt, html):
    """
    "view_price":"115.00"
    "raw_title":"黑爵机械战警游戏机械键盘青轴黑轴红轴茶轴有线吃鸡电脑台式电竞"
    :param ilt:
    :param html:
    :return:
    """
    try:
        plt = re.findall(r'\"view_price\":\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        for i in range(len(plt)):
            price  = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price, title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:8}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = "键盘"
    depth = 2 # 爬取深度
    start_url = "https://s.taobao.com/search?q=" + goods
    # url示例：https://s.taobao.com/search?q=键盘
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*i)
            # url示例：第2页
            html = getHTMLText(url)
            parserPage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()