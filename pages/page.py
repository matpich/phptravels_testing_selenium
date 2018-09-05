from selenium import webdriver
from pages import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class BasePage():
    '''Base class to initialize in all page objects'''
    def __init__(self,driver):
        self.driver = driver
        self.is_logged = False

    def logout(self):
        self.driver.get('https://www.phptravels.net/account/logout')
        self.is_logged = False

    def logout_if_logged_in(self):
        if self.is_logged: self.logout()

    def input_into_box(self, value, location):
        '''Input search values into box.'''
        element = self.driver.find_element(*location)
        element.clear()
        element.send_keys(value)
    
    def click_element(self, location):
        '''Clicks given element'''
        element = self.driver.find_element(*location)
        element.click()

class LoginPage(BasePage):
    '''Login page elements and methods. In some cases it was necessary to replace WebDriverWait with time.sleep().
       After successful password reset it's unable to do valid login...'''

    def wait_for_load(self):
        '''This method waits for page to be fully loaded after reloads'''
        WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(locators.LOGIN_EMAIL))
        WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(locators.LOGIN_PASSWORD))
        WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable(locators.LOGIN_SUBMIT_BUTTON))

    def fill_email(self,address):
        self.input_into_box(address, locators.LOGIN_EMAIL)

    def fill_password(self,password):
        self.input_into_box(password, locators.LOGIN_PASSWORD)

    def fill_forget_email(self,address):
        self.input_into_box(address, locators.LOGIN_FORGET_EMAIL)

    def click_login_bttn(self):
        self.click_element(locators.LOGIN_SUBMIT_BUTTON)

    def click_forget_bttn(self):
        '''WebDriverWait was unable to wait for specific elements, so I had to use time.sleep(1). I'm working on better solution.'''
        time.sleep(1)
        self.click_element(locators.LOGIN_FORGET_PASSWORD)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, -150);") # it's necessary to scroll a little, otherwise modal window won't show up (on the second time)
        time.sleep(1)

    def click_reset_bttn(self):
        self.click_element(locators.LOGIN_FORGET_RESET)

    def valid_login(self):
        self.wait_for_load()
        self.fill_email('user@phptravels.com')
        self.fill_password('demouser')
        self.click_login_bttn()
        #WebDriverWait(self.driver, 10).until(EC.title_is("My Account"))
        self.is_logged = True

    def invalid_login(self):
        self.logout_if_logged_in()
        self.wait_for_load()
        self.fill_email('user@phptravels.com')
        self.fill_password('zxcvbn')
        self.click_login_bttn()

    def empty_login(self):
        self.logout_if_logged_in()
        self.wait_for_load()
        self.click_login_bttn()

    def valid_forget(self):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locators.LOGIN_FORGET_PASSWORD))
        self.click_forget_bttn()
        #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.LOGIN_FORGET_EMAIL))
        self.fill_forget_email('user@phptravels.com')
        self.click_reset_bttn()

    def invalid_forget(self):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locators.LOGIN_FORGET_PASSWORD))
        self.click_forget_bttn()
        #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.LOGIN_FORGET_EMAIL))
        self.fill_forget_email('')
        self.click_reset_bttn()

