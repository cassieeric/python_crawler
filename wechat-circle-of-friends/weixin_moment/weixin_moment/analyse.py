# -*- coding: utf-8 -*-

"""分析导出的朋友圈数据"""

import json
import os
import jieba
from wordcloud import WordCloud

def analyse_words():
    """
    分析抓取到的朋友圈数据，使用jieba进行分词，使用wordcloud生成词云
    """
    curr_path = os.path.dirname(__file__)  # 当前文件文件夹所在目录
    parent_path = os.path.dirname(curr_path)  # 上层目录
    file_path = os.path.join(parent_path, 'moment.json')
    font_path = os.path.join(parent_path, "simhei.ttf")
    if not os.path.isfile(file_path):
        return
    with open(file_path, encoding='utf-8') as moment_file:
        data = json.load(moment_file)  # 使用json加载文件
        moments = [item.get('moment', '') for item in data]  # 获取朋友圈文字数组
        contents = ' '.join(moments)  # 拼接为长文本
        cut_texts = ' '.join(jieba.cut(contents))  # 使用结巴分词进行中文分词

    cloud = WordCloud(font_path=font_path)
    wordcloud = cloud.generate(cut_texts)  # 生成词云
    wordcloud.to_file('keys.png')  # 保存图片
    image = wordcloud.to_image()  # 转化为图片
    image.show()  # 展示图片


if __name__ == '__main__':
    analyse_words()
