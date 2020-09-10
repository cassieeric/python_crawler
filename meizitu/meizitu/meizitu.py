# -*- coding: utf-8 -*-
# @Time : 2020/9/9 20:48
# @Author : 邢小白
# @Site : 
# @File : 自己爬妹纸图.py
# @Software: PyCharm



# -*- coding: utf-8 -*-
# @Time : 2020/8/29 21:11
# @Author : 邢小白
# @Site :
# @File : 妹子图.py
# @Software: PyCharm

'''
1.数据来源? url
2.发送请求? requests
3.解析数据?  筛选数据
4.下载保存?   BeautifulSoup
'''
import requests
from bs4 import BeautifulSoup     # 数据解析
from lxml import etree
import time



def get_girl():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Referer': 'https://www.mzitu.com/'
    }
    url = 'https://www.mzitu.com/xinggan/'
    response = requests.get(url=url, headers=headers)
    # print(response)
    html = etree.HTML(response.text)
    img_url_list = html.xpath('//img[@class="lazy"]/@data-original')
    img_name_list = html.xpath('//img[@class="lazy"]/@alt')
    # print(img_url_list)
    # print(img_name_list)
    for url, name in zip(img_url_list, img_name_list):
        print('正在抓取:' + name + '.jpg')
        with open('%s.jpg' % name, 'wb') as f:
            time.sleep(1)
            f.write(requests.get(url, headers=headers).content)
            f.close()


if __name__ == '__main__':
    get_girl()
