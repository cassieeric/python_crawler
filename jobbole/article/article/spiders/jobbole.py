# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader

from article.items import JobboleArticleItem

from article.utils.common import get_md5

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/113659/']
    # start_urls = ['http://blog.jobbole.com/114706/']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # 解析所有文章的URL并且交给scrapy下载后进行解析
        selectors = response.css('div#archive .floated-thumb .post-thumb a')
        for selector in selectors:
            image_url = selector.css('img::attr(src)').extract_first("")
            post_url = selector.css('::attr(href)').extract_first("")
            # print(post_url)
            yield Request(url=parse.urljoin(response.url, post_url), meta={'front_image_url': image_url}, callback=self.parse_detail)

        # # 解析所有文章的URL并且交给scrapy下载后进行解析
        # post_url = response.css('div#archive .floated-thumb .post-thumb a').css('::attr(href)').extract_first("")
        # front_img_url = response.css('div#archive .floated-thumb .post-thumb a').css('img::attr(src)').extract_first("")
        # yield Request(url=parse.urljoin(response.url, post_url), meta={'front_img_url': front_img_url},
        #                   callback=self.parse_detail)

    # 提取下一页信息，并交给scrapy进行下载
    #     next_page_url = response.css('a.page-numbers::attr(href)').extract()[0]
    #     next_page_url = response.css('.next.page-numbers::attr(href)').extract_first("")
    #     if next_page_url:
    #         yield Request(url=parse.urljoin(response.url, next_page_url), callback=self.parse)
    #     else:
    #         print('已无下一页!')

        next_url = response.css('.next.page-numbers::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)

    def parse_detail(self, response):
        item = JobboleArticleItem()
        # 提取目标数据
        # front_img_url = response.meta["front_img_url"]
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图的URL，加入get方法，默认返回空值
        title = response.css('div.entry-header h1::text').extract()[0]
        release_date = response.css('p.entry-meta-hide-on-mobile ::text').extract()[0].replace(' ·', '').strip()
        tag = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        tags = ','.join(tag)
        voteup_num = int(response.css('span.vote-post-up h10::text').extract()[0])
        collection_num = response.css('span.bookmark-btn::text').extract()[0]
        collection_pattern = re.match('.*?(\d+).*', collection_num)
        if collection_pattern:
            collection_num = int(collection_pattern.group(1))
        else:
            collection_num = 0

        comment_num = response.css('a[href="#article-comment"] span::text').extract()[0]
        comment_pattern = re.match('.*?(\d+).*', comment_num)
        if comment_pattern:
            comment_num = int(comment_pattern.group(1))
        else:
            comment_num = 0

        content = response.css('div.entry').extract()[0]

        item["url_object_id"] = get_md5(response.url)
        item['front_image_url'] = [front_image_url]
        item['title'] = title
        item['url'] = response.url
        try:
            release_date = datetime.datetime.strftime(release_date, '%Y/%m/%d').date()
        except Exception as e:
            release_date = datetime.datetime.now().date()
        item['release_date'] = release_date
        item['tags'] = tags
        item['voteup_num'] = voteup_num
        item['collection_num'] = collection_num
        item['comment_num'] = comment_num
        item['content'] = content

        # 通过item_loader加载item
        item_loader = ItemLoader(item=JobboleArticleItem(), response=response)
        item_loader.add_css("title", "div.entry-header h1::text")
        # item_loader.add_xpath()
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("release_date", "p.entry-meta-hide-on-mobile ::text")
        item_loader.add_css("tag", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("voteup_num", "span.vote-post-up h10::text")
        item_loader.add_css("collection_num", "span.bookmark-btn::text")
        item_loader.add_css("comment_num", 'a[href="#article-comment"] span::text')
        item_loader.add_css("content", "div.entry")


        yield item

    # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
    # release_date = response.xpath(
    #     '//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].replace(' ·', '').strip()
    # tag = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
    # tags = ','.join(tag)
    #
    # voteup_num = int(response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract()[0])
    # collection_num = response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract()[0]
    # collection_pattern = re.match('.*?(\d+).*', collection_num)
    # if collection_pattern:
    #     collection_num = int(collection_pattern.group(1))
    #
    # comment_num = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
    # comment_pattern = re.match('.*?(\d+).*', comment_num)
    # if comment_pattern:
    #     comment_num = int(comment_pattern.group(1))
    #
    # content = response.xpath('//div[@class="entry"]').extract()[0]

