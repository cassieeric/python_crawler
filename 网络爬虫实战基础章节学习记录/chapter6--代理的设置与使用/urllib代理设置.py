# -*- coding: utf-8 -*-
import urllib.request

url = "http://www.baidu.com"
proxies = {
    "http": "http://171.214.214.185:8118",
    "https": "https://163.125.223.14:8118"
}
proxy_handler = urllib.request.ProxyHandler(proxies)
proxy_opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(proxy_opener)
response = urllib.request.urlopen(url)
print(response.text)
