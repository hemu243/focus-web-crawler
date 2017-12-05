# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from focused_scrapy_crawler.items import FocusedScrapyCrawlerItem
import time
import metapy
import logging
from scrapy.http import Request


class NewhouseSpider(CrawlSpider):
    """
    Crawler which craw for new house urls
    """
    name = 'newhouse'

    rules = (
        Rule(LinkExtractor(unique=True), callback='parse_item', follow=False),
    )

    crawled_urls = []

    NEW_HOME_LABEL = 'NewHome'

    def __init__(self, input_urls=None, allowed_domains=None, *args, **kwargs):
        """
        Initialized crawl
        :param input_urls: comma separates list of uris
        :param allowed_domains: allowed domains
        :param args: list of args
        :param kwargs: key value args
        """
        super(NewhouseSpider, self).__init__(*args, **kwargs)
        self.start_urls = str(input_urls).split(',')
        if allowed_domains:
            self.allowed_domains = str(allowed_domains).split(',')
        # Initialized classifier
        if 'classifier' in kwargs and 'fwdIndex' in kwargs:
            self.classifier = kwargs.get('classifier')
            self.fwdIndex = kwargs.get('fwdIndex')

    def parse_item(self, response):
        """
        crawling the webpage and extracts the url.
        Once the crawling is done, evaluate the page content is relevant to new house or not
        :param response: - response of fetch
        :return: items
        """
        NewhouseSpider.crawled_urls.append(response.url)

        item = FocusedScrapyCrawlerItem()
        item['url'] = response.url
        item['body'] = self._getBody(response)
        item['page_title'] = '\n'.join(response.xpath("//h1/text()").extract())
        item['last_updated'] = time.time()

        # Update links
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
        doc.content(item['page_title'] + item['body'])
        docvec = self.fwdIndex.tokenize(doc)
        label = self.classifier.classify(docvec)
        item['label'] = label
        yield item
        if label != NewhouseSpider.NEW_HOME_LABEL:
            self.log("item={} does not belong to new home so stop crawling".format(item),
                     logging.INFO)
        else:
            for link in links:
                req = Request(link, priority=10,  # after the request is done, run parse_item to train the apprentice
                              callback=self.parse_item)
                yield req

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
