# configuration_manager.py
# author: Josue Mendoza
# date: 4-2-2015

from xml.dom.minidom import *
from file_manager.file_manager import File
from utils.singleton import Singleton

class Configuration(object):

	__metaclass__ = Singleton

	CONFIGURATION_NAME = 'configuration'
	LEVEL_NAME = 'level'
	ALGORITHM_NAME = 'algorithm'
	FILEPATH_SAVE_NAME = 'filepath_save'
	FILENAME_SAVE_NAME = 'filename_save'

	def __init__(self, xml_content = None):
		self.__raw_xml_configuration = xml_content
		self.level = self.get_value_from_raw_xml(self.LEVEL_NAME)
		self.algorithm = self.get_value_from_raw_xml(self.ALGORITHM_NAME)
		self.filepath_save = self.get_value_from_raw_xml(self.FILEPATH_SAVE_NAME)
		self.filename_save = self.get_value_from_raw_xml(self.FILENAME_SAVE_NAME)

	def get_value_from_raw_xml(self, xml_key):
		"""Gets a value from a XML string.

		Keyword arguments:
		xml_key -- the string that contains the xml data
		"""
		dom = parseString(self.__raw_xml_configuration)
		
		try:
			return dom.getElementsByTagName(xml_key)[0].childNodes[0].data
		except IndexError as e:
			raise IndexError("invalid configuration file, elements not found")

	def get_xml_as_string(self):
		"""Retrieves all the attributes from a configuration instance, with the	data
		gathered it builds an XML and stores it into a string which is returned as result
		"""
		doc = Document()
		config = doc.createElement(self.CONFIGURATION_NAME)
		level = doc.createElement(self.LEVEL_NAME)
		algorithm = doc.createElement(self.ALGORITHM_NAME)
		filepath_save = doc.createElement(self.FILEPATH_SAVE_NAME)
		filename_save = doc.createElement(self.FILENAME_SAVE_NAME)

		level.appendChild(doc.createTextNode(self.level))
		algorithm.appendChild(doc.createTextNode(self.algorithm))
		filepath_save.appendChild(doc.createTextNode(self.filepath_save))
		filename_save.appendChild(doc.createTextNode(self.filename_save))

		doc.appendChild(config)
		config.appendChild(level)
		config.appendChild(algorithm)
		config.appendChild(filepath_save)
		config.appendChild(filename_save)

		return doc.toprettyxml()