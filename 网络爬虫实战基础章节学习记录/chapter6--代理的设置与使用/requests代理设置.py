# -*- coding: utf-8 -*-
import requests

url = "http://myip.kkcha.com"
proxies = {"http": "171.214.214.185:8118"}
response = requests.get(url=url, proxies=proxies)
print(response.text)

