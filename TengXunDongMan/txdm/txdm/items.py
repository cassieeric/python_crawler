# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TxdmItem(scrapy.Item):
    # define the fields for your item here like
    name = scrapy.Field()
    author = scrapy.Field()
    types = scrapy.Field()
    popularity = scrapy.Field()
    pass
