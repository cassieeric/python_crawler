import requests
from lxml import etree
from fake_useragent import UserAgent


# 网站  ： url
class Mikan(object):
    def __init__(self):
        self.url = "https://mikanani.me/Home/Classic/{}"  # /zhuanchang/:搜索的名字的拼音缩写
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }

    def get_page(self, url):
        req = requests.get(url=url, headers=self.headers)
        html = req.content.decode("utf-8")
        return html

    def page_page(self, html):
        parse_html = etree.HTML(html)
        one = parse_html.xpath('//tbody//tr//td[3]/a/@href')
        for li in one:
            yr = "https://mikanani.me" + li
            # print(yr)
            html2 = self.get_page(yr)  # 第二个发生请求
            parse_html2 = etree.HTML(html2)

            tow = parse_html2.xpath('//body')
            for i in tow:
                four = i.xpath('.//p[@class="episode-title"]//text()')[0].strip()
                fif = i.xpath('.//div[@class="leftbar-nav"]/a[1]/@href')[0].strip()
                # print(four)
                t = "https://mikanani.me" + fif
                print(t)
                dirname = "./种子/" + four[:15] + four[-20:] + '.torrent'
                # print(dirname)
                html3 = requests.get(url=t, headers=self.headers).content
                with open(dirname, 'wb') as f:
                    f.write(html3)
                    print("\n%s下载成功" % four)

    def main(self):
        stat = int(input("start :"))
        end = int(input(" end:"))
        for page in range(stat, end + 1):
            url = self.url.format(page)
            print(url)
            html = self.get_page(url)
            self.page_page(html)
            print("==================第%s页爬取成功！！！！=====================" % page)


if __name__ == '__main__':
    Siper = Mikan()
    Siper.main()
