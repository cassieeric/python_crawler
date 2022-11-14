# coding: utf-8
"""
思路：
1、拿到主页面的源代码，找到iframe
2、从iframe页面的源代码中找到m3u8文件
3、下载第一层的m3u8文件， ---> 下载第二层的m3u8文件(视频存放路径)
4、下载视频
5、下载密钥，进行解密操作，
6、合并所有ts文件为一个mp4文件
"""
import requests


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"}
url1 = "https://vod1.bdzybf1.com/20200901/e4NhpyM5/index.m3u8"
response1 = requests.get(url=url1, headers=headers)
with open('first.m3u8', "w") as f:
    f.write(response1.text)
print("下载完成")
