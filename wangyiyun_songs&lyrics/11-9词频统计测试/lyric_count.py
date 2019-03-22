#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
import jieba
import jieba.analyse
import os

# text = ['Hello', 'My', 'name', 'is', 'dcpeng', 'Dcpeng', 'is', 'name']
# for i in range(len(text)):
#     # print(text[i])
#     text[i] = text[i].lower()
# count_dict = Counter(text).most_common(4)
# print(count_dict)

# text = ['忽然就流出泪来', '忽然想要听到她的声音', '而我却什么话都说不出来',
#         '是谁在温暖你', '有谁会让我觉得这夜晚还有期盼', '我就会跟着它去远行',
#         '可是你在哪里', '可是明天醒来的第一脸阳光']
# # for i in range(len(text)):
#     # print(text[i])
#     # text[i] = text[i].lower()
# count_dict = Counter(text).most_common(4)
# print(count_dict)

# def get_word():
#     seg_list = jieba.cut("他来到了网易杭研大厦")
#     return ", ".join(seg_list)
# if __name__ == '__main__':
#     print(get_word())

def read_content(content_path):
    content = ''
    for f in os.listdir(content_path):
        file_fullpath = os.path.join(content_path, f)
        if os.path.isfile(file_fullpath):
            print('Loading {}'.format(file_fullpath))
            content += open(file_fullpath, 'r', encoding='utf-8').read()
            content += '\n'
    print('Down loading')
    return content

content = read_content('./text/')
# print('\nPreview the previous content\n')
# print(content[:99])

# result = jieba.analyse.textrank(content, topK=100, withWeight=True)
# keywords = dict()
# for i in result:
#     keywords[i[0]] = i[1]
# print(keywords)
#
# count_dict = Counter(content).most_common(10)
# print(count_dict)

wordsall = {}  # define return dic
postfile = open('./text/outputs.txt', 'r', encoding='utf-8')
ptitle = postfile.readlines()
for ititle in ptitle:
    ititle = ititle.replace('\n', '')  # clean \n
    seg_list = jieba.cut(ititle, cut_all=False)
    rowlist = ' '.join(seg_list)
    words = rowlist.split(' ')
    for word in words:
        if word != '':
            if word in wordsall:
                wordsall[word] += 1
            else:
                wordsall[word] = 1
            wordsall = sorted(wordsall.items(), key=lambda d: d[1], reverse=True)
            for word, cnt in wordsall:
                print('{0}: {1}'.format(word, cnt))
