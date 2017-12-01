"""
Helper class to generate sample data for metapy

This file is being used to fetch sample data from google (or already fetched as json form)
then covert it to file corpus for metapy

This file fetch data using google customer search api with api key and context. So you have to setup API key and
context key using your own google account
"""
import json
import os
import csv
import glob


class SampleData(object):
	"""
		Fetch sample data
	"""

	'''
	# install google client lib using command - pip install google-api-python-client
	# Sample function code to get data from google if you are interested
	from googleapiclient.discovery import build
	
	# GET API KEY and CONTEXT KEY using your own google account
	API_KEY = "AIzaSyDJdiXMmWJlBRfH-OZrGgiKZJBqvP1RuI4"
	CONTEXT_KEY = "009145565549379058663%3A26iwjephy54"

	def get_sample_from_google(self, query, start=1):
		service = build("customsearch", "v1", developerKey=self.API_KEY)
		res = service.cse().list(q=query, cx=self.CONTEXT_KEY, start=start).execute()
		return res['items']
	'''

	def _isValid(self, filePath):
		"""
		Return true/false
		:param filePath: file path to validate
		:return: true/false
		"""
		return os.path.isabs(filePath) and not os.path.exists(filePath)


	def _generateSample(self, filePattern, sampleDestFolder):
		"""
		Utility function to generate sample
		:param labelFilePointer:  file pointer which hold label and relative file
		:param sampleDestFolder: sample folder path
		:param label: classification label
		:return: list of generated sample files
		"""
		files = []
		for filepath in glob.glob(filePattern):
			with open(filepath, "r") as fp:
				data = json.load(fp)
				if not data:
					continue
				items = data.get("items")
				destBase = sampleDestFolder + os.sep + os.path.basename(filepath).replace(".json", "")
				for index, item in enumerate(items):
					destItemBase = destBase + str(index)
					destTitle = destItemBase + "_title.txt"
					destDescription = destItemBase + "_description.txt"
					with open(destTitle, "w") as destTitleFp:
						destTitleFp.write(item.get("title").encode('utf-8'))
					files.append(destTitle)
					with open(destDescription, "w") as destDescriptionFp:
						destDescriptionFp.write(item.get("snippet").encode('utf-8'))
					files.append(destDescription)
				print "Successfully generate same files for pattern=" + destBase
		return files

	def convertDataSetToCsv(self, rawFolderPath, rootDestFolderPath, label):
		"""
		Convert raw sample set to format which metapy understand
		:param rawFolderPath:
		:param rootDestFolderPath:
		:param label:
		:return:
		"""
		if self._isValid(rawFolderPath):
			print "Invalid raw source folder path"
			return
		if self._isValid(rootDestFolderPath):
			print "Invalid dest folder path"
			return

		labelFile = rootDestFolderPath + os.sep + "dataset-full-corpus.txt"
		# create sample folder
		destFolderPath = rootDestFolderPath + os.sep + "sample"
		if not os.path.exists(destFolderPath):
			os.makedirs(destFolderPath)

		files = self._generateSample(rawFolderPath + os.sep + "*.json", sampleDestFolder=destFolderPath)
		with open(labelFile, "a+") as labelFilePointer:
			for filePath in files:
				labelFilePointer.write(label + "\t" + filePath.replace(rootDestFolderPath, ""))
				labelFilePointer.write("\n")

if __name__ == "__main__":
	SampleData().convertDataSetToCsv(os.path.abspath("google_sample_data/dataset/raw/new_homes"),
									 os.path.abspath("google_sample_data/dataset"), "NewHome")