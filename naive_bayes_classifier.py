#
import metapy
from classifier import WebClassifier


class NaiveBayesClassifier(WebClassifier):

	def __init__(self, configFile):
		"""
		Initialized
		:param configFile: config file path
		:return:
		"""
		super(NaiveBayesClassifier, self).__init__(configFile)

	def getClassifier(self, training, fwdIndex, invertedIndex):
		"""
		This function needs to implemented  by inherit class
		:param training: training set
		:param fwdIndex: fwdIndex created by metapy
		:param invertedIndex: inverted index created by metapy
		:return: classifier instance
		"""
		return metapy.classify.NaiveBayes(training=training, alpha=0.01, beta=0.01)

	def score(self, link_text, page_title, body_text):
		"""
		Should implemented by inherit class
		:param link_text: url link text (anchor text)
		:param page_title: page title
		:param body_text: body text
		:return: double score value between 0 - 1
		"""
		doc = metapy.index.Document()
		doc.content(link_text + page_title + body_text)
		docvec = self.fwdIndex.tokenize(doc)
		label = self.classifier.classify(docvec)
		if label == "NewHome":
			return 1.0
		elif label == "NotNewHome":
			return 0.0
		else:
			return 0.5
