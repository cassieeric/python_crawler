#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import Counter
import jieba

all_words = []
for filename in os.listdir('D:/pythonDemo/November/11-2网易云歌词爬取/all_singer/歌手们的歌词情绪/'):
    with open('D:/pythonDemo/November/11-2网易云歌词爬取/all_singer/歌手们的歌词情绪/' + filename, encoding='gbk') as f:
        lyrics = f.read()
        data = jieba.cut(lyrics)
        all_words.extend(set(data))

count = Counter(all_words)
result = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word in result:
    print(word[0], word[1])
