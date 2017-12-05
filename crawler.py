from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import metapy

"""
Module which start crawling using seeds urls and classifier
"""

def starCrawl(input_urls="http://newhomesource.com", classifier=None, fwdIndex=None):
	"""
	Start web crawler using seed urls and classifier instance
	Note - this function block the process because crawl will keep running until
	it is being stopped
	:param input_urls: seed urls separated by ,
	:param classifier: classifier instance
	:return: Nothing
	"""
	os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'focused_scrapy_crawler.settings')

	# Create Crawl Process which also start twisted reactor
	process = CrawlerProcess(get_project_settings())
	# Pointed out bot which I am running
	process.crawl('newhouse', input_urls, classifier=classifier, fwdIndex=fwdIndex)

	# Start
	process.start() # the script will block here until the crawling is finished
#
