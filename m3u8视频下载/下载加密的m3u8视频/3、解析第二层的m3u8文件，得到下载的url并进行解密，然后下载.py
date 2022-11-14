# coding: utf-8

import requests
from Crypto.Cipher import AES
import subprocess

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}


def get_m3u8_url():
    with open("second.m3u8", 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            # print(line)
            download(line)


"""
直接使用download()函数进行下载，可以下载成功，但是文件是打不开的，因为该视频是加密过的，需要进行解密
加密方式在m3u8文件中的
#EXT-X-KEY:METHOD=AES-128,URI="https://ts1.yuyuangewh.com:9999/20200901/e4NhpyM5/1000kb/hls/key.key"
可以看到是AES-128加密方法，使用的key.key，可以在响应中看得到，这里是：50aa1c78cad9eb8d
有了加密方法和密钥，就可以进行破解了
思路步骤
1、目前我们已经拿到了视频播放路径，接下来就可以下载视频
2、下载密钥，进行解密操作
3、合并所以的ts文件为一个mp4文件
"""


def download(url):
    name = url.split("/")[-1]
    response = requests.get(url, headers=headers)
    aes = AES.new(key.encode("utf-8"), AES.MODE_CBC, key.encode("utf-8"))  # 通过秘钥新建解密器
    with open("videos/%s" % name, "wb") as f:
        content = aes.decrypt(response.content)
        f.write(content)
    print("%s下载完成" % name)


def merge_file():
    command = r"copy/b E:\PythonCrawler\有趣的代码\m3u8视频下载\下载加密的m3u8视频\videos\*.ts " \
              r"E:\PythonCrawler\有趣的代码\m3u8视频下载\下载加密的m3u8视频\movie.mp4"
    subprocess.getoutput(command)
    print("合并完成")


if __name__ == '__main__':
    key = "50aa1c78cad9eb8d"
    get_m3u8_url()
    # merge_file()
