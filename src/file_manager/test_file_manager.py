# test_file_manager.py
# author: Josue Mendoza
# date: 4-2-2015

import unittest
import os

from file_manager import File

class FileManagerTest(unittest.TestCase):

    def test_file_manager_creates_a_file_if_the_file_does_not_exist_while_writting_content(self):
        file_path = "C:\\test_file.txt"
        file_instance = File(file_path)

        if file_instance.file_exists():
        	file_instance.delete()
        file_instance.write_content("test")

        self.assertTrue(os.path.exists(file_path))
        file_instance.delete()

    def test_file_manager_can_read_file_content(self):
        file_path = "C:\\test_file.txt"
        file_instance = File(file_path)
        sample_content = "sample text"

        fo = open(file_path, "wb")
        fo.write(sample_content);
        fo.close()

        self.assertEqual(sample_content, file_instance.read_content())
        file_instance.delete()


if __name__ == '__main__':
    unittest.main()