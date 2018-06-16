"""
目标：获取上交所和深交所所有股票的名称和交易信息
输出：保存到文件中
技术路线：requests-bs4-re

百度股票-股市通
https://gupiao.baidu.com/
新浪股票
http://finance.sina.com.cn/stock/

候选数据网站的选择
选择原则：静态的保存在HTML中，且没有Robots协议限制

选取方法：浏览器F12，源代码查看等方法确认。
不要纠结于某个网点，多找信息源尝试

步骤1：从东方财富网获取购票列表
步骤2：根据股票列表逐个到百度股票获取个肌信息


"""

import requests
import bs4
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = bs4.BeautifulSoup(html, "html.parser")
    a = soup.find_all("a")
    for i in a:
        try:
            href = i.attrs["href"]
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = bs4.BeautifulSoup(html, "html.parser")
            stockInfo = soup.find("div", attrs={"class":"stock-bets"})

            name = stockInfo.find_all(attrs={"class":"bets-name"})[0]
            infoDict.update({"股票名称": name.text.split()[0]})

            keyList = stockInfo.find_all("dt")
            valueList = stockInfo.find_all("dd")
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, "a", encoding="utf-8") as f:
                f.write(str(infoDict) + "\n")
                count = count + 1
                print("\r当前进度：{:.2f}%".format(count*100/len(lst)), end="")
        except:
            count = count + 1
            print("\r当前进度：{:.2f}%".format(count * 100 / len(lst)), end="")
            traceback.print_exc()
            continue

def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "C:\\E-Data-File\\腾讯课堂\\Python入门\\spider-v1.0\\venv\\files\\baiduStockInfo.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()

