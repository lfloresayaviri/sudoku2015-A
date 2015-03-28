import unittest
import sys

sys.path.append("../src")

from point_test import PointTest
from line_test import LineTest
from line_segment_test import LineSegmentTest

# Load Tests
point_suite = unittest.TestLoader().loadTestsFromTestCase(PointTest)
line_suite = unittest.TestLoader().loadTestsFromTestCase(LineTest)
line_segment_suite = unittest.TestLoader().loadTestsFromTestCase(LineSegmentTest)

# Load Test Suite
alltests = unittest.TestSuite([point_suite, line_suite, line_segment_suite])

# Execute Test Suite
unittest.TextTestRunner(verbosity=1).run(alltests)

