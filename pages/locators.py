from selenium.webdriver.common.by import By

#common
ERROR_BOX = (By.XPATH, "//div[@class='alert alert-danger']")
SUCCESS_BOX = (By.XPATH, "//div[@class='alert alert-success']")

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

#account page elements

ACCOUNT_MY_PROFILE = (By.XPATH, "//*[@id='body-section']/div/div[3]/div/div[1]/ul/li[2]/a")
ACCOUNT_NEWSLETTER = (By.XPATH, "//*[@id='body-section']/div/div[3]/div/div[1]/ul/li[4]/a")

#my profile elements

MP_FIRST_NAME = (By.XPATH, "//input[@name='firstname']")
MP_LAST_NAME = (By.XPATH, "//input[@name='lastname']")

MP_PHONE = (By.XPATH, "//input[@name='phone']")
MP_EMAIL = (By.XPATH, "//*[@id='profilefrm']/div/div[2]/div[2]/div[1]/div[2]/input")
MP_PASSWORD = (By.XPATH, "//input[@name='password']")
MP_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='confirmpassword']")

MP_ADDRESS = (By.XPATH, "//input[@name='address1']")
MP_ADDRESS_2 = (By.XPATH, "//input[@name='address2']")
MP_CITY = (By.XPATH, "//input[@name='city']")
MP_REGION = (By.XPATH, "//input[@name='state']")
MP_POSTAL = (By.XPATH, "//input[@name='zip']")
MP_COUNTRY = (By.XPATH, "//select[@name='country']")

MP_SUBMIT = (By.XPATH, "//*[@id='profilefrm']/div/div[3]/div[3]/button")

#newsletter

NL_SUBSCRIBE = (By.XPATH, "//*[@id='newsletter']/div/div/label/span")