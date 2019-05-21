# -*- coding: utf-8 -*-
# /usr/bin/env python

'''
Author: dcp
Email: pdcfighting@163.com
Wechat: pycharm1314
Blog: https://blog.csdn.net/pdcfighting
公众号: Python爬虫与数据挖掘

date: 2019/5/20 20:52
desc:
'''

import requests
import re
from lxml import etree

def get_url():
    urls = []
    for line in open('all_urls.txt', 'r'):
        urls.append(line)
    return urls

def get_info(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    return response

def get_detail_info(response):
    html = etree.HTML(response)
    selectors = html.xpath('//tr[@onmouseover="this.bgColor=\'#EFF3FB\';"]')
    for selector in selectors[1:3]:

        xinghao = selector.xpath('//a[@style="color:#0060e3"]/text()')
        zhekou = selector.xpath('//span[@style="color:red"]/text()')
        changshang = selector.xpath('//td[@style="width:100px;"]/text()')[0]

        kucunshu = selector.xpath('//td[@style="color:Black;width:67px;"]/text()')
        # try:
        #     jiage = selector.xpath('//td[@style="color:Black;width:161px;"]/text()').strip()
        #     if jiage == '暂无':
        #         jiage = '暂无'
        #         print(jiage)
        #     else:
        #         jiage = selector.xpath('//table[@class="prilist"]/text()')
        #         print(jiage)
        # except:
        #     jiage = 'exception'

        # print(xinghao)
        # print(zhekou)
        # print(changshang)
        # print(miaoshu)
        # print(kucunshu)
        # print(jiage)

        # try:
        #     # miaoshu = selector.xpath('//span[contains(@id,"SVG")]').strip()
        #     miaoshu = selector.xpath('//span[@id="SGVClass4Pro_ctl0{}_labDescription"]/text()').format(str(i) for i in range(2, len(selectors)+2))
        #
        #     print(miaoshu)
        # except:
        #     miaoshu = 'exception'
        #     print(miaoshu)


if __name__ == '__main__':
    # urls = get_url()
    # for url in urls[0:1]:
    #     print(url)
    url = 'http://www.icbase.com/ClassList3.aspx?id=1728'
    response = get_info(url)
    get_detail_info(response)
