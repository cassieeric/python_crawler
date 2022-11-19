# coding: utf-8
"""
参考小小明的文章：https://blog.csdn.net/as604049322/article/details/118347004
"""
import m3u8
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import time
import requests

url = "https://vod1.bdzybf1.com/20200813/uNqvsBhl/index.m3u8"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}


def get_real_url(url):
    playlist = m3u8.load(uri=url, headers=headers)
    return playlist.playlists[0].absolute_uri
# real_url = "https://vod1.bdzybf1.com/20200813/uNqvsBhl/2000kb/hls/index.m3u8"


playlist = m3u8.load(uri=get_real_url(url), headers=headers)
r = requests.get(playlist.keys[0].uri, headers=headers)
key = r.content
# print(playlist.keys[0])
# print(playlist.keys[0].uri)
# print(playlist.keys[0].absolute_uri)
# print(key)
# print(len(playlist.segments))  输出579


def AESDecrypt(cipher_text, key, iv):
    cipher_text = pad(data_to_pad=cipher_text, block_size=AES.block_size)
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=key)
    cipher_text = aes.decrypt(cipher_text)
    return cipher_text


n = len(playlist.segments)  # n=579
size = 0
start = time.time()
for i, seg in enumerate(playlist.segments, 1):
    # print(seg.absolute_uri)
    r = requests.get(seg.absolute_uri, headers=headers)
    data = r.content
    data = AESDecrypt(data, key=key, iv=key)
    size += len(data)
    with open("斗罗大陆.mp4", "ab") as f:
        f.write(data)
    print(f"\r下载进度({i}/{n})，已下载：{size/1024/1024:.2f}MB，下载已耗时：{time.time()-start:.2f}s", end=" ")
