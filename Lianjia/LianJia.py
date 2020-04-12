import requests
from lxml import etree
import time


class LianJia(object):
    def __init__(self):
        self.url = "https://bj.lianjia.com/ershoufang/pg{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        # 请求数据

    def get_page(self, url):
        html = requests.get(url=url, headers=self.headers).content.decode("utf-8")
        # print(html)
        self.page_page(html)

    # 数据处理
    def page_page(self, html):
        parse_html = etree.HTML(html)
        page = parse_html.xpath('//*[@id="content"]/div[1]/ul/li')
        # da=parse_html.xpath("//div[@id='content']/div[1]/ul/li[1]/div[1]/div[2]/div/a")[0].strip()
        # print(len(page))
        # print(parse_html)
        house_dict = {}
        for li in page:
            house_dict['名称'] = li.xpath('.//div[@class="info clear"]//div[@class="title"]/a/text()')[0].strip()
            house_dict["价格"] = li.xpath(".//div[@class='priceInfo']/div[@class='totalPrice']/span/text()")[
                                   0].strip() + "万"
            house_dict["关注度"] = li.xpath('.//div[@class="info clear"]//div[@class="followInfo"]//text()')[0].strip()
            f = open('房子.doc', 'a', encoding='utf-8')  # 以'w'方式打开文件
            f.write(str(house_dict))
            print(house_dict)
            f.write("\n")  # 键和值分行放，键在单数行，值在双数行
            f.close()

    def main(self):

        for pg in range(1, 101):
            url = self.url.format(str(pg))
            self.get_page(url)
            print("第%s页爬取成功！！！！" % pg)
            print(" =" * 50)
            time.sleep(1.4)

            # print("/*" * 100)
            # print(url)


if __name__ == '__main__':
    spider = LianJia()
    spider.main()
