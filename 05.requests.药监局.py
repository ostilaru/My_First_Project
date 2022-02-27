# 动态加载数据
# 首页中对应的企业信息数据是通过ajax动态请求到的
# 通过对详情页url的观察发现：
    # url的域名都是一样的，只是携带的参数（id）不一样
    # id值可以从首页对应的ajax请求到的json串中获取
    # 域名和id值拼接出一个完整的企业对应的详情页
# 详情页的企业详细数据也是动态加载出来的
#  http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
#  http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
# 观察后发现：
    # 所有的post请求的url都是一样的，只有参数的id是不同的
    # 如果可以批量获取多家企业的id，就可以将id和url形成的完整的详情页对应的详细数据的ajax请求的url
import requests
import json
if __name__ == "__main__":
    # 批量获取有关企业的id
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    # 参数的封装
    id_list = [] #存储企业id
    all_data_list = [] #存储所有企业详情数据

    for page in range(1,30):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        ids_json = requests.post(url=url,data=data,headers=headers).json()
        for dic in ids_json['list']:
            id_list.append(dic['ID'])
        # print(id_list)
    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        # print(detail_json)
        all_data_list.append(detail_json)

    # 持久化存储all_data_list
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print("over!")
