# coding:utf-8

# @Time : 2022/5/10 16:30
# @Author: Python进阶者
# @公众号: Python爬虫与数据挖掘
# @website : http://pdcfighting.com/
# @File : 头条jsrpc.py
# @Software: PyCharm

import requests
import json
import urllib.parse
import time


param_url = "http://127.0.0.1:12080/go?group=para&name=test&action=get_para"
response = requests.get(url=param_url).text
response_json = json.loads(response)
sign = response_json["get_para"]
print(sign)
behot_time = int(time.time())
params = {
            "offset": 0,
            "channel_id": 0,
            "max_behot_time": 1641416108,
            "category": "pc_profile_recommend",
            "aid": 24,
            "app_name": "toutiao_web",
            "disable_raw_data": "true",
            "_signature": sign
        }
url = f'https://www.toutiao.com/api/pc/list/feed'

response_detail = requests.get(url, params=params).json()
print(response_detail["data"])

