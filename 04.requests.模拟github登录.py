import requests
import json
import re

# url = 'https://api.github.com/events'
# proxies = {
#     "https":"https://185.238.239.55:8090",
#     "http":"http://185.238.239.55:8090"
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
# }
# response = requests.get(url, auth = ('user','pass'), headers = headers, proxies=proxies)
# print(response.status_code)

def login():
    # session
    session = requests.session()

    # headers
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
     }
    session.proxies = {
        "https": None,
        "http":None
    }
    session.trust_env = False
    # url1-获取token
    url1 = 'https://github.com/login'
    # 发送请求获取响应
    response_1 = session.get(url1).content.decode()
    # 正则提取
    'name="authenticity_token" value="(.*?)" />'
    token = re.findall('name="authenticity_token" value="(.*?)" />', response_1)[0]
    print(token)

    # url2-登录
    url2 = "https://github.com/session"
    # 构建表单数据
    data = {
        'commit': 'Sign in',
        'authenticity_token': 'QEYx - Wr_lbw29GhFlBxTPcxv8sIi7wY - nYif0J1bK2a - FaT8_wPF8CAyCtpEwXfwIWp4 - c2vmhjX_KIVAzc4JQ',
        'login': '543498711@qq.com',
        'password': 'jl20020426',
        'trusted_device': '',
        'webauthn - support': 'supported',
        'webauthn - iuvpaa - support': 'supported',
        'return_to': 'https: // github.com / login',
        'allow_signup': '',
        'client_id': '',
        'integration': '',
        'required_field_7d5b': '',
        'timestamp': '1646020865425',
        'timestamp_secret': '7e61bb3b1dc95125bf332e63c47efe3fc676668127b59c378ac3549be5c54b40',
    }
    #print(data)
    # 发送请求登录
    session.post(url2,data=data)
    # url3-验证
    url3 = "https://github.com/ostilaru"
    response = session.get(url3)
    with open('github.html','wb') as fp:
        fp.write(response.content)

if __name__ == "__main__":
    login()