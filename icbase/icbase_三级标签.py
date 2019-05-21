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

def get_info(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    return response

def get_detail_info(response):
    regex_str = r'<li><a href="ClassList3.aspx?(.*?)">'

    short_urls = re.findall(regex_str, response)

    with open('urls.txt', 'a') as fp:
       for short_url in short_urls:
        url = 'http://www.icbase.com/ClassList3.aspx' + short_url
        fp.write(url+"\n")
        print(url)
    fp.close()

if __name__ == '__main__':
    main_url = 'http://www.icbase.com/ClassList2.aspx?id=3'
    response = get_info(main_url)
    get_detail_info(response)
