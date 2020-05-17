import requests
from lxml import etree
# 网站  ： url
import ssl  # ssl验证

ssl._create_default_https_context = ssl._create_unverified_context


class Panda(object):
    def __init__(self):
        self.url = "https://www.tukuppt.com/yinxiaomuban/zhuanchang/__zonghe_0_0_0_0_0_0_{}.html" #/zhuanchang/:搜索的名字的拼音缩写
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }

    def get_page(self, url):
        req = requests.get(url=url, headers=self.headers)
        html = req.content.decode("utf-8")
        return html

    def page_page(self, html):
        parse_html = etree.HTML(html)
        one = parse_html.xpath('//div[@class="b-box"]//dl')
        for li in one:
            lis_imges = li.xpath(".//audio//source/@src")[0].strip()
            who = li.xpath(".//dt//a/text()")[0].strip()
            mp3 = "https:" + lis_imges
            # print(str(mp3));
            dirname = "./音效/" + who + '.mp3'
            html2 = requests.get(url=mp3, headers=self.headers).content
            with open(dirname, 'wb') as f:
                f.write(html2)
                print("\n%s下载成功" % who)

    def main(self):
        print("\n" + "*" * 10 + '【音效】' + "*" * 10)
        stat = int(input("输 入 开 始 :"))
        end = int(input("输 入 结 束:"))
        for page in range(stat, end + 1):
            url = self.url.format(page)
            # print(url)
            html = self.get_page(url)
            self.page_page(html)
            print("==================第%s页爬取成功！！！！=====================" % page)


if __name__ == '__main__':
    Siper = Panda()
    Siper.main()
