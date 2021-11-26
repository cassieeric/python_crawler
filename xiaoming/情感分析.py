#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snownlp import SnowNLP

# 积极/消极
# print(s.sentiments)  # 0.9769551298267365  positive的概率


def get_word():
    with open("情感分析用词.txt", encoding='utf-8') as f:
        line = f.readline()
        word_list = []
        while line:
            line = f.readline()
            word_list.append(line.strip('\r\n'))
        f.close()
        return word_list


def get_sentiment(word):
    text = u'{}'.format(word)
    s = SnowNLP(text)
    print(s.sentiments)


if __name__ == '__main__':
    words = get_word()
    for word in words:
        try:
            get_sentiment(word)
        except:
            continue

# text = u'''
# 也许
# '''
# s = SnowNLP(text)
# print(s.sentiments)
#     with open('lyric_sentiments.txt', 'a', encoding='utf-8') as fp:
#         fp.write(str(s.sentiments)+'\n')
# print('happy end')
