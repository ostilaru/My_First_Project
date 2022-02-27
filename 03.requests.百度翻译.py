# 需求:破解百度翻译
# -post请求（携带了参数）
# 响应数据是一组json数据

import requests
import json

class King(object):
    def __init__(self, word):
        self.url = 'http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=37218aa29f55fdcc'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        self.data = {
            'from': 'zh',
            'to': 'en',
            'q': word
        }

    def get_data(self):
        response = requests.post(self.url,data=self.data,headers=self.headers)
        return response.content

    def parse_data(self, data):
        dic_data = json.loads(data)
        print(dic_data['content']['out'])


    def run(self):
        response = self.get_data()
        self.parse_data(response)

if __name__ == '__main__':
    word = input("请输入你想要翻译的单词或句子: ")
    king = King(word)
    king.run()
