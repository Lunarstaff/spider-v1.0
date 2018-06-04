import requests
url_JD_First = "https://www.jd.com/"
try:
    r = requests.get(url_JD_First)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("访问异常，爬取失败！")