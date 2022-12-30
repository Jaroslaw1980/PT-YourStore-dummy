### "Login Page" URL, Locators, Page elements and Page actions ###

from locators.locators import LoginPageLocators
from base.base_page import BasePage
from utilities.base_urls import BaseUrls


class LoginPage(BasePage):
    # Url for login page locators
    base_url = BaseUrls.login_page_url

    # Locators
    email_field = LoginPageLocators.input_email_ID
    password_field = LoginPageLocators.input_password_ID
    submit_button = LoginPageLocators.submit_button_XPATH
    wrong_login_popup_text = LoginPageLocators.popup_text_XPATH

    # Page elements
    def get_email_field(self):
        return self.get_element(self.email_field)

    def get_password_field(self):
        return self.get_element(self.password_field)

    def get_submit_button(self):
        return self.get_element(self.submit_button, locator_type='xpath')

    def get_wrong_login_popup_text(self):
        return self.get_element(self.wrong_login_popup_text, locator_type='xpath')

    # Page actions
    def enter_email(self, email):
        self.send_keys_to_element(email, self.email_field)

    def enter_password(self, password):
        self.send_keys_to_element(password, self.password_field)

    def click_submit(self):
        self.click_element(self.submit_button, locator_type='xpath')
