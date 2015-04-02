# file_manager.py
# author: Josue Mendoza
# date: 4-2-2015

from xml.dom.minidom import parseString
import os

class File(object):
	def __init__(self, file_path):
		self.file_path = file_path

	def read_content(self):
		fo = open(self.file_path, 'r')
		file_content = fo.read()
		fo.close()
		return file_content

	def write_content(self, file_content):
		fo = open(self.file_path, "wb")
		fo.write(file_content);
		fo.close()

	def delete(self):
		os.remove(self.file_path)

	def file_exists(self):
		return os.path.exists(self.file_path)