import requests
from lxml import etree

url = 'https://so.gushiwen.cn/nocdn/ajaxshangxi.aspx?id=8D28FF88D9DCC292'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
# print(response.text)

html = etree.HTML(response.text)
for content in html.xpath('//div/p//text()'):
    print("".join(content.strip()))

