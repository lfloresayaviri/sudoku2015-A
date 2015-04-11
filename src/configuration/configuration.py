# configuration_manager.py
# author: Josue Mendoza
# date: 4-2-2015

from xml.dom.minidom import *
from file_manager import File
from singleton import Singleton


class Configuration(object):
    """Configuration instance objects have attributes containing the
    configuration values and the raw xml as string.

    Attributes are:
    __raw_xml_configuration: a string containing the complete configuration xml
    level: a string containing the level of the game. (i.e. easy)
    algorithm: a string containing the algorithm to be used to solve the game if
    applicable. (i.e. peter_norvig)
    file_path_save: a string containing the default file path where games will
    be saved. (i.e. C:\sudoku\files\)
    file_name_save: a string containing the default file name for the games to
    be saved. (i.e. game_1_4_2015)
    """
    __metaclass__ = Singleton

    CONFIGURATION_NAME = 'configuration'
    LEVEL_NAME = 'level'
    ALGORITHM_NAME = 'algorithm'
    FILE_PATH_SAVE_NAME = 'file_path_save'
    FILE_NAME_SAVE_NAME = 'file_name_save'

    def __init__(self, xml_content=None):
        self.__raw_xml_configuration = xml_content
        self.level = self.get_value_from_raw_xml(self.LEVEL_NAME)
        self.algorithm = self.get_value_from_raw_xml(self.ALGORITHM_NAME)
        self.file_path_save = self.get_value_from_raw_xml(self.FILE_PATH_SAVE_NAME)
        self.file_name_save = self.get_value_from_raw_xml(self.FILE_NAME_SAVE_NAME)

    def get_value_from_raw_xml(self, xml_key):
        """Returns a value from a XML string based on the key sent as argument.

        Keyword arguments:
        xml_key -- the string that contains the xml data.
        """
        dom = parseString(self.__raw_xml_configuration)
        
        try:
            return dom.getElementsByTagName(xml_key)[0].childNodes[0].data
        except IndexError:
            raise IndexError("invalid configuration file, elements not found")

    def get_xml_as_string(self):
        """Retrieves all the attributes from a configuration instance, with the    data
        gathered it builds an XML and stores it into a string which is returned as result
        """
        doc = Document()
        config = doc.createElement(self.CONFIGURATION_NAME)
        level = doc.createElement(self.LEVEL_NAME)
        algorithm = doc.createElement(self.ALGORITHM_NAME)
        file_path_save = doc.createElement(self.FILE_PATH_SAVE_NAME)
        file_name_save = doc.createElement(self.FILE_NAME_SAVE_NAME)

        level.appendChild(doc.createTextNode(self.level))
        algorithm.appendChild(doc.createTextNode(self.algorithm))
        file_path_save.appendChild(doc.createTextNode(self.file_path_save))
        file_name_save.appendChild(doc.createTextNode(self.file_name_save))

        doc.appendChild(config)
        config.appendChild(level)
        config.appendChild(algorithm)
        config.appendChild(file_path_save)
        config.appendChild(file_name_save)

        return doc.toprettyxml()