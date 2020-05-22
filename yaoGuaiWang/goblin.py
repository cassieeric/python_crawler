import requests, os
from lxml import etree
from fake_useragent import UserAgent
import time


class goblin(object):
    def __init__(self):
        self.url = "http://www.cbaigui.com/?paged={}"
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,
                'Host': 'www.cbaigui.com',
                'Referer': 'http: // www.cbaigui.com /?paged={}'
            }
        os.mkdir("妖怪")  # 创建妖怪这个文件夹 记住只有第一次运行加上，如果多次运行请屏蔽掉本行

    '''发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("utf-8")
        return html
        '''解析数据'''

    #
    def parse_page(self, html):
        parse_html = etree.HTML(html)
        t = parse_html.xpath('//div[@class="post-inner post-hover"]/h2')
        for i in t:
            goblin_herf = i.xpath('./a/@href')[0].strip()  # 二级页面链接
            name = i.xpath('.//a/text()')[0].strip()  # 对应文件夹的名字
            os.mkdir("././妖怪/{}".format(name))  # 拼接文件夹
            print(name, goblin_herf)
            html2 = self.get_page(goblin_herf)  # 第二个发生请求
            parse_html2 = etree.HTML(html2)
            r = parse_html2.xpath('//div[@class="entry"]/p/text()')
            for rte in r:
                # print(rte)w
                try:
                    with open("./妖怪/{}/{}.txt".format(name, name), "a", encoding='utf-8') as f:
                        f.write(rte)  # 把内容存储到对应名字的文件里
                except OSError:
                    pass
                continue

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            print(url)
            html = self.get_page(url)
            self.parse_page(html)
            time.sleep(1)
            print("======================第%s页爬取成功！！！！=======================" % page)


if __name__ == '__main__':
    imageSpider = goblin()
    imageSpider.main()
