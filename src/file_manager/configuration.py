# configuration_manager.py
# author: Josue Mendoza
# date: 4-2-2015

from xml.dom.minidom import *
from file_manager import File


class Configuration(object):
	def __init__(self, xml_content):
		self.raw_xml_configuration = xml_content
		self.level = self.get_value_from_raw_xml('level')
		self.algorithm = self.get_value_from_raw_xml('algorithm')
		self.filepath_save = self.get_value_from_raw_xml('filepath_save')
		self.filename_save = self.get_value_from_raw_xml('filename_save')

	def get_value_from_raw_xml(self, xml_key):
		dom = parseString(self.raw_xml_configuration)
		return dom.getElementsByTagName(xml_key)[0].childNodes[0].data

	def get_xml_as_string(self):
		doc = Document();
		config = doc.createElement('configuration')
		level = doc.createElement('level')
		algorithm = doc.createElement('algorithm')
		filepath_save = doc.createElement('filepath_save')
		filename_save = doc.createElement('filename_save')

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

#test = File("../../doc/xmlTest.xml")
#config = Configuration(test.read_content())
#print config.get_xml_as_string()
#print config.level