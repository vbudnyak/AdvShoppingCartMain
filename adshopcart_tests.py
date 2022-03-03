import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class TestShopping(unittest.TestCase):


    @staticmethod
    def test_open_shooping_site():
        methods.setUp()
        methods.create_new_user()
        methods.login_user()
        methods.check_homepage()
        methods.delete_user()
        methods.retry_login()
        methods.tearDown()
