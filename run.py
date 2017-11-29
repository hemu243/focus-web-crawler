from scrapy.crawler import CrawlerProcess
from focused_scrapy_crawler.focused_scrapy_crawler.spiders.basicbot import BasicbotSpider

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(BasicbotSpider, input_urls="http://newhomesource.com")
process.start() # the script will block here until the crawling is finished