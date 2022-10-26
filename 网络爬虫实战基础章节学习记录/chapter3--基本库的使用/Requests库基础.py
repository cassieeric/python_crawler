# -*- coding: utf-8 -*-
import requests

url = "http://tieba.baidu.com"
response = requests.get(url)
print(response.status_code)
print(response.encoding)
print(response.apparent_encoding)
print(response.text)
print(response.content)