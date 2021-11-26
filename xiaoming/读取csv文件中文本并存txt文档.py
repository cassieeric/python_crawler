# coding: utf-8
import pandas as pd
df = pd.read_csv('./职位描述.csv', encoding='gbk')
# print(df.head())

for text in df['Job_Description']:
    # print(text)
    if text is not None:
        with open('职位表述文本.txt', mode='a', encoding='utf-8') as file:
            file.write(str(text))

print('写入完成')
