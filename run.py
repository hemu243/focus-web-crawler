import os
import sys

from naive_bayes_classifier import NaiveBayesClassifier

from crawler import starCrawl


def getSeedUrls(args):
	"""
	Validate inputs params and return seed urls
	:param args: list of args passed in the command line
	:return:
	"""
	if len(args) < 2:
		print "\033[91m Error: Invalid invocation of script \033[0m \n" \
			  "\033[95m------ Usage: ------ \033[0m \n \033[93m {0} seed_url1,seed_urls2 \033[0m \n \n \nExample:\n {0} http://newhomesource.com".format(args[0])
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
	# TODO - get input urls as command line options
	starCrawl(input_urls=urls, classifier=classifier)


if __name__ == '__main__':
	main(sys.argv)