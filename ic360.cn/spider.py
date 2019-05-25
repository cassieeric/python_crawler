import random
import time
import pandas as pd
import csv
import requests
from lxml import etree
import redis
import json
import pymongo

class IC(object):
    def __init__(self):
        self.headers = {
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
        self.r = requests.session()
        self.redis_client = redis.Redis(host="localhost", port=6379, db=11, password=None)
        self.mongo_client = pymongo.MongoClient("localhost", 27017)
        self.db = self.mongo_client["IC360"]

    def get_html(self, url):
        try:
            res = self.r.get(url, headers=self.headers)
            if res.status_code == 200:
                return res.text
            return None
        except ConnectionError:
            return None


    # def parse_seed(self, seed_html):
    #     doc = self.Xpath(seed_html)
    #     try:
    #         trs = doc.xpath("//div[@class='search_list']/table/tr")
    #         if len(trs) > 0:
    #             tag = doc.xpath("//div[@class='location']/span[2]/strong/text()")
    #             tag = tag[0] if len(tag) > 0 else None
    #             for tr in trs[1:]:
    #                 item = {}
    #                 item["所属标签"] = tag
    #                 title = tr.xpath("./td[@class='tc ac']/a/text()")
    #                 item["制造商型号"] = title[0] if len(title)>0 else None
    #                 link = tr.xpath("./td[@class='tc ac']/a/@href")
    #                 item["链接"] = link[0] if len(link)>0 else None
    #                 chang = tr.xpath("./td[@class='tc'][1]/text()")
    #                 item["厂家"] = chang[0].replace('\r\n', '').replace(' ', '') if len(chang)>0 else None
    #                 desc = tr.xpath("./td[@class='tc'][2]/text()")
    #                 item["描述"] = desc[0].replace('\r\n', '').replace(' ', '') if len(desc)>0 else None
    #                 nums = tr.xpath("./td[@class='tc']/p/text()")
    #                 item["库存数量"] = nums[0].replace('\r\n', '').replace(' ', '') if len(nums)>0 else None
    #                 pi = tr.xpath("./td[@class='tc'][4]/text()")
    #                 item["批号"] = pi[0].replace('\r\n', '').replace(' ', '') if len(pi)>0 else None
    #                 date_time = tr.xpath("./td[@class='tc'][5]/text()")
    #                 item["货期"] = date_time[0].replace('\r\n', '').replace(' ', '') if len(date_time)>0 else None
    #                 # dans = tr.xpath("./td[@style='text-align: center;']/p")
    #                 # dj = tr.xpath("./td[6]/p")
    #                 # lst = []
    #                 # for a, b in zip(dj,dans):
    #                 #     sums = a.xpath("./text()")[0].replace('\r\n', '').replace(' ', '')
    #                 #     price = b.xpath("./text()")[0].replace('\r\n', '').replace(' ', '')
    #                 #     lst.append((sums,price))
    #                 # item["数量单价"] = lst
    #                 dans = [dan.xpath("./text()")[0].replace('\r\n', '').replace(' ', '') for dan in tr.xpath("./td[@style='text-align: center;']/p")]
    #                 dans = '\n'.join(dans)
    #                 dj = [dj.xpath("./text()")[0].replace('\r\n', '').replace(' ', '') for dj in tr.xpath("./td[6]/p")]
    #                 dj = '\n'.join(dj)
    #                 item["单价含税(13%)"] = dans
    #                 item["起订量"] = dj
    #                 self.save_to_mongodb(item)
    #             time.sleep(random.uniform(0.3,2))
    #
    #     except Exception as e:
    #         print(e)
    #         pass



    def get_page_nums(self,html):
        try:
            doc = self.Xpath(html)
            page_nums = doc.xpath("//span[@class='ano_span']/em/b/text()")
            page_nums = page_nums[0] if len(page_nums) > 0 else None
            return page_nums
        except:
            return None


    def Xpath(self, html):
        return etree.HTML(html)

    def save_to_mongodb(self, item):
        collection = self.db["ic360_item"]
        if item:
            # if collection.update({"链接": item["链接"]}, {"$set": item}, True):
            if collection.insert(item):
                print("成功存储到MONGODB", item)
            else:
                print("存储到MONGODB失败", item)


    def get_redis_data(self):
        data_byte = self.redis_client.lpop("IC360")
        data_str = data_byte.decode()
        data_json = json.loads(data_str)
        return data_json.get("link")

    def parse_table(self, html):
        tb = pd.read_html(html, skiprows=[0, ])[0]  # 经观察发现所需表格是网页中第4个表格，故为[3]
        tb.to_csv(r'IC360.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
        print('抓取完成')

    def run(self):
        with open(r'IC360.csv', 'a', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerow(
                ['制造商型号', '厂家', '描述', '库存数量', '批号', '起订量', '香港(美金)', '单价含税(13%)', '货期', '操作'])
        while 1:
            try:
                href = self.get_redis_data()
                print("LINK", href)
                seed_html = self.get_html(href)
                try:
                    self.parse_table(seed_html)
                    page_nums = self.get_page_nums(seed_html)
                    print("总页数: ",page_nums )
                    if page_nums:
                        for page in range(2, int(page_nums) + 1):
                            next_page = href + "pi" + str(page) + "/"
                            print("当前页: ", next_page)
                            next_page_html = self.get_html(next_page)
                            self.parse_table(next_page_html)
                        time.sleep(random.uniform(0.3, 2))
                except IndexError:
                    print("不是可转换对象 ... ")
                    pass

            except Exception as e:
                if "IC360" not in self.redis_client.keys():  # 获取url完毕
                    print("爬取结束,关闭爬虫！")
                    break
                else:
                    print("请求发送失败", e)# 其他原因请求失败
                    pass

if __name__ == '__main__':
    I = IC()
    I.run()

"https://ic360.cn/products/%E9%9B%86%E6%88%90%E7%94%B5%E8%B7%AF/Embedded%20-%20System%20On%20Chip%20(SoC)/pi3/"