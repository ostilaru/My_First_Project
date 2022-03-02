"""
1.提取页面源代码
2.解析页面源代码，提取数据
"""
import requests
from lxml import etree

session = requests.session()
session.url = 'https://bj.58.com/ershoufang/'
session.trust_env = False
session.proxies = {
    'http':None,
    'https':None,
}
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

response = session.get(session.url)
response.encoding = "utf-8"

et = etree.HTML(response.text)
divs = et.xpath("//section[@class='list']/div")
for div in divs:
    # 建造时间
    t = div.xpath("./a/div[2]/div/section/div[1]/p[5]/text()")
    if not t:
        break
    time = t[0].strip()
    # 房屋名称
    n = div.xpath("./a/div[2]/div/div/h3/text()")
    name = n[0]
    # 房屋价格
    p = div.xpath("./a/div[2]/div[2]/p[1]/span/text()")
    total_price = p[0]

    print(name,"--",time,"--",total_price,"w")