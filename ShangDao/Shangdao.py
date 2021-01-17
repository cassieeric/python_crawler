import requests
from lxml import etree
from fake_useragent import UserAgent

# 网站  ： url
class Shangdao(object):
    def __init__(self):
        self.url = "http://www.daogame.cn/qudao-p-2.html?s=/qudao-p-{}.html"  # /zhuanchang/:搜索的名字的拼音缩写
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
        one = parse_html.xpath('//h2/a/text()')
        for i in one:
            print(i)
            f = open('公司.doc', 'a', encoding='utf-8')  # 以'w'方式打开文件
            f.write(str(i))

            f.write("\n")  # 键和值分行放，键在单数行，值在双数行
        f.close()
    def main(self):
        stat = int(input("输 入 开 始 （2开始）:"))
        end = int(input("输 入 结 束:"))
        for page in range(stat, end + 1):
            url = self.url.format(page)
            print(url)
            html = self.get_page(url)
            self.page_page(html)
            print("==================第%s页爬取成功！！！！=====================" % page)
if __name__ == '__main__':
    Siper = Shangdao()
    Siper.main()
