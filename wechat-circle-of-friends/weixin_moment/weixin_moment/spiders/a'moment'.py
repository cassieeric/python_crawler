# -*- coding: utf-8 -*-
import scrapy
import json
import re
from weixin_moment.items import WeixinMomentItem


class AmomentSpider(scrapy.Spider):
    name = 'moment'
    allowed_domains = ['chushu.la']
    start_urls = ['http://chushu.la/']

    bookid = '071569794'  # 请填写【出书啦】返回链接中的数字部分

    def start_requests(self):
        """
        使用get方式请求导航数据包
        """
        url = 'https://chushu.la/api/book/chushula-{0}?isAjax=1'.format(self.bookid)  # 获取目录的url
        yield scrapy.Request(
            url,
            headers={
                'Referer': 'https://chushu.la/book/chushula-071569794',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            },
            callback=self.parse)

    def parse(self, response):
        """
        处理获取到的导航数据包
        """
        json_body = json.loads(str(response.text))  # 加载json数据包
        catalogs = json_body['book']['catalogs']  # 获取json中的目录数据包
        url = 'https://chushu.la/api/book/wx/chushula-{}/pages?isAjax=1'.format(self.bookid)  # 分页数据url
        start_page = int(catalogs[0]['month'])  # 获取起始月份作为index传值
        for catalog in catalogs:
            year = catalog['year']
            month = catalog['month']
            formdata = {
                "type": 'year_month',
                "year": str(year),
                "month": str(month),
                "index": str(start_page),
                "value": 'v_{0}{1}'.format(year, month)
            }
            start_page += 1

            yield scrapy.FormRequest(
                url,
                method='POST',
                body=json.dumps(formdata),
                headers={
                    'Host': 'chushu.la',
                    'Connection': 'keep-alive',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Origin': 'https://chushu.la',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                    'Content-Type': 'application/json',
                    # 'Referer': 'https://chushu.la/book/chushula-071569794',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    # 'Cookie': 'Hm_lvt_a64b0c58cf35c32b2f7fd256b188b238=1525744133; _token=ac9ba3520ffd752044df52bc94134ccb; JSESSIONID=5E9A48443EB7A309DBF7E9BBCE15B21C'
                    'Cookie': 'JSESSIONID=0BC643B0058EFB3B78E8DC432FF0DDB4; Hm_lvt_a64b0c58cf35c32b2f7fd256b188b238=1540108405; Hm_lpvt_a64b0c58cf35c32b2f7fd256b188b238=1540108452; _token=18fdab5b2676aaa1d3988adf1812c722'
                },
                callback=self.parse_moment)

    def parse_moment(self, response):
        """
        朋友圈数据处理
        """
        # json_body = json.loads(response.body)
        json_body = json.loads(response.text)
        pages = json_body['pages']
        # print(pages)
        pattern = re.compile(u"[\u4e00-\u9fa5]+")  # 匹配中文
        items = WeixinMomentItem()
        for page in pages:
            if (page['type'] == "weixin_moment_page"):  # 仅抓取朋友圈分页数据
                # paras = page['data']['paras']
                for i in range(0, 6):
                    paras = page['data']['moments'][i]['paras']
                    if paras:
                        moment = ''
                        for content in paras[0]['rows']:
                            result = re.findall(pattern, content['data'])  # 使用正则匹配所有中文朋友圈
                            moment += ''.join(result)
                        items['moment'] = moment
                        # items['date'] = page['data']['moments'][0]['dateText']  # 获取时间
                        items['date'] = page['data']['pubTime']  # 获取时间
                        yield items
                    else:
                        pass

                # paras_moments = page['data']['moments']
                # for paras in paras_moments:
                #     if paras:
                #         moment = ''
                #         for content in paras[0]['rows']:
                #             result = re.findall(pattern, content['data'])  # 使用正则匹配所有中文朋友圈
                #             moment += ''.join(result)
                #         items['moment'] = moment
                #         # items['date'] = page['data']['moments'][0]['dateText']  # 获取时间
                #         items['date'] = page['data']['pubTime']  # 获取时间
                #         yield items
                #     else:
                #         pass

