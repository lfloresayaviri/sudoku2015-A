# configuration_manager.py
# author: Josue Mendoza
# date: 4-7-2015

import unittest
import sys

sys.path.append("../src")
sys.path.append("../src/file_manager")
sys.path.append("../src/configuration")
sys.path.append("../src/solver")
sys.path.append("../src/solver/algorithms")
sys.path.append("../src/utils")

from file_manager_test import FileManagerTest
from configuration_test import ConfigurationTest
from norvig_solver_test import NorvigSolverTest

# Load Tests
file_manager_suite = unittest.TestLoader().loadTestsFromTestCase(FileManagerTest)
configuration_suite = unittest.TestLoader().loadTestsFromTestCase(ConfigurationTest)
norvig_solver_suite = unittest.TestLoader().loadTestsFromTestCase(NorvigSolverTest)

# Load Test Suite
all_tests = unittest.TestSuite([file_manager_suite, configuration_suite, norvig_solver_suite])

# Execute Test Suite
unittest.TextTestRunner(verbosity=2).run(all_tests)