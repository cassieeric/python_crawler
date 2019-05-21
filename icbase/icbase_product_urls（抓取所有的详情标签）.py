# -*- coding: utf-8 -*-
import requests
import re
import time

product_url = []

def get_info(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    # print(response)
    return response

def get_product_list_url(response):
    regex_str = r'<li><a href="/ClassList2.aspx?(.*?)">'
    short_urls = re.findall(regex_str, response)
    for short_url in short_urls:
        url = 'http://www.icbase.com/ClassList2.aspx' + short_url
        print(url)
        time.sleep(1)
        get_product_url(url)

def get_product_url(url):
    response = get_info(url)

    regex_str = r'<li><a href="ClassList3.aspx?(.*?)">'
    short_urls = re.findall(regex_str, response)

    with open('urls.txt', 'a') as fp:
        for short_url in short_urls:
            url = 'http://www.icbase.com/ClassList3.aspx' + short_url
            fp.write(url + "\n")
            # print(url)
    fp.close()

if __name__ == '__main__':
    main_url = 'http://www.icbase.com/'
    response = get_info(main_url)
    get_product_list_url(response)
