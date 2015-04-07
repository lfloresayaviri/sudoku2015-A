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

		try:
			file_content = fo.read()
		except IOError as e:
			raise IOError('cannot read file')
		finally:
			fo.close()

		return file_content

	def write_content(self, file_content):
		fo = open(self.file_path, "wb")
		result = True

		try:
			fo.write(file_content);
		except IOError as e:
			raise IOError('cannot write content to file')
			result = False
		finally:
			fo.close()

		return result

	def delete(self):
		os.remove(self.file_path)

	def file_exists(self):
		return os.path.exists(self.file_path)