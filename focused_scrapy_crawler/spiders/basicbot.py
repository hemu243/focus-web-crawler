# -*- coding: utf-8 -*-
import logging

import scrapy
import time


class BasicbotSpider(scrapy.Spider):
    """
    Basic bot which crawl the web pages
    """
    name = 'basicbot'

    def __init__(self, input_urls=None, allowed_domains=None, *args, **kwargs):
        """
        Initialized crawl
        :param input_urls: comma separates list of uris
        :param allowed_domains: allowed domains
        :param agrs: list of args
        :param kwargs: key value args
        """
        super(BasicbotSpider, self).__init__(*args, **kwargs)
        self.start_urls = str(input_urls).split(',')
        if allowed_domains:
            self.allowed_domains = str(allowed_domains).split(',')

    def parse(self, response):
        item = dict()
        body = '\n'.join(response.xpath('//body//p//text()').extract())
        if isinstance(body, basestring):
            # Remove spaces
            body.lstrip()
            body.rstrip()
        # Get all links
        for anchor in response.xpath('//a'):
            if not anchor.root:
                continue
            href = anchor.root.attrib.get('href')
            text = anchor.root.text
            # Convert relative href to full uri
            if href and href.startswith("/"):
                href = response.urljoin(href)
            else:
                continue
            self.log("Crawling url="+ href, logging.INFO)
            item['link'] = href
            item['text'] = text
            # TODO - tokenizer body here so we can easily construct features
            item['body'] = body
            item['page_title'] = '\n'.join(response.xpath("//h1/text()").extract())
            item['last_updated'] = time.time()
            yield item
            yield response.follow(href, callback=self.parse)

