# 思路
# 1、拿到页面源代码
# 2、编写正则，获取页面数据
# 3、保存数据
import random
import time
import requests
import re
from bs4 import BeautifulSoup

session = requests.session()

session.url = "https://movie.douban.com/top250"
session.trust_env = False
session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

response = session.get(url=session.url,headers=session.headers,timeout=3)
pageSourse = response.text

# 编写正则表达式   re.S可以让正则中的.匹配换行符
obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>',re.S)
# 进行正则匹配
result = obj.finditer(pageSourse)
for item in result:
     print(item.group("name"))   # 拿结果