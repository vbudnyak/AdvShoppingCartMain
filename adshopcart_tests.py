import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class TestShopping(unittest.TestCase):


    @staticmethod
    def test_open_shooping_site():
        methods.setUp()
        methods.tearDown()
