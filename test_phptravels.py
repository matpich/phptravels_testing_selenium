import unittest
from selenium import webdriver
import time
from pages.page import LoginPage, RegisterPage, EditPage

def setUpModule():
    global driver
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.phptravels.net/register")
    RegisterPage(driver).valid_register()

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
        self.register_page.valid_register("valid.test@email.com") #setUpModule call the same method to create user for tests, that's why I'm passing email address - to avoid "Email existing conflict"
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

class EditProfileFunctionality(unittest.TestCase):
    def setUp(self):
        driver.get("https://www.phptravels.net/account")
        self.edit_page = EditPage(driver)
        #if not logged in it should redirect to login page first

    def test_names_not_editable(self):
        '''First and last name shouldn't be editable.'''
        self.assertTrue(self.edit_page.is_first_name_editable())
        self.assertTrue(self.edit_page.is_last_name_editable())

    def test_valid_change_email(self):
        '''Changes email with correct email.'''
        self.edit_page.change_with_valid_email()
        self.assertIn("Profile Updated Successfully.", driver.page_source)
        self.assertIn('alert alert-success', driver.page_source)   

    def test_wrong_change_email(self):
        '''Changes email with incorrect email.'''
        self.edit_page.change_with_invalid_email()
        self.assertIn("The Email field must contain a valid email address.", driver.page_source)
        self.assertIn('alert alert-danger', driver.page_source)   

    def test_valid_change_password(self):
        self.edit_page.change_with_valid_password()
        self.assertIn("Profile Updated Successfully.", driver.page_source)
        self.assertIn('alert alert-success', driver.page_source)  

    def test_invalid_change_password(self):
        self.edit_page.change_with_invalid_password()
        self.assertIn("The Password field must be at least 6 characters in length.", driver.page_source)
        self.assertIn('alert alert-danger', driver.page_source)    

    def test_mismatching_change_password(self):
        self.edit_page.change_with_mismatching_password()
        self.assertIn("Passwords not matching.", driver.page_source)
        self.assertIn('alert alert-danger', driver.page_source)    

    def test_valid_change_phone(self):
        self.edit_page.change_phone()
        self.assertIn("Profile Updated Successfully.", driver.page_source)
        self.assertIn('alert alert-success', driver.page_source) 

    def test_valid_change_address(self):
        self.edit_page.change_address_data()
        self.assertIn("Profile Updated Successfully.", driver.page_source)
        self.assertIn('alert alert-success', driver.page_source) 

    def test_subscribe_is_switching(self):
        self.assertEqual(self.edit_page.check_subscribe_status(),"No")
        self.edit_page.change_subscribe_status()
        self.assertEqual(self.edit_page.check_subscribe_status(),"Yes")
        self.edit_page.change_subscribe_status()
        self.assertEqual(self.edit_page.check_subscribe_status(),"No")