from selenium.webdriver.common.by import By

LOGIN_EMAIL = (By.XPATH,"//input[@name='username']")
LOGIN_PASSWORD = (By.XPATH, "//input[@name='password']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//*[@id='loginfrm']/div[1]/div[5]/button")
LOGIN_FORGET_PASSWORD = (By.XPATH, "//*[@id='loginfrm']/div[2]/div[3]/a")
LOGIN_FORGET_RESET = (By.XPATH, "//*[@id='passresetfrm']/div[2]/span/button[@class='btn btn-primary resetbtn']")
LOGIN_FORGET_EMAIL = (By.XPATH, "//*[@id='resetemail']")