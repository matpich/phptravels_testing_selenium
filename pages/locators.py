from selenium.webdriver.common.by import By

#login page elements
LOGIN_EMAIL = (By.XPATH,"//input[@name='username']")
LOGIN_PASSWORD = (By.XPATH, "//input[@name='password']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//*[@id='loginfrm']/div[1]/div[5]/button")
LOGIN_FORGET_PASSWORD = (By.XPATH, "//*[@id='loginfrm']/div[2]/div[3]/a")
LOGIN_FORGET_RESET = (By.XPATH, "//*[@id='passresetfrm']/div[2]/span/button[@class='btn btn-primary resetbtn']")
LOGIN_FORGET_EMAIL = (By.XPATH, "//*[@id='resetemail']")

#register page elements
REGISTER_FIRST_NAME = (By.XPATH, "//input[@name='firstname']")
REGISTER_LAST_NAME = (By.XPATH, "//input[@name='lastname']")
REGISTER_MOBILE_NUMBER = (By.XPATH, "//input[@name='phone']")
REGISTER_EMAIL = (By.XPATH, "//input[@name='email']")
REGISTER_PASSWORD = (By.XPATH, "//input[@name='password']")
REGISTER_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='confirmpassword']")
REGISTER_SIGN_UP_BUTTON = (By.XPATH, "//*[@id='headersignupform']/div[9]/button")