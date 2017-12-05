# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FocusedScrapyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    links = scrapy.Field()
    title = scrapy.Field()
    page_title = scrapy.Field()
    body = scrapy.Field()
    label = scrapy.Field()
    last_updated = scrapy.Field()
