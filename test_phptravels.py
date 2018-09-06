import unittest
from selenium import webdriver
import time
from pages.page import LoginPage, RegisterPage

def setUpModule():
    global driver
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.maximize_window()

def tearDownModule():
    driver.close()

class LoginFunctionality(unittest.TestCase):

    def setUp(self):
        self.login_page = LoginPage(driver)
        self.login_page.driver.get("https://www.phptravels.net/login")
        
    def test_valid_login(self):
        self.login_page.valid_login()
        self.assertEqual(driver.current_url, 'https://www.phptravels.net/account/')

    def test_invalid_login(self):
        self.login_page.invalid_login()
        self.assertIn('alert alert-danger', driver.page_source)
    
    def test_empty_login(self):
        self.login_page.empty_login()
        self.assertIn('alert alert-danger', driver.page_source) 

    def test_valid_forget_pass(self):
        self.login_page.valid_forget()
        self.assertIn('alert alert-success', driver.page_source)
    
    def test_invalid_forget_pass(self):
        self.login_page.invalid_forget()
        self.assertIn('alert alert-danger', driver.page_source)

class RegisterFunctionality(unittest.TestCase):

    def setUp(self):
        self.register_page = RegisterPage(driver)
        self.register_page.logout_if_logged_in()
        self.register_page.driver.get("https://www.phptravels.net/register")
        

    def test_valid_register(self):
        self.register_page.valid_register()
        self.assertEqual(driver.current_url, 'https://www.phptravels.net/account/')
        self.assertIn("Hi, John Doe", driver.page_source) 

    def test_existing_email_register(self):
        self.register_page.existing_email_register() 
        self.assertEqual(driver.current_url, 'https://www.phptravels.net/register')
        self.assertIn("Email Already Exists.", driver.page_source)
        self.assertIn('alert alert-danger', driver.page_source)    

    def test_short_password_register(self):
        self.register_page.short_password_register() 
        self.assertEqual(driver.current_url, 'https://www.phptravels.net/register')
        self.assertIn("The Password field must be at least 6 characters in length.", driver.page_source)
        self.assertIn('alert alert-danger', driver.page_source)   

    def test_mismatching_password_register(self):
        self.register_page.mismatching_password_register() 
        self.assertEqual(driver.current_url, 'https://www.phptravels.net/register')
        self.assertIn("Password not matching with confirm password.", driver.page_source)
        self.assertIn('alert alert-danger', driver.page_source)   

    def test_empty_register(self):
        self.register_page.empty_register() 
        self.assertEqual(driver.current_url, 'https://www.phptravels.net/register')
        self.assertIn("The Email field is required.", driver.page_source)
        self.assertIn("The Password field is required.", driver.page_source)
        self.assertIn("The First name field is required.", driver.page_source)
        self.assertIn("The Last Name field is required.", driver.page_source)
        self.assertIn('alert alert-danger', driver.page_source)  

    def test_no_mobile_register(self):
        '''Mobile number is optional.'''
        self.register_page.no_mobile_register()
        self.assertEqual(driver.current_url, 'https://www.phptravels.net/account/')
        self.assertIn("Hi, John Doe", driver.page_source) 