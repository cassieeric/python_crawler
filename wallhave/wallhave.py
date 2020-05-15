import requests
from lxml import etree
from fake_useragent import UserAgent
import time


class wallhaven(object):
    def __init__(self):
        self.url = "https://wallhaven.cc/search?q=id%3A65348&page={}"
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }
        # print(self.headers)

    '''发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("utf-8")
        return html
        '''解析数据'''

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//figure//a/@href')
        for i in image_src_list:
            html1 = self.get_page(i)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            # print(parse_html1)
            filename = parse_html1.xpath('//div[@class="scrollbox"]//img/@src')
            # print(filename)

            # 图片地址发生请求
            for img in filename:
                dirname = "./图/" + img[32:]
                html2 = requests.get(url=img, headers=self.headers).content
                with open(dirname, 'wb') as f:
                    f.write(html2)
                    print("%s下载成功" % dirname)

    def main(self):
        startPage = int(input("4K起始页:"))
        endPage = int(input("4K终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            html = self.get_page(url)
            self.parse_page(html)
            time.sleep(1.4)
            print("第%s页爬取成功！！！！" % page)


if __name__ == '__main__':
    imageSpider = wallhaven()
    imageSpider.main()
