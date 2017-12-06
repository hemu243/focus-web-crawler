# 
from abc import ABCMeta
import metapy


class WebClassifier(object):
	"""
	This module is abstract module which needs to be called by
	inherit
	"""
	__metaclass__ = ABCMeta

	def __init__(self, configFile):
		"""
		Initialized basic of classifier like fwd index, index
		:param configFile:
		"""
		metapy.log_to_stderr()

		# Loading indexes
		self.invertedIndex = metapy.index.make_inverted_index(configFile)
		self.fwdIndex = metapy.index.make_forward_index(configFile)
		# Define multi class data set
		self.multiClassDataset = metapy.classify.MulticlassDataset(self.fwdIndex)
		self.classifier = self.getClassifier(self.multiClassDataset, self.fwdIndex, self.invertedIndex)

	def getClassifier(self, training, fwdIndex, invertedIndex):
		"""
		This function needs to implemented  by inherit class
		:param training: training set
		:param fwdIndex: fwdIndex created by metapy
		:param invertedIndex: inverted index created by metapy
		:return: classifier instance
		"""
		raise NotImplemented("Must implement this function by inherit class")

	def score(self, link_text, page_title, body_text):
		"""
		Should implemented by inherit class
		:param link_text: url link text (anchor text)
		:param page_title: page title
		:param body_text: body text
		:return: double score value between 0 - 1
		"""
		raise NotImplemented("Must implement this function by inherit class")