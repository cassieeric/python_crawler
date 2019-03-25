# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    part = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()
    href = scrapy.Field()
    author = scrapy.Field()
    reply_count = scrapy.Field()
    view_count = scrapy.Field()
    link_count = scrapy.Field()
    comment = scrapy.Field()
    comment_light = scrapy.Field()
    comment_author = scrapy.Field()
    comment_quote_author = scrapy.Field()
    comment_quote_content = scrapy.Field()
