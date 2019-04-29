# -*- coding: utf-8 -*-
import json
import logging
import os
import re

import scrapy
from project.items import ProjectItem
from scrapy.shell import inspect_response
from lxml import html
from project.parts import parts

# parts = {'火箭专区': 'https://bbs.hupu.com/rockets'}


class Spider(scrapy.Spider):
    name = 'test'

    if not os.path.exists('results'):
        os.mkdir('results')

    if os.path.exists('LOG.log'):
        open('LOG.log', 'w').close()

    custom_settings = {
        'ITEM_PIPELINES': {
            'project.pipelines.ProjectPipeline': 300,
        },
        # 'DOWNLOADER_MIDDLEWARES': {
        #     'project.middlewares.ProxyMiddleware': 740,
        #     # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 关闭默认方法
        #     # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,  # 开启
        # },

        # 'JOBDIR': 'crawl/test',

        'LOG_ENABLED': True,
        'LOG_LEVEL': logging.INFO,
        # 'LOG_FILE':'LOG.log',

        # 'HTTPERROR_ALLOWED_CODES': [407],
        # 'HTTPERROR_ALLOW_ALL': True,  # 这样本身就可以禁止重定向

        # 'AUTOTHROTTLE_ENABLED': True,
        # 'AUTOTHROTTLE_START_DELAY': 1,
        # 'AUTOTHROTTLE_MAX_DELAY': 10,
        # 'AUTOTHROTTLE_TARGET_CONCURRENCY': 6,
        # 'AUTOTHROTTLE_DEBUG': False  # INFO: slot: book.douban.com
    }

    def start_requests(self):

        # for part, link in parts.items():
        # open('results/{}.txt'.format(part), 'w').close()
        # for i in range(2, 3):  # 爬前十页
        #     yield scrapy.Request('https://bbs.hupu.com/rockets-{}'.format(i), meta={'part': '火箭专区'})
        # yield scrapy.Request('https://bbs.hupu.com/26073334.html', meta={'part': '火箭专区'}, callback=self.comment())
        item = ProjectItem()
        item['id'] = '26073334'
        item['comment'] = []
        item['part'] = '火箭专区'
        item['title'] = '【一图流】哈登压哨后撤三分命中'
        item['author'] = 'LonzoBa'
        item['reply_count'] = 0
        item['link_count'] = 0
        item['view_count'] = 0
        yield scrapy.Request('https://m.hupu.com/api/bbs/replies/26073334-1',
                             meta={'item': item, 'total_page': 1, 'page': 1},
                             callback=self.comment)

    def parse(self, response):
        part = response.meta['part']
        # inspect_response(response, self)
        for li in response.xpath('//ul[@class="for-list"]/li')[1:2]:
            item = ProjectItem()
            item['part'] = part
            item['title'] = li.xpath('div[@class="titlelink box"]/a[@class="truetit"]//text()').get().strip().replace(
                '\n', ' ')
            href = li.xpath('div[@class="titlelink box"]/a[@class="truetit"]/@href').get()
            item['href'] = 'https://bbs.hupu.com' + href
            item['id'] = re.search(r'\d+', href).group()
            item['author'] = li.xpath('div[@class="author box"]/a[@class="aulink"]/text()').get()
            item['reply_count'] = li.xpath('span[@class="ansour box"]/text()').get().split('\xa0')[0]
            item['view_count'] = li.xpath('span[@class="ansour box"]/text()').get().split('\xa0')[-1]

            link_count_text = li.xpath('div[@class="titlelink box"]/span[@class="light_r  "]/a/@title').get()
            if link_count_text:
                link_count = re.search(r'\d+', link_count_text).group()
            else:
                link_count = 0
            item['link_count'] = link_count
            item['comment'] = []
            # yield item
            total_page = (int(item['reply_count']) - 1) // 20 + 1
            print('{},{},{},{},{},{},{}, 总页数:{}'.format(item['id'], item['href'], item['title'], item['author'],
                                                        item['reply_count'], item['view_count'], item['link_count'],
                                                        total_page))

            if item['reply_count'] != '0':
                yield scrapy.Request('https://m.hupu.com/api/bbs/replies/{}-1'.format(item['id']),
                                     meta={'item': item, 'total_page': total_page, 'page': 1},
                                     callback=self.comment)

    def comment(self, response):
        meta = response.meta
        item = meta['item']
        total_page = meta['total_page']
        page = meta['page']

        if page <= total_page:
            for reply in json.loads(response.text)['data']['replies']:
                # 评论内容
                if reply['content'].strip() and reply['is_ban'] == 0:  # 有些评论会被禁止,不显示
                    result = ' '.join(
                        [text.strip() for text in html.fromstring(reply['content'].strip()).xpath('//text()')])
                    # item['comment'].append(result)

                    # 认可数
                    item['comment_light'] = reply['light']
                    # 评论者
                    item['comment_author'] = reply['author']
                    # 引用
                    if reply['quote']:  # 有引用
                        item['comment_quote_author'] = html.fromstring(reply['quote'][0]['header'][0].strip()).xpath(
                            '//a//text()')
                        item['comment_quote_content'] = ' '.join([text.strip() for text in html.fromstring(
                            reply['quote'][0]['content'].strip()).xpath('//text()')])
                    else:
                        item['comment_quote_author'] = ''
                        item['comment_quote_content'] = ''

                    # print([item['part'], item['title'], item['author'], item['reply_count'], item['link_count'],
                    #        item['view_count']])
                    item['comment'].append(
                        {'comment_author': item['comment_author'],
                         'comment_light': item['comment_light'],
                         'comment': result,
                         'comment_quote_author': item['comment_quote_author'],
                         'comment_quote_content': item['comment_quote_content']})
                    # print('=====================')

            # for comment in item['comment']:
            #     if comment['comment_quote_author']:  # 有引用
            #         print('评论者:{}, 认可数:{},评论:{}\n引用者:{}, 引用内容:{}\n======'.format(comment['comment_author'],
            #                                                                      comment['comment_light'],
            #                                                                      comment['comment'],
            #                                                                      comment['comment_quote_author'],
            #                                                                      comment['comment_quote_content']))
            #     else:
            #         print('评论者:{}, 认可数:{},评论:{}\n======'.format(comment['comment_author'],
            #                                                     comment['comment_light'],
            #                                                     comment['comment'],
            #                                                     ))

            yield scrapy.Request('https://m.hupu.com/api/bbs/replies/{}-{}'.format(item['id'], page + 1),
                                 meta={'item': item, 'total_page': total_page, 'page': page + 1},
                                 callback=self.comment)
        else:
            yield item

        # with open('results.txt', 'w', encoding='utf-8') as f:
        #     f.write('\n\n'.join(results))
