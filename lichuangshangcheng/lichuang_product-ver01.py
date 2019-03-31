# -*- coding: utf-8 -*-
# /usr/bin/env python

'''
Author: dcp
Email: pdcfighting@163.com
Wechat: pycharm1314
Blog: https://blog.csdn.net/pdcfighting
公众号: Python爬虫与数据挖掘

date: 2019/3/26 16:30
desc:
'''

import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

data = []

def get_url(url):
    response = requests.get(url).text
    pattern = '<a class="child-item-a" href="(.*?)">'
    links = re.findall(pattern, response, re.S)
    # for link in links:
    #     get_detail(link)
    get_deail(links[0])


def get_deail(url):
    # response = requests.get(url).text.encode("latin1").decode("utf-8")
    # response = requests.get(url).text
    # html = etree.HTML(response)
    # html = etree.tostring(html)
    # result = html.decode('utf-8')

    # tbodys = html.xpath('//tbody')
    # print(etree.tostring(tbodys[0]).decode("latin1").encode("utf-8"))
    # for tbody in tbodys:
    #     print(etree.tostring(tbody).decode('utf-8'))
    response = requests.get(url).text.encode("latin1").decode("utf-8")
    soup = BeautifulSoup(response, 'html.parser')
    tbodys = soup.find_all('tbody')
    # print(tbodys[0])
    # part_2
    part_2 = tbodys[0].find(attrs={'class': 'two'})
    title = part_2.find(attrs={'class': 'two-tit ellipsis'}).a.get_text().strip()
    # pruduct_number = tbodys[0].find(attrs={'class': 'l02_zb'}).li.get_text()
    li_tags = part_2.find_all('li')
    pruduct_number = li_tags[0].get_text().strip()
    store_size = li_tags[1].get_text().strip()
    band = li_tags[2].get_text().strip()
    xinghao = li_tags[3].get_text().strip()
    description = part_2.find(attrs={'class': 'lower'}).div.get_text().strip()
    # print(title, pruduct_number, store_size, band, xinghao, description)
    # data.append([title, pruduct_number, store_size, band, xinghao, description])

    # part_3
    part_3 = tbodys[0].find(attrs={'class': 'three'})
    li_tags = part_3.find_all('li')
    # print(len(li_tags))
    zengzhishui = li_tags[0].get_text().strip()
    print(zengzhishui)
    try:
        start1_end9 = li_tags[1].get_text().strip()
        print(start1_end9)
    except:
        start1_end9 = ''
        print(start1_end9)

    try:
        start10_end29 = li_tags[2].get_text().strip()
        print(start10_end29)
    except:
        start10_end29 = ''
        print(start10_end29)

    try:
        start30_end99 = li_tags[3].get_text().strip()
        print(start30_end99)
    except:
        start30_end99 = ''
        print(start30_end99)

    try:
        start100_end499 = li_tags[4].get_text().strip()
        print(start100_end499)
    except:
        start100_end499 = ''
        print(start100_end499)

    try:
        start500_end999 = li_tags[5].get_text().strip()
        print(start500_end999)
    except:
        start500_end999 = ''
        print(start500_end999)

    try:
        start1000 = li_tags[6].get_text().strip()
        print(start1000)
    except:
        start1000 = ''
        print(start1000)

    # data.append([zengzhishui, start1_end9, start10_end29, start30_end99, start100_end499, start500_end999, start1000])

    # part_4
    part_4 = tbodys[0].find(attrs={'class': 'ffour'})
    li_tags = part_4.find_all('li')
    pan_list = li_tags[0].get_text().strip()
    recent_buy = li_tags[1].get_text().strip()
    inventory = li_tags[2].get_text().strip()
    status = li_tags[3].get_text().strip()
    print(pan_list, recent_buy, inventory, status)

    data.append([title, pruduct_number, store_size, band, xinghao, description, zengzhishui,
                 start1_end9, start10_end29, start30_end99, start100_end499, start500_end999, start1000,
                 pan_list, recent_buy, inventory, status])

    print(data)

    return data

def write_file(data):
    with open('product.txt', 'w', encoding='utf-8') as fp:
        fp.write(str(data))
    print('任务完成!')



if __name__ == '__main__':
    # url = 'https://www.szlcsc.com/catalog.html'
    # get_url(url)
    url = 'https://list.szlcsc.com/catalog/11047.html'
    data = get_deail(url)
    write_file(data)

