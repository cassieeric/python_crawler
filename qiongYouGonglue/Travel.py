import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import csv


class Travel(object):
    def __init__(self):
        self.url = "https://place.qyer.com/south-korea/citylist-0-0-{}/"
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }

    '''发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("utf-8")
        return html
        '''解析数据'''

    #
    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//ul[@class="plcCitylist"]/li')
        # 创建csv文件进行写入
        csv_file = open('scrape.csv', 'a', encoding='gbk')
        csv_writer = csv.writer(csv_file)
        # 写入csv标题头内容
        csv_writer.writerow(['城市', '景点热度', '图片链接'])
        for i in image_src_list:
            b = i.xpath('.//h3//a/text()')[0].strip()
            c = i.xpath('.//p[@class="beento"]//text()')[0].strip()
            d = i.xpath('.//p[@class="pics"]//img//@src')[0].strip()
            csv_writer.writerow([b, c, d])
        csv_file.close()

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            html = self.get_page(url)
            # print(html)
            self.parse_page(html)
            time.sleep(2)

            print("======================第%s页爬取成功！！！！=======================" % page)


if __name__ == '__main__':
    imageSpider = Travel()
    imageSpider.main()
