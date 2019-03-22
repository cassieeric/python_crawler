#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

def read_content(content_path):
    content = ''
    for f in os.listdir(content_path):
        file_fullpath = os.path.join(content_path, f)
        if os.path.isfile(file_fullpath):
            print('Loading {}'.format(file_fullpath))
            content += open(file_fullpath, 'r').read()
            content += '\n'
    print('Down loading')
    return content

content = read_content('./lyric/')
# print('\nPreview the previous content\n')
# print(content[:99])

result = jieba.analyse.textrank(content, topK=100, withWeight=True)
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)
