# -*- coding: utf-8 -*-
import logging

import scrapy
from scrapy.spiders import Rule

class BasicbotSpider(scrapy.Spider):
    name = 'basicbot'
    allowed_domains = ['newhomesource.com']
    start_urls = ['http://www.newhomesource.com/']

    '''def parse(self, response):
        pass

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )'''

    def parse(self, response):
        #item = dict()
        #item['url'] = response.url
        #item['title'] = response.meta['link_text']
        # extracting basic body
        #item['body'] = '\n'.join(response.xpath('//text()').extract())
        #self.log('\n'.join(response.xpath('//text()').extract()), logging.INFO)
        self.log('\n'.join(response.xpath('//body//p//text()').extract()), logging.INFO)
        # or better just save whole source
        #item['source'] = response.body
        #yield item
        for href in response.xpath('//a/@href').extract():
            # Handle relative uri
            if href.startswith("/"):
                href = response.url + href
            self.log("Crawling url=" + href, logging.INFO)
            #yield response.follow(href, callback=self.parse)

