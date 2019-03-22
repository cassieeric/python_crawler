#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def stopwd_reduction(infilepath, outfilepath):
    infile = open(infilepath, 'r', encoding='gbk')
    outfile = open(outfilepath, 'w')
    stopwordslist = []
    for str in infile.read().split('\n'):
        if str not in stopwordslist:
            stopwordslist.append(str)
            outfile.write(str + '\n')


stopwd_reduction('stopwords.txt', 'stop_word.txt')