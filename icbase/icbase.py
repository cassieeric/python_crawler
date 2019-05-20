# -*- coding: utf-8 -*-
import requests
import re

product_url = []

def get_info(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    # print(response)
    return response

def get_product_url(response):
    regex_str = r'<li><a href="/ClassList2.aspx?(.*?)">'
    short_urls = re.findall(regex_str, response)
    for short_url in short_urls:
        url = 'http://www.icbase.com/ClassList2.aspx' + short_url
        # print(url)
        get_detail_info(url)

def get_detail_info(url):
    response = get_info(url)
    pass


if __name__ == '__main__':
    main_url = 'http://www.icbase.com/'
    response = get_info(main_url)
    get_product_url(response)
