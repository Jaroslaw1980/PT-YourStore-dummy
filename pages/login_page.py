from locators.locators import LoginPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.base_urls import BaseUrls


class LoginPage(BasePage):

    base_url = BaseUrls.login_page_url

    input_email_ID = LoginPageLocators.input_email_logPg_ID
    input_password_ID = LoginPageLocators.input_password_logPg_ID
    submit_button_XPATH = LoginPageLocators.submit_button_logPg_XPATH
    popup_text_XPATH = LoginPageLocators.popup_text_logPg_XPATH

    def input_email(self, email):
        self.driver.find_element(By.ID, self.input_email_ID).clear()
        self.driver.find_element(By.ID, self.input_email_ID).send_keys(email)

    def input_password(self, password):
        self.driver.find_element(By.ID, self.input_password_ID).clear()
        self.driver.find_element(By.ID, self.input_password_ID).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_button_XPATH).click()

    def wrong_login_popup_text(self):   # Warning: No match for E-Mail Address and/or Password.
        popup = self.driver.find_element(By.XPATH, self.popup_text_XPATH)
        return popup

