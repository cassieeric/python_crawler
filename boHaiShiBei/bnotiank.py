import requests, os,time
from lxml import etree
from fake_useragent import UserAgent


class bnotiank(object):
    def __init__(self):
        self.url = "https://bh.sb/page/{}/"
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,
            }
            # os.mkdir("新闻图片")  # 在创建文件夹 记住只有第一次运行加上，如果多次运行请注释掉本行。

    '''发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("utf-8")
        return html
        '''解析数据'''

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//p/a/@href')
        # print(image_src_list)
        for i in image_src_list:
            # print(i)
            html1 = self.get_page(i)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            reo = parse_html1.xpath('//div//div[@class="content"]')
            for j in reo:
                d = j.xpath('.//article[@class="article-content"]//p/img/@src')[0]
                text = parse_html1.xpath('//h1[@class ="article-title"] //a/text()')[0].strip()
                html2 = requests.get(url=d, headers=self.headers).content
                dirname = "./d/" + text + ".jpg"
                with open(dirname, 'wb') as f:
                    f.write(html2)
                    print("%s 【下载成功！！！！】" % text)
    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            html = self.get_page(url)
            time.sleep(1)
            """时间延时"""
            self.parse_page(html)
            print("======================第%s页爬取成功！！！！=======================" % page)


if __name__ == '__main__':
    imageSpider = bnotiank()
    imageSpider.main()
