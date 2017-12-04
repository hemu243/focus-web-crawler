import os
import time
import sys

import metapy

from crawler import starCrawl


def getClassifier(trainingData, invertedIndex, fwdInx):
	"""
	Return classifier object
	:param trainingData:
	:param invertedIndex:
	:param fwdInx:
	:return:
	"""
	classifier = metapy.classify.NaiveBayes(training=trainingData, alpha=0.01, beta=0.01)
	return classifier


def initializedClassifier(configFile):
	"""
	Initialized classifier
	:param configFile - main config file path to load metapy settings
	:return: a classifier object
	"""
	# Settings log
	metapy.log_to_stderr()

	# Loading indexes
	invertedIndex = metapy.index.make_inverted_index(configFile)
	fwdIndex = metapy.index.make_forward_index(configFile)

	dset = metapy.classify.MulticlassDataset(fwdIndex)

	print('Running cross-validation...')
	start_time = time.time()
	matrix = metapy.classify.cross_validate(lambda fold:
											getClassifier(fold, invertedIndex, fwdIndex), dset, 5)

	print(matrix)
	matrix.print_stats()
	print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))


def main(args):
	"""
	Main function which initialized classifier and start crawling
	:return:
	"""
	initializedClassifier(os.path.abspath("config.toml"))
	# TODO - get input urls as command line options
	starCrawl(input_urls="http://newhomesource.com", classifier=None)


if __name__ == '__main__':
	main(sys.argv)