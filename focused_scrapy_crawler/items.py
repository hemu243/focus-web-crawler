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
    link_text = scrapy.Field()
    body_p_tags = scrapy.Field()
    head_title = scrapy.Field()
    score = scrapy.Field()
    last_crawled = scrapy.Field()
