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

content = read_content('./birthday/')
# print('\nPreview the previous content\n')
# print(content[:99])

result = jieba.analyse.textrank(content, topK=100, withWeight=True)
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)

image = Image.open('./images/pic1.png')
graph = np.array(image)

wc = WordCloud(font_path='./fonts/simhei.ttf', background_color='white', max_words=100, mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)

plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis('off')
plt.show()
