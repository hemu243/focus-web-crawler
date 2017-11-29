from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Workaround to point out project settings
import os


if __name__ == '__main__':
	os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'focused_scrapy_crawler.settings')


	# Create Crawl Process which also start twisted reactor
	process = CrawlerProcess(get_project_settings())
	# Pointed out bot which I am running
	# TODO - get input urls as command line options
	process.crawl('basicbot', input_urls="http://newhomesource.com")

	# Start
	process.start() # the script will block here until the crawling is finished