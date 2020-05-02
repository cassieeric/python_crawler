import requests
from lxml import etree
from fake_useragent import UserAgent
import time


class kitchen(object):
    u = 0;

    def __init__(self):
        self.url = "https://www.xiachufang.com/explore/?page={}"
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
        image_src_list = parse_html.xpath('//li/div/a/@href')
        for i in image_src_list:
            url = "https://www.xiachufang.com/" + i
            # print(url)
            html1 = self.get_page(url)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            # print(parse_html1)

            num = parse_html1.xpath('.//h2[@id="steps"]/text()')[0].strip()
            name = parse_html1.xpath('.//li[@class="container"]/p/text()')
            ingredients = parse_html1.xpath('.//td//a/text()')
            self.u += 1;
            # print(self.u)
            # print(str(self.u)+"."+house_dict["名 称 :"]+":")
            # da=tuple(house_dict["材 料:"])
            food_info = '''  
第 %s 种
           
菜 名 : %s
原 料 : %s
下 载 链 接 : %s,
=================================================================
                    ''' % (str(self.u), num, ingredients, url)
            # print(food_info)
            f = open('下厨房/菜谱.doc', 'a', encoding='utf-8')  # 以'w'方式打开文件
            f.write(str(food_info))
            print(str(food_info))
            f.close()

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            html = self.get_page(url)
            self.parse_page(html)
            time.sleep(1.4)
            print("====================================第 %s 页 爬 取 成 功====================================" % page)


if __name__ == '__main__':
    imageSpider = kitchen()
    imageSpider.main()
