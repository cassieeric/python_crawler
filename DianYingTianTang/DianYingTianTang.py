'''
https://www.ygdy8.net/html/gndy/dyzz/index.html
https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html
https://www.ygdy8.net/html/gndy/dyzz/list_23_3.html
https://www.ygdy8.net/html/gndy/dyzz/list_23_4.html
'''

import time
from urllib import request,parse
import re
import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class FilmSky(object):
    def __init__(self):
        # 定义一个url地址
        self.url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"

        }

    '''发送请求  获取响应 '''
    def get_page(self, url):
        # 构造请求对象
        req = requests.get(url=url, headers=self.headers)
        '''获取响应对象'''
        req.encoding = 'gbk'
        # 数  可以忽略编码问题
        # print(req.text)
        html = req.text
        return html

    # 解析一级页面数据
    def parse_page(self, html):
        # 先解析一级页面  获取电影名称和电影的url地址
        pattern = re.compile('<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>', re.S)
        film_list = pattern.findall(html)
        # print(film_list)


        for film in film_list:
            film_link = "https://www.ygdy8.net"+film[0]
            film_name = film[1]

            download_link = self.parse_two_page(film_link)

            # 测试下
            d = {
                '电影名称': film_name,
                '下载链接': download_link
            }

            print(d)

    # 发送二级页面请求  获取二级页面响应  解析二级页面数据
    def parse_two_page(self, film_link):
        two_html = self.get_page(film_link)
        pattern = re.compile('<td style="WORD-WRAP.*?>.*?<a.*?>(.*?)</a>', re.S)
        # print(pattern)
        download_link = pattern.findall(two_html)

        if len(download_link) > 0:
            download_link = download_link[0].strip()[0:39]
        else:
            download_link = ' '
        # print(download_link)
        return download_link

    def main(self):
        # 准备url地址
        for page in range(1, 4):
            url = self.url.format(page)
            # print(url)
            html = self.get_page(url)

            self.parse_page(html)


if __name__ == '__main__':
    start = time.time()
    spider = FilmSky()
    spider.main()
    end = time.time()
