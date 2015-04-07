# test_configuration.py
# author: Josue Mendoza
# date: 4-5-2015

from xml.dom.minidom import *
import unittest
import os

from configuration import Configuration
from file_manager import File

class FileManagerTest(unittest.TestCase):
	TEST_FOLDER = os.getcwd() + '\\test_folder'
	TEST_FILE = TEST_FOLDER + '\\test_file.txt'

	SAMPLE_LEVEL = 'easy'
	SAMPLE_ALGORITHM = 'norvigs'
	SAMPLE_FILEPATH = 'D:\\'
	SAMPLE_FILENAME = 'sudoku.txt'

	XML_SAMPLE = '<?xml version="1.0" ?><configuration>\
		<level>' + SAMPLE_LEVEL + '</level>\
		<algorithm>' + SAMPLE_ALGORITHM + '</algorithm>\
		<filepath_save>' + SAMPLE_FILEPATH + '</filepath_save>\
		<filename_save>' + SAMPLE_FILENAME + '</filename_save>\
		</configuration>'

	if not os.path.exists(TEST_FOLDER): os.makedirs(TEST_FOLDER)

	def test_just_one_instance_of_configuration_can_be_created(self):
		file_instance = File(self.TEST_FILE)
		file_instance.write_content(self.XML_SAMPLE)
		configuration_instance_a = Configuration(file_instance.read_content())
		configuration_instance_b = Configuration(file_instance.read_content())
		self.assertEqual(configuration_instance_a, configuration_instance_b)
		file_instance.delete()

	def test_configuration_instances_have_correct_values_in_attributes(self):
		file_instance = File(self.TEST_FILE)
		file_instance.write_content(self.XML_SAMPLE)
		configuration_instance = Configuration(file_instance.read_content())
		self.assertEqual(self.SAMPLE_LEVEL, configuration_instance.level)
		self.assertEqual(self.SAMPLE_ALGORITHM, configuration_instance.algorithm)
		self.assertEqual(self.SAMPLE_FILEPATH, configuration_instance.filepath_save)
		self.assertEqual(self.SAMPLE_FILENAME, configuration_instance.filename_save)

	def test_configuration_can_be_retrieved_as_xml(self):
		file_instance = File(self.TEST_FILE)
		file_instance.write_content(self.XML_SAMPLE)
		configuration_instance = Configuration(file_instance.read_content())

		raw_xml_sample = ''

		for i in self.XML_SAMPLE:
			raw_xml_sample += i.strip("\n").strip("\t").replace("\n","").replace("\t","")

		raw_retrieved_xml = ''

		for i in configuration_instance.get_xml_as_string():
			raw_retrieved_xml += i.strip("\n").strip("\t").replace("\n","").replace("\t","")

		self.assertEqual(raw_xml_sample, raw_retrieved_xml)


if __name__ == '__main__':
    unittest.main()