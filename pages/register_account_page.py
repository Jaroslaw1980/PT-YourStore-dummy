### "Register Account Page" URL, Locators, Page elements and Page actions ###

from locators.locators import RegisterAccountLocators
from base.base_page import BasePage
from utilities.base_urls import BaseUrls


class RegisterAccount(BasePage):
    # Url for register account page
    base_url = BaseUrls.register_page_url

    # Locators
    firstname_field = RegisterAccountLocators.input_firstname_ID
    error_popup_firstname = RegisterAccountLocators.error_popup_firstname_XPATH
    lastname_field = RegisterAccountLocators.input_lastname_ID
    error_popup_lastname = RegisterAccountLocators.error_popup_lastname_XPATH
    email_field = RegisterAccountLocators.input_email_ID
    error_popup_email = RegisterAccountLocators.error_popup_email_XPATH
    telephone_field = RegisterAccountLocators.input_telephone_ID
    error_popup_telephone = RegisterAccountLocators.error_popup_telephone_XPATH
    password_field = RegisterAccountLocators.input_password_ID
    error_popup_password = RegisterAccountLocators.error_popup_password_XPATH
    confirm_password_field = RegisterAccountLocators.confirm_password_ID
    error_popup_confirm_password = RegisterAccountLocators.error_popup_confirm_password_XPATH
    checkbox = RegisterAccountLocators.click_checkbox_XPATH
    error_popup_checkbox = RegisterAccountLocators.error_popup_checkbox_XPATH
    submit_button = RegisterAccountLocators.click_submit_XPATH

    # Page elements

    def get_firstname_field(self):
        return self.get_element(self.firstname_field)

    def get_error_popup_firstname(self):
        return self.get_element(self.error_popup_firstname, locator_type='xpath')

    def get_lastname_field(self):
        return self.get_element(self.lastname_field)

    def get_error_popup_lastname(self):
        return self.get_element(self.error_popup_lastname, locator_type='xpath')

    def get_email_field(self):
        return self.get_element(self.email_field)

    def get_error_popup_email(self):
        return self.get_element(self.error_popup_email, locator_type='xpath')

    def get_telephone_field(self):
        return self.get_element(self.telephone_field)

    def get_error_popup_telephone(self):
        return self.get_element(self.error_popup_telephone, locator_type='xpath')

    def get_password_field(self):
        return self.get_element(self.password_field)

    def get_error_popup_password(self):
        return self.get_element(self.error_popup_password, locator_type='xpath')

    def get_confirm_password_field(self):
        return self.get_element(self.confirm_password_field)

    def get_error_popup_confirm_password(self):
        return self.get_element(self.error_popup_confirm_password, locator_type='xpath')

    def get_checkbox(self):
        return self.get_element(self.checkbox, locator_type='xpath')

    def get_error_popup_checkbox(self):
        return self.get_element(self.error_popup_checkbox, locator_type='xpath')

    def get_submit_button(self):
        return self.get_element(self.submit_button, locator_type='xpath')

    # Page actions
    def enter_firstname(self, firstname):
        self.send_keys_to_element(firstname, self.firstname_field)

    def enter_lastname(self, lastname):
        self.send_keys_to_element(lastname, self.lastname_field)

    def enter_email(self, email):
        self.send_keys_to_element(email, self.email_field)

    def enter_telephone(self, telephone):
        self.send_keys_to_element(telephone, self.telephone_field)

    def enter_password(self, password):
        self.send_keys_to_element(password, self.password_field)

    def enter_confirm_password(self, confirm):
        self.send_keys_to_element(confirm, self.confirm_password_field)

    def click_checkbox(self):
        self.click_element(self.checkbox, locator_type='xpath')

    def click_submit(self):
        self.click_element(self.submit_button, locator_type='xpath')
