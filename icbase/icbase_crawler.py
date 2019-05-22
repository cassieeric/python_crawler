# -*- coding: utf-8 -*-
# /usr/bin/env python

'''
Author: dcp
Email: pdcfighting@163.com
Wechat: pycharm1314
Blog: https://blog.csdn.net/pdcfighting
公众号: Python爬虫与数据挖掘

date: 2019/5/22 20:30
desc:
'''

import requests
import re
from lxml import etree
import time

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
    trs = html.xpath('//table[@id="SGVClass4Pro"]/tr')
    with open('data.txt', 'a')as fp:
        for selector in trs:
            td = selector.xpath('child::td')
            if td and len(td) > 0:
                pass
            else:
                continue
            t1 = td[1]
            t2 = td[2]
            t3 = td[3]
            t4 = td[5]
            t5 = td[6]
            items = [t1.xpath('string(.)').strip(),
                     t2.xpath('string(.)').strip(),
                     t3.xpath('string(.)').strip(),
                     t4.xpath('string(.)').strip(),
                     t5.xpath('string(.)').strip()]
            fp.write('\t'.join(items).replace('\n', '').replace('\r', '') + '\n')

if __name__ == '__main__':
    urls = get_url()
    for url in urls[62:]:
        print(url)
        time.sleep(0.5)
        response = get_info(url)
        get_detail_info(response)
