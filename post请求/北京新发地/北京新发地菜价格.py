# coding: utf-8
import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.xinfadi.com.cn/getPriceData.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"}
param = {
    "limit": 20,
    "current": 1
}

response = requests.get(url=url, params=param).json()
print(response)

f = open('data.csv', mode='w', encoding='utf-8')
csv_writer = csv.writer(f)

html = BeautifulSoup(response.text, "html.parser")
table1 = html.find('table', attrs={'class': 'hq-table'})
table2 = html.find('table', class_="hq-table")  # class是关键字，所以使用class_来做属性提取，和上面的代码一样的效果
# tr是指行，td是指列
trs = table1.find_all('tr')[1:]  # 首行是head表头，不需要
for tr in trs:  # 每一行
    tds = tr.find_all('td')
    name = tds[0].text  # .text拿到被标签标记的内容
    low = tds[1].text  # .text拿到被标签标记的内容
    avg = tds[2].text  # .text拿到被标签标记的内容
    high = tds[3].text  # .text拿到被标签标记的内容
    size = tds[4].text  # .text拿到被标签标记的内容
    unit = tds[5].text  # .text拿到被标签标记的内容
    date = tds[0].text  # .text拿到被标签标记的内容
    csv_writer.writerow([name, low, avg, high, size, unit, date])
f.close()
print('Write over!')









