import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
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

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_shopping_cart_url and driver.title == ' Advantage Shopping':
        print(f'We are at Advantage online shopping homepage -- {driver.current_url}')
        print(f'We are seeing title message -- "Advantage Demo"')
    else:
        print(f'We are not at the Advantage online shopping homepage. Check your code!')
        driver.close()
        driver.quit()
    sleep(0.25)

def create_new_user():
#    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)

#    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(2)

    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)

    driver.find_element(By.NAME, 'allowOffersPromotion').click()
    driver.find_element(By.NAME, 'i_agree').click()
    driver.find_element(By.ID, 'register_btnundefined').click()

    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="menuUser"]').click()

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="menuUser"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()

#    if driver.find_element(By.LINK_TEXT, '- No orders -') == '- No orders -':
#        print(f"No orders in the basket")

    driver.find_element(By.XPATH, '//*[@id="menuUser"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(0.5)

def login_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '// *[ @ id = "sign_in_btnundefined"]').click()

def delete_user():
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="menuUser"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()

    driver.find_element(By.XPATH, '// *[ @ id = "myAccountContainer"] / div[6] / button').click()
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    sleep(3)

def retry_login():
    driver.find_element(By.XPATH, '//*[@id="menuUser"]').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(1)
    driver.find_element(By.XPATH, '// *[ @ id = "sign_in_btnundefined"]').click()
    sleep(1)
    if driver.find_element(By.ID, 'signInResultMessage'):
        print(f'-----------------------------------------------')
        print(f'Account is disabled. Please contact site administration.')
    else:
        print(f'Ups, something wrong. Check for errors.')

    print(f'#############################################################')
    print(f'TEST IS ACCOMPLISHED!!!')
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')


def tearDown():
    if driver is not None:
        print(f"---------------------------------")
        print(f"Test Completed at: {datetime.datetime.now()}")
        driver.close()
        driver.quit()

