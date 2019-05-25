# coding=utf-8
import random
import time
import pandas as pd
import csv
import requests
from lxml import etree
import redis
import json
import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client["IC360"]

def get_html(url):
    try:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "sadfsdfsdfsdf=ffbicevg0bkxslxwun1yvalc; sso_temp_uid=fed2f0de2c7e4f52a855ce4b51786e75",
            "Host": "ic360.cn",
            "Referer": "https://ic360.cn/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        return None
    except ConnectionError as e:
        print(e)
        return None


# def parse_seed(html):
#     doc = etree.HTML(html)
#     try:
#         trs = doc.xpath("//div[@class='search_list']/table/tr")
#         if len(trs) > 0:
#             # tag = doc.xpath("//div[@class='location']/span[2]/strong/text()")
#             # tag = tag[0] if len(tag) > 0 else None
#             for tr in trs[1:]:
#                 item = {}
#                 # item["所属标签"] = tag
#                 title = tr.xpath("./td[@class='tc ac']/a/text()")
#                 item["制造商型号"] = title[0] if len(title) > 0 else None
#                 link = tr.xpath("./td[@class='tc ac']/a/@href")
#                 item["链接"] = link[0] if len(link) > 0 else None
#                 chang = tr.xpath("./td[@class='tc'][1]/text()")
#                 item["厂家"] = chang[0].replace('\r\n', '').replace(' ', '') if len(chang) > 0 else None
#                 desc = tr.xpath("./td[@class='tc'][2]/text()")
#                 item["描述"] = desc[0].replace('\r\n', '').replace(' ', '') if len(desc) > 0 else None
#                 nums = tr.xpath("./td[@class='tc']/p/text()")
#                 item["库存数量"] = nums[0].replace('\r\n', '').replace(' ', '') if len(nums) > 0 else None
#                 pi = tr.xpath("./td[@class='tc'][4]/text()")
#                 item["批号"] = pi[0].replace('\r\n', '').replace(' ', '') if len(pi) > 0 else None
#                 date_time = tr.xpath("./td[@class='tc'][5]/text()")
#                 item["货期"] = date_time[0].replace('\r\n', '').replace(' ', '') if len(date_time) > 0 else None
#                 # dans = tr.xpath("./td[@style='text-align: center;']/p")
#                 # dj = tr.xpath("./td[6]/p")
#                 # lst = []
#                 # for a, b in zip(dj,dans):
#                 #     sums = a.xpath("./text()")[0].replace('\r\n', '').replace(' ', '')
#                 #     price = b.xpath("./text()")[0].replace('\r\n', '').replace(' ', '')
#                 #     lst.append((sums,price))
#                 # item["数量单价"] = lst
#                 dans = [dan.xpath("./text()")[0].replace('\r\n', '').replace(' ', '') for dan in
#                         tr.xpath("./td[@style='text-align: center;']/p")]
#                 dans = '\n'.join(dans)
#                 dj = [dj.xpath("./text()")[0].replace('\r\n', '').replace(' ', '') for dj in tr.xpath("./td[6]/p")]
#                 dj = '\n'.join(dj)
#                 item["单价含税(13%)"] = dans
#                 item["起订量"] = dj
#                 save_to_mongodb(item)
#             time.sleep(random.uniform(0.3, 2))
#     except:
#         pass

def parse_seed(html): # pandas  html to table
    tb = pd.read_html(html, skiprows=[0, ])[0]
    tb.to_csv(r'IC360_sy.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
    print('抓取完成')

def get_page_nums(html):
    try:
        doc = etree.HTML(html)
        page_nums = doc.xpath("//span[@class='ano_span']/em/b/text()")
        page_nums = page_nums[0] if len(page_nums) > 0 else None
        return page_nums
    except:
        return None

def save_to_mongodb(item):
    collection = db["sy_ic360_item"]
    if item:
        if collection.insert(item):
            print("成功存储到MONGODB", item)
        else:
            print("存储到MONGODB失败", item)

def run():
    with open(r'IC360_sy.csv', 'a', encoding='utf-8-sig', newline='') as f:
        csv.writer(f).writerow(
            ['制造商型号', '厂家', '描述', '库存数量', '批号', '起订量', '香港(美金)', '单价含税(13%)', '货期', '操作'])
    href = "https://ic360.cn/products/"
    html = get_html(href)
    page_nums = get_page_nums(html)
    try:
        parse_seed(html)
        if page_nums:
            print("总页数: ", page_nums)
            for page in range(2, int(page_nums) + 1):
                next_page = href + "pi" + str(page) + "/"
                print("当前页: ", next_page)
                next_page_html = get_html(next_page)
                parse_seed(next_page_html)
            time.sleep(random.uniform(0.3, 2))
    except IndexError:
        print("不是可转换对象 ... ")
        pass


run()