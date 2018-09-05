import unittest
from selenium import webdriver
import time
from pages.page import LoginPage

def setUpModule():
    global driver
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.maximize_window()

def tearDownModule():
    driver.close()

class LoginFunctionality(unittest.TestCase):

    def setUp(self):
        driver.get("https://www.phptravels.net/login")
        self.login_page = LoginPage(driver)

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

