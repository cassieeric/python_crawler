# -*- coding: utf-8 -*-
import itchat
import numpy as np
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image

itchat.login()
friends = itchat.get_friends(update=True)

NickName = friends[0].NickName  # 获取自己的昵称
os.mkdir(NickName)  # 为自己创建一个文件夹

file = '\%s' % NickName  # 刚刚创建的那个文件夹的相对路径
cp = os.getcwd()  # 当前路径
path = os.path.join(cp + file)  # 刚刚创建的那个文件夹的绝对路径
os.chdir(path)  # 切换路径

number_of_friends = len(friends)  # 好友数量
# print(number_of_friends)

df_friends = pd.DataFrame(friends)  # pandas可以把据处理成 DataFrame

# 提取并清理签名，得到语料库。
Signatures = df_friends.Signature

regex1 = re.compile('<span.*?</span>')  # 匹配表情

regex2 = re.compile('\s{2,}')  # 匹配两个以上占位符。

# 用一个空格替换表情和多个空格。
Signatures = [regex2.sub(' ', regex1.sub('', signature, re.S)) for signature in Signatures]

Signatures = [signature for signature in Signatures if len(signature) > 0]  # 去除空字符串

text = ' '.join(Signatures)

file_name = NickName+'_wechat_signatures.txt'

with open(file_name, 'w', encoding='utf-8') as f:
    f.write(text)
    f.close()

# jieba 分词分析语料库
wordlist = jieba.cut(text, cut_all=True)

word_space_split = ' '.join(wordlist)

# 画图
coloring = np.array(Image.open("D:/pythonDemo/2018/May/pic.png"))  # 词云的背景和颜色。这张图片在本地。

# 生成词云
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,
                         font_path="D:/pythonDemo/2018/May/simhei.ttf").generate(word_space_split)
# 指定字体，有些字不能解析中文，这种情况下会出现乱码。
# font_path="D:\pythonDemo\2018\May\simhei.ttf"


file_name_p = NickName+'.jpg'

my_wordcloud.to_file(file_name_p)  # 保存图片
