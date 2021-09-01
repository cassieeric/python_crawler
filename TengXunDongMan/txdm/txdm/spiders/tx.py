import scrapy
from txdm.items import TxdmItem # 需要设置(注意目录结构)


count = 1
class TxSpider(scrapy.Spider):
    name = 'tx'
    allowed_domains = ['ac.qq.com']
    start_urls = ['https://ac.qq.com/Comic/index/page/1']

    def parse(self, response):

        global count
        print(count)

        count += 1
        li_list = response.xpath("//ul[@class='ret-search-list clearfix']/li")


        print('****',len(li_list),"****")
        for i in li_list:  # 遍历

            name = i.xpath("./div[2]/h3/a/text()").extract_first()  # 获取名字
            author = i.xpath("./div[2]/p[1]/text()").extract_first() # 获取作者
            types = i.xpath("./div[2]/p[2]/span[1]/text()").extract_first()  # 获取类型
            popularity = i.xpath("./div[2]/p[2]/span[3]/em/text()").extract_first() # 人气

            item = TxdmItem(imgLink=imgLink,name=name,author=author,types=types,popularity=popularity)

            yield item

        next_url = 'https://ac.qq.com/Comic/index/page/{}'.format(
            count)  # 这里的count是初始化的全局变量count,每次执行数据解析,就让他+1
        print("*"*20)
        print(next_url)
        print("*"*20)
        if count == 462:
            return None

        request = scrapy.Request(next_url)
        yield request