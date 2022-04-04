import unittest
import jpetstore_locators as locators
import jpetstore_methods as methods


class JpetstoreAppPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_main_jpetstore():
        methods.setUp()
        methods.register_new_user()
        methods.my_cart()
        methods.update_cart()
        methods.check_out()
        methods.tearDown()
