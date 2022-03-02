"""
1.拿到页面源代码
2.从页面源代码中提取数据：名称，价格，公司，近半年成交数
"""
import requests
from lxml import etree

session = requests.session()
session.url = 'https://beijing.zbj.com/search/f/?kw=saas'
session.trust_env = False
session.proxies = {
    'http':None,
    'https':None,
}
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

response = session.get(url=session.url, headers=session.headers, proxies=session.proxies)
response.encoding = "utf-8"
# print(response.text)

# 提取数据
et = etree.HTML(response.text)
# new-service-wrap/div
divs = et.xpath("//div[@class='new-service-wrap']/div")
for div in divs:
    # 此时的div就是一条数据，对应一条商品信息
    spans = div.xpath("./div/div/a[2]/div[2]/div/span/text()")
    ps = div.xpath("./div/div/a/div/p/text()")
    company = ps[1].strip()
    price = spans[0]    # 价格
    half_year_nums = spans[1]   # 半年成交数
    print(price, half_year_nums, company)
print("over!")