import requests
from lxml import etree
from pprint import pprint


"""

https://go.hao123.com/ticket?city=%E5%B9%BF%E5%B7%9E&theme=all&pn=2
https://go.hao123.com/ticket?city=%E5%B9%BF%E5%B7%9E&theme=all&pn=3

"""
class HaoTripSpider(object):
    def __init__(self):
        """准备url地址"""
        self.url="https://go.hao123.com/ticket?city=广州&pn={}"
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
    '''发送请求  获取响应'''
    def get_page(self,url):
        res=requests.get(url=url,headers=self.headers)
        html=res.content.decode("utf-8")
        self.parse_page(html)
    '''解析数据'''
    def parse_page(self,html):
        '''创建解析对象'''
        parse_html=etree.HTML(html)
        '''获取二级页面链接'''
        link=parse_html.xpath('//div[@class="info-item"]//div[@class="info g-ib"]/a[@class="title g-ib g-tover"]/@href')
        for l in link:
            '''发送请求  获取响应'''
            html1=requests.get(url=l,headers=self.headers).content.decode('utf-8')
            parse_html1 = etree.HTML(html1)
            list={}
            str1=parse_html1.xpath('//div[@class="info_r"]//h3[@class="s_name"]/text()|//div[@class="brief-box clearfix"]//div[@class="brief-right"]/h2/text()')
            str2=parse_html1.xpath('//div[@class="info_r"]//p[@class="s_com open_time canhover"]//span/text()|//div[@class="brief-right"]//span[@data-reactid="51"]/text()')
            str3=parse_html1.xpath('//div[@class="s_comment"]/div[@class="s_comment_i"]/text()')
            str4=parse_html1.xpath('//div[@class="s_price"]/div[@class="s_p_t"]//b/text()|//td[@class="td5"]//strong[@class="ttd-fs-24"]/text()')
            if len(str1)!=0:
                list['景点名称']=str1[0].strip()
            else:
                list['景点名称'] = "null"
            if len(str2)!=0:
                list['开放时间']=str2[0].strip()
            else:
                list['开放时间'] = "null"
            if len(str3)!=0:
                list['精彩点评']=str3[0].strip()
            else:
                list['精彩点评'] = "null"
            if len(str4)!=0:
                list['价格']=str4[0].strip()
            else:
                list['价格'] = "null"
            print(list)
    def main(self):
        startPage=int(input("请输入起始页:"))
        endPage=int(input("请输入终止页:"))
        for page in range(startPage,endPage+1):
            url=self.url.format(page)
            html=self.get_page(url)
            print(page)
if __name__ == '__main__':
    haotripSpider=HaoTripSpider()
    haotripSpider.main()
