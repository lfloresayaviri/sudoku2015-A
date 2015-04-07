# configuration_manager.py
# author: Josue Mendoza
# date: 4-7-2015

import unittest
import sys

sys.path.append("../src")
sys.path.append("../src/file_manager")
sys.path.append("../src/configuration")
sys.path.append("../src/utils")

from file_manager_test import FileManagerTest
from configuration_test import ConfigurationTest

# Load Tests
file_manager_suite = unittest.TestLoader().loadTestsFromTestCase(FileManagerTest)
configuration_suite = unittest.TestLoader().loadTestsFromTestCase(ConfigurationTest)

# Load Test Suite
alltests = unittest.TestSuite([file_manager_suite, configuration_suite])

# Execute Test Suite
unittest.TextTestRunner(verbosity=2).run(alltests)