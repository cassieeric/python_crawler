# coding: utf-8
"""
通过第一步我们已经得到了M3U8文件，接下来需要针对该文件进行解析，提取出url，之后对齐进行下载
"""
import m3u8
import requests

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

# 解析m3u8文件
n = 1
with open("哲人王后.m3u8", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 去除空格、空白、换行符
        if line.startswith("#"):  # 如何以#打头，直接跳过
            continue
        # print(line)
        # 下载视频片段
        response = requests.get(line, headers=headers)
        f = open(f"videos/{n}.ts", "wb")  # 这种方法下载下来的是一个个的片段，还需要进行文件合并
        # f = open(f"videos/video.ts", "ab")  # 写入格式为ab，追加成一个ts文件，亲测好使
        f.write(response.content)
        f.close()
        response.close()
        n += 1
        print("下载了1个")

