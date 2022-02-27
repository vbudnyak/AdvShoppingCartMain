import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class TestShopping(unittest.TestCase):


    @staticmethod
    def open_shooping_site():
        methods.setUp(locators.advantage_shopping_cart_url)
        methods.tearDown()
