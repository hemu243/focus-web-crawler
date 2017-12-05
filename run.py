import os
import sys
import time
import metapy

from crawler import starCrawl

def initializedClassifier(configFile):
	"""
	Initialized classifier
	:param configFile - main config file path to load metapy settings
	:return: a classifier instance and fowardIndex instance
	"""
	# Settings log
	metapy.log_to_stderr()

	# Loading indexes
	invertedIndex = metapy.index.make_inverted_index(configFile)
	fwdIndex = metapy.index.make_forward_index(configFile)

	dset = metapy.classify.MulticlassDataset(fwdIndex)
	classifier = metapy.classify.NaiveBayes(training=dset, alpha=0.01, beta=0.01)
	return classifier, fwdIndex


	# Cross validating
	'''print('Running cross-validation...')
	start_time = time.time()
	matrix = metapy.classify.cross_validate(lambda fold:
											metapy.classify.NaiveBayes(training=fold), dset, 5)

	print(matrix)
	matrix.print_stats()
	print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))'''

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
	urls = getSeedUrls(sys.argv)
	if not urls:
		return
	classifier, fwdIndex = initializedClassifier(os.path.abspath("config.toml"))
	# TODO - get input urls as command line options
	starCrawl(input_urls=urls, classifier=classifier, fwdIndex=fwdIndex)


if __name__ == '__main__':
	main(sys.argv)