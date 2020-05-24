import requests
from lxml import etree
import time
import ssl  # ssl验证

ssl._create_default_https_context = ssl._create_unverified_context


class Emoticon(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.url = 'https://www.doutula.com/photo/list/?page={}'

    # 线程事件函数(请求,解析提取数据)
    def get_page(self, url):
        req = requests.get(url=url, headers=self.headers)
        html = req.content.decode("utf-8")
        return html

    # 解析函数
    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image = parse_html.xpath('//ul[@class="list-group"]/li/div/div//a')
        for i in image:
            image_src_list = i.xpath('.//img/@data-original')[0]
            image_name = i.xpath('.//img//@alt')[0]
            print(image_src_list)

            html2 = requests.get(url=image_src_list, headers=self.headers).content
            name = "/图/" + image_src_list[-20:]
            print(name[-10:])
            with open(name[-10:], 'wb') as f:
                f.write(html2)
                print("%s 【下载成功！！！！】" % image_name)
                print("==================================")

    # 主函数
    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1, 20):
            url = self.url.format(page)
            # print(url)
            html = self.get_page(url)
            self.parse_page(html)
            print("======================第%s页爬取成功！！！！=======================" % page)


if __name__ == '__main__':
    start = time.time()
    spider = Emoticon()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end - start))
