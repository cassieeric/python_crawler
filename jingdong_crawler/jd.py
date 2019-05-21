#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

def get_product(keyword):
    url = 'https://search.jd.com/Search?keyword=' + quote(keyword) + '&enc=utf-8'
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    li_all = soup.find_all('li', class_="gl-item")
    for i in li_all:
        print('title: ', i.a['title'])
        print('url: ', i.a['href'].split('//')[1])
        # print('img: ', i.a.img['src'])
        # print('img: ', i.a.img.get('src'))

        # try:
        #     print('img: ', i.a.img['src'].split('//')[1])
        # except Exception as e:
        #     # pass
        #
        #     # print(i.img.attrs)
        #     print('img: ', i.a.img['data-lazy-img'].split('//')[1])

        img = i.a.img["src"].split('//')[1] if "src" in i.img else i.a.img.get('data-lazy-img')
        print('img: ', img)

        print('price: ', i.strong.i.get_text())
        # print('price: ', i.div.strong.i.string())
        print('=========================')
'''
如果使用img['src']会有报错产生，因为匹配不到对应值，
但是使用get['src']就不会报错，如果没有匹配到，它会返回None。
此外也可以利用try+except异常处理，如果匹配不到就pass
'''

if __name__ == '__main__':
    get_product('狗粮')
