import requests
from lxml import etree
from fake_useragent import UserAgent


# 网站  ： url
class Zhaopin(object):
    def __init__(self):
        self.url = "https://gz.58.com/job/pn2/?param7503=1&from=yjz2_zhaopin&PGTID=0d302408-0000-3efd-48f6-ff64d26b4b1c&ClickID={}"  # /zhuanchang/:搜索的名字的拼音缩写
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
        one = parse_html.xpath('//div[@class="main clearfix"]//div[@class="leftCon"]/ul/li')
        for l in one:
            o = l.xpath('.//a/span[1]/text()')[0].strip()
            t = l.xpath('.//a//span[@class="name"]/text()')[0].strip()
            f = l.xpath('.//p[@class="job_salary"]/text()')
            thr = l.xpath('.//div[@class="comp_name"]//a/text()')[0].strip()
            for e in f:
                boss = '''  

 %s:||%s: 
 公司：%s,
 工资：%s元/月
 =========================================================
                                ''' % (o, t, thr, e)
            # print(food_info)
            f = open('g.txt', 'a', encoding='utf-8')  # 以'w'方式打开文件
            f.write(str(boss))
            print(str(boss))
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
    Siper = Zhaopin()
    Siper.main()
