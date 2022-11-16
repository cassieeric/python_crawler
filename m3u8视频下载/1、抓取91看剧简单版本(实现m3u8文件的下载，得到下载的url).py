# coding: utf-8
"""
1、拿到54812-1-1.html页面的源代码
2、从源代码中提取到m3u8的url
3、下载m3u8
4、读取m3u8文件，下载视频
5、合并视频
"""
import m3u8
import requests
import aiohttp
import aiofiles
import asyncio
import re

url = "https://www.91kanju.com/vod-play/54812-1-1.html"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
response1 = requests.get(url, headers=headers)
# response = requests.get(url, verify=False, headers=headers).text
regex = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的url地址
m3u8_url = re.search(regex, response1.text).group("url")  # 拿到m3u8的url
print(m3u8_url)
response1.close()
response2 = requests.get(m3u8_url, headers=headers)
with open("哲人王后.m3u8", "wb") as f:  # 下载m3u8文件，得到url
    f.write(response2.content)
response2.close()
print("下载完成")


