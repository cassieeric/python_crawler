import requests
import redis
from lxml import etree
import json
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

    def get_html(self, url):
        try:
            res = self.r.get(url, headers=self.headers)
            if res.status_code == 200:
                return res.text
            return None
        except ConnectionError:
            return None

    def parse_index(self, index_html):
        doc = self.Xpath(index_html)
        dl_list = doc.xpath("//div[@class='classify-all']/dl")
        for dls in dl_list:
            # print(len(dls.xpath("./dd")))
            for dl in dls.xpath("./dd"):
                data = {}
                title = dl.xpath("./a/text()")
                data["title"] = title[0] if len(title) > 0 else None
                link = dl.xpath("./a/@href")
                data["link"] = link[0] if len(link)>0 else None
                print(data)
                self.redis_client.lpush("IC360",json.dumps(data, ensure_ascii=False))

    def Xpath(self, html):
        return etree.HTML(html)

    def run(self):
        html = self.get_html("https://ic360.cn/Categories/Products/")
        self.parse_index(html)

if __name__ == '__main__':
    I = IC()
    I.run()











# import pandas as pd
# import csv
# import requests
#
# headers = {
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Accept-Language": "zh-CN,zh;q=0.9",
#             "Cache-Control": "max-age=0",
#             "Connection": "keep-alive",
#             "Cookie": "sadfsdfsdfsdf=ffbicevg0bkxslxwun1yvalc; sso_temp_uid=fed2f0de2c7e4f52a855ce4b51786e75",
#             "Host": "ic360.cn",
#             "Referer": "https://ic360.cn/",
#             "Upgrade-Insecure-Requests": "1",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
#                         }
#
# url = 'https://ic360.cn/products/%E5%8D%95%E7%89%87%E6%9C%BA/%E5%A4%84%E7%90%86%E5%99%A8/DSP/%E5%B5%8C%E5%85%A5%E5%BC%8F%20-%20%E5%BE%AE%E6%8E%A7%E5%88%B6%E5%99%A8%20-%20%E5%BA%94%E7%94%A8%E7%89%B9%E5%AE%9A/'
# res = requests.get(url,headers=headers)
# html = res.text
# tb = pd.read_html(html,skiprows=[0,])[0]
# with open(r'ic360.csv', 'a', encoding='utf-8-sig', newline='') as f:
#     csv.writer(f).writerow(['制造商型号', '厂家', '描述', '库存数量', '批号', '起订量', '香港(美金)', '单价含税(13%)', '货期','操作'])
# tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
# print('抓取完成')


