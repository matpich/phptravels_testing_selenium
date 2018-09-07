from selenium import webdriver
from pages import locators
from pages.user import User
from selenium.webdriver.support.ui import WebDriverWait, Select
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

    def select_element_by_text(self, value, location):
        select = Select(self.driver.find_element(*location))
        select.select_by_visible_text(value)

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
        self.logout_if_logged_in()
        self.wait_for_load()
        self.fill_email(User.email)
        self.fill_password(User.password)
        self.click_login_bttn()
        WebDriverWait(self.driver, 10).until(EC.title_is("My Account"))
        BasePage.is_logged = True

    def invalid_login(self):
        self.logout_if_logged_in()
        self.wait_for_load()
        self.fill_email('wrong@email.com')
        self.fill_password('wrong-password')
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

    def valid_register(self, email = User.email):
        self.fill_first_name(User.first_name)
        self.fill_last_name(User.last_name)
        self.fill_mobile(User.mobile)
        self.fill_email(email)
        self.fill_password(User.password)
        self.fill_confirm_password(User.confirm_password)
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.title_is("My Account"))
        BasePage.is_logged = True

    def existing_email_register(self):
        self.fill_first_name(User.first_name)
        self.fill_last_name(User.last_name)
        self.fill_mobile(User.mobile)
        self.fill_email("user@phptravels.com")
        self.fill_password(User.password)
        self.fill_confirm_password(User.confirm_password)
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
        self.fill_first_name(User.first_name)
        self.fill_last_name(User.last_name)
        self.fill_mobile(User.mobile)
        self.fill_email("mismatch_"+User.email)
        self.fill_password(User.password)
        self.fill_confirm_password("asdfgh")
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def empty_register(self):
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def no_mobile_register(self):
        self.fill_first_name(User.first_name)
        self.fill_last_name(User.last_name)
        self.fill_email("phone_"+User.email)
        self.fill_password(User.password)
        self.fill_confirm_password(User.confirm_password)
        self.click_signup_bttn()
        WebDriverWait(self.driver, 10).until(EC.title_is("My Account"))
        BasePage.is_logged = True

class EditPage(LoginPage):
    def __init__(self,driver):
        super(EditPage, self).__init__(driver)
        #it will sign in user if logged out
        if not BasePage.is_logged: self.valid_login()
        self.click_my_profile()

    def click_newsletter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ACCOUNT_NEWSLETTER))
        self.click_element(locators.ACCOUNT_NEWSLETTER)

    def click_my_profile(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.ACCOUNT_MY_PROFILE))
        self.click_element(locators.ACCOUNT_MY_PROFILE)

    def click_submit_button(self):
        self.click_element(locators.MP_SUBMIT)

    def click_subscribe(self):
        self.click_element(locators.NL_SUBSCRIBE)

    def check_subscribe_status(self):
        self.click_newsletter()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locators.NL_SUBSCRIBE))
        element = self.driver.find_element(*locators.NL_SUBSCRIBE)
        return element.text
    
    def fill_edit_email(self, address):
        self.input_into_box(address, locators.MP_EMAIL)

    def fill_edit_phone(self, phone):
        self.input_into_box(phone, locators.MP_PHONE)

    def fill_edit_password(self, password):
        self.input_into_box(password, locators.MP_PASSWORD)

    def fill_edit_confirm_password(self, password):
        self.input_into_box(password, locators.MP_CONFIRM_PASSWORD)

    def fill_edit_address_one(self, address):
        self.input_into_box(address, locators.MP_ADDRESS)

    def fill_edit_address_two(self, address):
        self.input_into_box(address, locators.MP_ADDRESS_2)

    def fill_edit_city(self, city):
        self.input_into_box(city, locators.MP_CITY)

    def fill_edit_region(self, region):
        self.input_into_box(region, locators.MP_REGION)

    def fill_edit_postal(self, postal):
        self.input_into_box(postal, locators.MP_POSTAL)

    def select_edit_country(self, value):
        self.select_element_by_text(value, locators.MP_COUNTRY)

    def is_first_name_editable(self):
        element = self.driver.find_element(*locators.MP_FIRST_NAME)
        return element.get_attribute("readonly")

    def is_last_name_editable(self):
        element = self.driver.find_element(*locators.MP_LAST_NAME)
        return element.get_attribute("readonly")

    def change_with_valid_email(self):
        email = "test@test.test"
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.MP_EMAIL))
        self.fill_edit_email(email)
        User.email = email
        self.click_submit_button()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.SUCCESS_BOX))

    def change_with_invalid_email(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.MP_EMAIL))
        self.fill_edit_email("wrong.email")
        self.click_submit_button()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def change_with_valid_password(self):
        new_password = "zxcvbn"
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.MP_EMAIL))
        self.fill_edit_password(new_password)
        self.fill_edit_confirm_password(new_password)
        User.password = new_password
        User.confirm_password = new_password
        self.click_submit_button()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.SUCCESS_BOX))

    def change_with_invalid_password(self):
        invalid_password = "asd"
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.MP_EMAIL))
        self.fill_edit_password(invalid_password)
        self.fill_edit_confirm_password(invalid_password)
        self.click_submit_button()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def change_with_mismatching_password(self):
        new_password = "zxcvbn"
        mismatching_password = "qwerty"
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.MP_EMAIL))
        self.fill_edit_password(new_password)
        self.fill_edit_confirm_password(mismatching_password)
        self.click_submit_button()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.ERROR_BOX))

    def change_phone(self):
        mobile = "111222333"
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.MP_EMAIL))
        self.fill_edit_phone(mobile)
        User.mobile = mobile
        self.click_submit_button()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.SUCCESS_BOX)) 

    def change_address_data(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.MP_ADDRESS))
        self.fill_edit_address_one("Road 12")
        self.fill_edit_address_two("Another Road")
        self.fill_edit_city("Somecity")
        self.fill_edit_region("Someregion")
        self.fill_edit_postal("35890")
        self.select_edit_country("Botswana")
        self.click_submit_button()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locators.SUCCESS_BOX))

    def change_subscribe_status(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locators.NL_SUBSCRIBE))
        self.click_subscribe()