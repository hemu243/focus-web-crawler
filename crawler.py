from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


def cleanFile(filepath):
	"""
	clean file
	:param filepath: file path to clean
	:return: None
	"""
	with open(filepath, "r+") as fp:
		fp.truncate()


def startCrawl(input_urls="http://newhomesource.com", classifier=None):
	"""
	Start web crawler using seed urls and classifier instance
	Note - this function block the process because crawl will keep running until
	it is being stopped
	:param input_urls: seed urls separated by ,
	:param classifier: classifier instance
	:return: Nothing
	"""
	os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'focused_scrapy_crawler.settings')

	# clean output file
	cleanFile("output/newhouse_output_all.txt")
	cleanFile("output/newhouse_output_positive_score.txt")
	cleanFile("output/log/newhouse_output_positive_score.txt")

	# Create Crawl Process which also start twisted reactor
	process = CrawlerProcess(get_project_settings())
	# Pointed out bot which I am running
	process.crawl('newhouse', input_urls, classifier=classifier)

	# Start
	process.start() # the script will block here until the crawling is finished
#
