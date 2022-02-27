import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=s)


# to open web browser
def setUp():

    print(f"---------------------------------")
    print(f"Test Started at: {datetime.datetime.now()}")

    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Moodle app website
    driver.get(locators.advantage_shopping_cart_url)
    sleep(0.5)
#    breakpoint()

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_shopping_cart_url and driver.title == ' Advantage Shopping':
        print(f'We are at Advantage online shopping homepage -- {driver.current_url}')
        print(f'We are seeing title message -- "Advantage Demo"')
    else:
        print(f'We are not at the Advantage online shopping homepage. Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f"---------------------------------")
        print(f"Test Completed at: {datetime.datetime.now()}")
        driver.close()
        driver.quit()

setUp()
tearDown()