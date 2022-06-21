from locators.locators import LoginPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    input_email_logPg_ID = LoginPageLocators.input_email_logPg_ID
    input_password_logPg_ID = LoginPageLocators.input_password_logPg_ID
    submit_button_logPg_XPATH = LoginPageLocators.submit_button_logPg_XPATH
    popup_text_logPg_XPATH = LoginPageLocators.popup_text_logPg_XPATH

    def input_email(self, email):
        self.driver.find_element(By.ID, self.input_email_logPg_ID).clear()
        self.driver.find_element(By.ID, self.input_email_logPg_ID).send_keys(email)

    def input_password(self, password):
        self.driver.find_element(By.ID, self.input_password_logPg_ID).clear()
        self.driver.find_element(By.ID, self.input_password_logPg_ID).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_button_logPg_XPATH).click()

    def wrong_login_popup_text(self):   # Warning: No match for E-Mail Address and/or Password.
        popup = self.driver.find_element(By.XPATH, self.popup_text_logPg_XPATH)
        return popup

