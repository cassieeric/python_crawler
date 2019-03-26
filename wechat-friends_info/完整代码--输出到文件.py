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

# 分析好友性别,男性为1；女性为2；未知为0；
# 自定义一个计数函数
# def get_count(Sex):
#     counts = defaultdict(int)  # 初始化一个字典
#     for x in Sex:
#         counts[x] += 1
#         return counts

# 获取性别信息
Sex = df_friends.Sex
# Sex_count = get_count(Sex)
# print(Sex_count)

# pandas为Series提供了一个value_counts()方法，可以更方便统计各项出现的次数
Sex_count = Sex.value_counts()  # defaultdict(int, {0: 31, 1: 292, 2: 245})
# print(Sex_count2)

Province = df_friends.Province
Province_count = Province.value_counts()
Province_count = Province_count[Province_count.index != '']  # 有一些好友地理信息为空，过滤掉这一部分人。

City = df_friends.City
City_count = City.value_counts()
City_count = City_count[City_count.index != '']  # 有一些好友地理信息为空，过滤掉这一部分人。

file_name_all = NickName+'_basic_inf.txt'

write_file = open(file_name_all, 'w')

write_file.write(
    '你共有%d个好友,其中有%d个男生，%d个女生，%d未显示性别。\n\n' % (number_of_friends, Sex_count[1], Sex_count[2], Sex_count[0]) +

    '你的朋友主要来自省份：%s(%d)、%s(%d)和%s(%d)。\n\n' % (Province_count.index[0], Province_count[0],
    Province_count.index[1], Province_count[1], Province_count.index[2], Province_count[2]) +
    '主要来自这些城市：%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)和%s(%d)。' % (City_count.index[0], City_count[0],
    City_count.index[1], City_count[1], City_count.index[2], City_count[2], City_count.index[3], City_count[3],
    City_count.index[4], City_count[4], City_count.index[5], City_count[5]))

write_file.close()
print('All down, over!')
