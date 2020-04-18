import requests
import os
import re
from fake_useragent import UserAgent
from lxml import etree

house_dict = {}


def get_page(url, page_num):
    pageList = []
    for i in range(1, page_num + 1):
        formdata = {
            'PageIndex': i}
        try:
            response = requests.post(url=url, data=formdata, headers=kv)
            html = response.content.decode('utf-8')
            parse_html = etree.HTML(html)
            page = parse_html.xpath('//div[@class="wrap"]//div[@class="list-main"]')
            for li in page:
                house_dict['项目'] = li.xpath('.//div[@class="main-top"]//b/text()')[0].strip()
                house_dict['QQ'] = li.xpath('.// div[ @class ="main-com"]//span//a/text()')[0].strip()
                # print(house_dict)
                # 关闭文件
                f = open('QQ号.csv', 'a', encoding='utf-8')  # 以'w'方式打开文件
                f.write(str(house_dict))
                print(house_dict)
                f.write("\n")  # 键和值分行放，键在单数行，值在双数行
                f.close()
            tempList = []
        except:
            pass
            # print('链接失败')
    print(pageList)
    return pageList


url = 'https://www.cpajia.com/index.php?g=Wap&a=search'
ua = UserAgent(verify_ssl=False)
kv = {
    'User-Agent': ua.random}

pageList = get_page(url, 100)  # 页数（网址，页数）
