from Selenium.PTYourStore.locators.locators import Locators
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.input_email_logPg_ID = Locators.input_email_logPg_ID
        self.input_password_logPg_ID = Locators.input_password_logPg_ID
        self.submit_button_logPg_XPATH = Locators.submit_button_logPg_XPATH

    def input_email(self, email):
        self.driver.find_element(By.ID, self.input_email_logPg_ID).clear()
        self.driver.find_element(By.ID, self.input_email_logPg_ID).send_keys(email)

    def input_password(self, password):
        self.driver.find_element(By.ID, self.input_password_logPg_ID).clear()
        self.driver.find_element(By.ID, self.input_password_logPg_ID).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_button_logPg_XPATH).click()
