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

# 运行程序，扫码登录
itchat.login()
friends = itchat.get_friends(update=True)

NickName = friends[0].NickName  # 获取自己的昵称
os.mkdir(NickName)  # 为自己创建一个文件夹

file = '\%s' % NickName  # 刚刚创建的那个文件夹的相对路径
cp = os.getcwd()  # 当前路径
path = os.path.join(cp + file)  # 刚刚创建的那个文件夹的绝对路径
os.chdir(path)  # 切换路径

# number_of_friends = len(friends)  # 好友数量
# print(number_of_friends)

df_friends = pd.DataFrame(friends)  # pandas可以把据处理成 DataFrame

# 分析好友性别,男性为1；女性为2；未知为0；
# 自定义一个计数函数
def get_count(Sex):
    counts = defaultdict(int)  # 初始化一个字典
    for x in Sex:
        counts[x] += 1
        return counts

# 获取性别信息
Sex = df_friends.Sex
Sex_count = get_count(Sex)
print(Sex_count)

# pandas为Series提供了一个value_counts()方法，可以更方便统计各项出现的次数
Sex_count2 = Sex.value_counts()  # defaultdict(int, {0: 31, 1: 292, 2: 245})
print(Sex_count2)

# 画图
Sex_count2.plot(kind='bar')
