import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/films?showType=2&offset={}'
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }
        # 添加计数(页数)
        self.page = 1

    # 获取页面
    def get_page(self, url):
        # random.choice一定要写在这里,每次请求都会随机选择
        res = requests.get(url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    # 解析页面
    def parse_page(self, html):
        # 　创建解析对象
        parse_html = etree.HTML(html)
        # 基准xpath节点对象列表
        dd_list = parse_html.xpath('//dl[@class="movie-list"]//dd')
        print(len(dd_list))
        movie_dict = {}
        # 依次遍历每个节点对象,提取数据
        for dd in dd_list:
            name = dd.xpath('.//div[@class="movie-hover-title"]//span[@class="name noscore"]/text()')[0].strip()
            star = dd.xpath('.//div[@class="movie-hover-info"]//div[@class="movie-hover-title"][3]/text()')[1].strip()
            type = dd.xpath('.//div[@class="movie-hover-info"]//div[@class="movie-hover-title"][2]/text()')[1].strip()
            dowld=dd.xpath('.//div[@class="movie-item-hover"]/a/@href')[0].strip()
            # print(movie_dict)
            movie = '''【即将上映】
            
电影名字: %s

主演：%s

类型：%s
详情链接：https://maoyan.com%s
=========================================================
                                   ''' % (name, star, type,dowld)
            print(movie)

    # 主函数
    def main(self):
        for offset in range(0, 90, 30):
            url = self.url.format(str(offset))
            self.get_page(url)
            # print("hgkhgkk")
            print(url)
            print('第%d页完成' % self.page)
            time.sleep(random.randint(1, 3))
            self.page += 1


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()
