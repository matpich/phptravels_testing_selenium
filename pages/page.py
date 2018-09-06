from selenium import webdriver
from pages import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random

class BasePage():
    '''Base class to initialize in all page objects'''

    is_logged = False

    def __init__(self,driver):
        self.driver = driver
        
    def logout(self):
        self.driver.get('https://www.phptravels.net/account/logout')
        BasePage.is_logged = False

    def logout_if_logged_in(self):
        if BasePage.is_logged: self.logout()

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
        BasePage.is_logged = True

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

class RegisterPage(BasePage):

    def fill_first_name(self,name):
        self.input_into_box(name, locators.REGISTER_FIRST_NAME)

    def fill_last_name(self,last_name):
        self.input_into_box(last_name, locators.REGISTER_LAST_NAME)

    def fill_mobile(self,mobile):
        self.input_into_box(mobile, locators.REGISTER_MOBILE_NUMBER)

    def fill_email(self,address):
        self.input_into_box(address, locators.REGISTER_EMAIL)

    def fill_password(self,password):
        self.input_into_box(password, locators.REGISTER_PASSWORD)

    def fill_confirm_password(self,confirm_password):
        self.input_into_box(confirm_password, locators.REGISTER_CONFIRM_PASSWORD)

    def click_signup_bttn(self):
        self.click_element(locators.REGISTER_SIGN_UP_BUTTON)

    def valid_register(self):
        self.fill_first_name("John")
        self.fill_last_name("Doe")
        self.fill_mobile("123456789")
        self.fill_email("john{}.doe@doe.doe".format(random.randint(0,9999)))
        self.fill_password("qwerty")
        self.fill_confirm_password("qwerty")
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.title_is("My Account"))
        BasePage.is_logged = True

    def existing_email_register(self):
        self.fill_first_name("John")
        self.fill_last_name("Doe")
        self.fill_mobile("123456789")
        self.fill_email("user@phptravels.com")
        self.fill_password("qwerty")
        self.fill_confirm_password("qwerty")
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def short_password_register(self):
        self.fill_first_name("John")
        self.fill_last_name("Doe")
        self.fill_mobile("123456789")
        self.fill_email("john{}.doe@doe.doe".format(random.randint(0,9999)))
        self.fill_password("qwe")
        self.fill_confirm_password("qwe")
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def mismatching_password_register(self):
        self.fill_first_name("John")
        self.fill_last_name("Doe")
        self.fill_mobile("123456789")
        self.fill_email("john{}.doe@doe.doe".format(random.randint(0,9999)))
        self.fill_password("qwerty")
        self.fill_confirm_password("asdfgh")
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def empty_register(self):
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def no_mobile_register(self):
        self.fill_first_name("John")
        self.fill_last_name("Doe")
        self.fill_email("john{}.doe@doe.doe".format(random.randint(0,9999)))
        self.fill_password("qwerty")
        self.fill_confirm_password("qwerty")
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.title_is("My Account"))
        BasePage.is_logged = True