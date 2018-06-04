"""
IP138查询IP归属地
http://www.ip138.com

查询接口：
http://m.ip138.com/ip.asp?ip=ipaddress
"""
import requests
ip138_url = "http://m.ip138.com/ip.asp?ip="
ipaddress = "163.177.151.109"
try:
    r = requests.get(ip138_url + ipaddress)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("访问失败！")