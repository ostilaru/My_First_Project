import requests
from bs4 import BeautifulSoup

session = requests.session()
domain = "https://umei.net"
"""
    注意，
        子页面的url如果开头是/，直接在前面拼接上域名即可（绝对路径）
        子页面的url开头不是/，此时需要找到主页面的url，去掉最后一个/后面的所有内容，和当前所获取的url拼接（相对路径）
"""
session.url = 'https://umei.net/bizhitupian/xiaoqingxinbizhi/'
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

page = BeautifulSoup(response.text, "html.parser")
a_list = page.find_all("a", attrs={"class":"TypeBigPics"})
n = 1
for a in a_list:
    href = a.get("href")
    child_href = domain + href
    # print(child_href)
    child_respose = session.get(child_href)
    child_respose.encoding = "utf-8"
    # print(child_respose.text)
    child_bs = BeautifulSoup(child_respose.text, "html.parser")
    img = child_bs.find("img").get("src")
    # print(img)
    # 下载图片
    img_response = session.get(img)
    with open(f"./壁纸图片{n}.jpg",'wb') as fp: # 注意，此时写入文件的是字节，所以是wb
        fp.write(img_response.content)
    print(f"第{n}张图片下载完毕")
    n += 1