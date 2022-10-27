# -*- coding: utf-8 -*-
import requests

url = "https://www.ygdy8.com/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77",
}

response = requests.get(url, headers=headers)
status_code = response.status_code
print(status_code)
response.encoding = "GBK"
html = response.text
print(html)


response = requests.get(url=url, headers=headers)
code = response.status_code
print(code)
response = response.content.decode('GBK')

print(response)



