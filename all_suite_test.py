import unittest

from unittest.loader import makeSuite

from test_cases.adding_a_player import TestAddPlayer
from test_cases.sign_out import TestDashboardPage
from test_cases.system_login import TestLoginPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestDashboardPage))
    test_suite.addTest(makeSuite(TestAddPlayer))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())

