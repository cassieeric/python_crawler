import requests
from lxml import etree
from fake_useragent import UserAgent
class xiaoshuo(object):
    def __init__(self):
        self.url = "https://www.555x.org/html/wuxiaxianxia/list_29_{}.html"
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

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//li[@class="qq_g"]/a/@href')
        for i in image_src_list:
            html1 = self.get_page(i)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            # print(parse_html1)
            dwom = parse_html1.xpath('//div[@class="downbox"]/a[1]/@href')

            # print(dwom)
            for tow in dwom:
                # print(tow)
                html2 = self.get_page(tow)  # 第二个发生请求
                parse_html2 = etree.HTML(html2)
                # print(parse_html1)
                three = parse_html2.xpath('//div[@class="xiazai"]')
                for rd in three:
                    b = rd.xpath('..//div[@class="shutou"]//b/text()')[0].strip()
                    tress = rd.xpath('..//div[@class="shuji"]//ul/li/a/@href')[0].strip()
                    # print(tress)
                    read = '''
《%s》 下 载 链 接 : %s ''' % (b, tress)
            print(read)

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            html = self.get_page(url)
            self.parse_page(html)
            print("======================第%s页爬取成功！！！！=======================" % page)

if __name__ == '__main__':
    imageSpider = xiaoshuo()
    imageSpider.main()
