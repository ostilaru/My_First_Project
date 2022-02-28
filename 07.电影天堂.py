"""
1、提取到主页面中的每一个电影背后的那个url地址
    1.拿到“2022必看热片”那一块的html代码
    2.从刚才拿到的html代码中提取到herf代码
2、访问子页面，提取到的电影的名称以及下载地址
    1.拿到子页面的页面源代码
    2.提取数据
"""
import requests
import re

session = requests.session()

session.url = "https://www.dy2018.com/"
session.proxies = {
    'http':None,
    'https':None,
}
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
session.trust_env = False

response = session.get(url=session.url,proxies=session.proxies,timeout=5)
response.encoding = 'gbk'
#print(response.text)

# 1、提取2022必看热片部分的HTML代码
obj1 = re.compile(r'2022必看热片.*?<ul>(?P<html>.*?)</ul>',re.S)
result1 = obj1.search(response.text)
html = result1.group("html")
# print(html)

# 2、提取a标签中的herf的值
obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title")
result2 = obj2.finditer(html)

obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<movie>.*?)<br />.*? <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

for item in result2:
    # print(item.group("href"))
    # 拼接出子页面的url
    child_url = session.url.strip("/") + item.group("href")
    child_response = session.get(child_url)
    child_response.encoding = "gbk"
    # print(child_response.text)
    result3 = obj3.search(child_response.text)
    moive = result3.group("movie")
    download = result3.group("download")
    print(moive,download)
    

