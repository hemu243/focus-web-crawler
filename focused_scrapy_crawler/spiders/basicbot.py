# -*- coding: utf-8 -*-
import logging

import scrapy
import time
import metapy


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
        # Initialized classifier
        if 'classifier' in kwargs and 'fwdIndex' in kwargs:
            self.classifier = kwargs.get('classifier')
            self.fwdIndex = kwargs.get('fwdIndex')

    def _getBody(self, response):
        """
        Get all text data of response
        :param response: response object
        :return: basestring
        """
        body = '\n'.join(response.xpath('//body//p//text()').extract())
        # Some cleaning is being done
        if isinstance(body, basestring):
            # Remove spaces
            body.lstrip()
            body.rstrip()
        return body

    def parse(self, response):
        """
        Function which parse the response after fetching response from given url
        :param response:
        :return:
        """
        item = dict()
        item['body'] = self._getBody(response)
        item['page_title'] = '\n'.join(response.xpath("//h1/text()").extract())
        item['last_updated'] = time.time()
        # Get all links of the pages
        links = []
        for anchor in response.xpath('//a'):
            if anchor.root is not None:
                continue
            link = {}
            href = anchor.root.attrib.get('href')
            text = anchor.root.text
            # Convert relative href to full uri
            if href and href.startswith("/"):
                href = response.urljoin(href)
            else:
                continue
            link['link'] = href
            link['text'] = text
            link['last_updated'] = time.time()
            links.append(link)
        item['links'] = links
        # Feature page title and content of the page
        doc = metapy.index.Document()
        doc.content(item['page_title'])
        docvec = self.fwdIndex.tokenize(doc)
        label = self.classifier.classify(docvec)
        if label != "NewHome":
            self.log("item={} does not belong to new home so stop crawling".format(item),
                     logging.INFO)
        else:
            pass
            #for link in links:
            #    yield response.follow(link, callback=self.parse)
        item['label'] = label
        yield item


