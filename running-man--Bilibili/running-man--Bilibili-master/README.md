# running man -Bilibili
从B站爬取所有评论数据
再用python做相关分析
最后的词云图是用R生成的
这是R的代码
library(wordcloud2)
data<-read.csv(header=FALSE,'C:/Users/伊雅/PycharmProjects/untitled/venv/share/doc/jieba.csv')
f=data.frame(data)
f
wordcloud2(f)
