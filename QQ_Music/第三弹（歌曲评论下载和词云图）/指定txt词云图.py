from wordcloud import WordCloud
import jieba
import numpy
import PIL.Image as Image

def cut(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=" ".join(wordlist_jieba)
    return space_wordlist
with open("句号评论.txt" ,encoding="utf-8")as file:
    text=file.read()
    text=cut(text)
    mask_pic=numpy.array(Image.open("心.png"))
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
    collocations=False,
    max_words= 100,
    min_font_size=10, 
    max_font_size=500,
    mask=mask_pic).generate(text)
    image=wordcloud.to_image()
    # image.show()
    wordcloud.to_file('云词图.png')  # 把词云保存下来 