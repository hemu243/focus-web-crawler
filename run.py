import os
import sys

from naive_bayes_classifier import NaiveBayesClassifier

from crawler import startCrawl


def getSeedUrls(args):
	"""
	Validate inputs params and return seed urls
	:param args: list of args passed in the command line
	:return:
	"""
	if len(args) < 2:
		print "\033[91m Error: Seed urls needs to be passed to the script \033[0m \n" \
			  "\033[95m------ Usage: ------ \033[0m \n \033[93m python {0} seed_url1,seed_urls2 \033[0m \n \n \nExample:\n python {0} http://newhomesource.com,https://stackoverflow.com".format(args[0])
		return None
	return args[1]


def main(args):
	"""
	Main function which initialized classifier and start crawling
	:return:
	"""
	urls = getSeedUrls(args)
	if not urls:
		return
	classifier = NaiveBayesClassifier(os.path.abspath("config.toml"))
	startCrawl(input_urls=urls, classifier=classifier)


if __name__ == '__main__':
	main(sys.argv)