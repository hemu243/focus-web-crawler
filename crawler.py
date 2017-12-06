from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import logging

"""
Module which start crawling using seeds urls and classifier
"""

'''from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log/focused_crawler.log',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)'''

'''
def setup_logging(log_name, logger_name, logger=None, level=logging.INFO, is_console_header=False,
                  log_format='%(asctime)s %(levelname)s [%(name)s] [%(module)s] [%(funcName)s] [%(process)d]'
                             ' %(message)s', is_propagate=False):

    if log_name is None or logger_name is None:
        raise ValueError("log_name or logger_name is not specified")

    if logger is None:
        # Logger is singleton so if logger is already defined it will return old handler
        logger = logging.getLogger(logger_name)

    logger.propagate = is_propagate  # Prevent the log messages from being duplicated in the python.log file
    logger.setLevel(level)

    file_handler = logging.handlers.RotatingFileHandler(make_splunkhome_path(['var', 'log', 'splunk', log_name]),
                                                            maxBytes=2500000, backupCount=5)
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console stream handler
        if is_console_header:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(log_format))
            logger.addHandler(console_handler)
            
    return logger
'''


def starCrawl(input_urls="http://newhomesource.com", classifier=None):
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
	process.crawl('newhouse', input_urls, classifier=classifier)

	# Start
	process.start() # the script will block here until the crawling is finished
#
