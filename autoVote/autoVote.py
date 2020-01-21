import time

from lxml import etree
import requests

with open("cookie.txt", "r", encoding="utf-8") as f:
    cookie = f.read()

base_url = "https://dig.chouti.com/"
header_dict = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "dig.chouti.com",
    "Referer": "https://dig.chouti.com/?showLogin=true",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}
r1 = requests.get(url=base_url, headers=header_dict)
r1.encoding = r1.apparent_encoding

html = etree.HTML(r1.content)

# 文章id列表
data_id_list = html.xpath("//a[@class='link-title link-statistics']/@data-id")
print(data_id_list)

lick_url = "https://dig.chouti.com/link/vote"
header_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "15",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": f"{cookie}",
    "Host": "dig.chouti.com",
    "Origin": "https://dig.chouti.com",
    "Referer": "https://dig.chouti.com/",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


# 点赞
for data_id in data_id_list[:10]:
    print(data_id)
    r1 = requests.post(url=lick_url, headers=header_dict, data={"linkId": data_id})
    print(r1.text)
    time.sleep(1)

自动点赞
