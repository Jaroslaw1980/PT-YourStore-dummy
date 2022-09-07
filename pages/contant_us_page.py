from base.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.locators import ContantUSLocators
from utilities.base_urls import BaseUrls


class ContactUsPage(BasePage):

    # Url for contact us page
    base_url = BaseUrls.contact_us_page_url

    # Locators
    name_field = ContantUSLocators.input_name_ID
    error_add_name = ContantUSLocators.error_add_name_XPATH
    email_field = ContantUSLocators.input_email_ID
    error_add_email = ContantUSLocators.error_add_email_XPATH
    enquiry_field = ContantUSLocators.input_enquiry_ID
    error_add_enquiry = ContantUSLocators.error_add_enquiry_XPATH
    submit_button = ContantUSLocators.click_submit_CSS

    # Page elements
    def get_name_field(self):
        return self.get_element(self.name_field)

    def get_error_after_add_name(self):
        return self.get_element(self.error_add_name, locator_type='xpath')

    def get_email_field(self):
        return self.get_element(self.email_field)

    def get_error_after_add_email(self):
        return self.get_element(self.error_add_email, locator_type='xpath')

    def get_enquiry_field(self):
        return self.get_element(self.enquiry_field)

    def get_error_after_add_enquiry(self):
        return self.get_element(self.error_add_enquiry, locator_type='xpath')

    def get_submit_button(self):
        return self.get_element(self.submit_button, locator_type='css')

    # Page actions
    def enter_name(self, name):  # 3 - 32 characters
        self.send_keys_to_element(name, self.name_field)

    def get_error_add_name(self):
        error = self.get_error_after_add_name()
        message = error.text
        return message

    def enter_email(self, email_input):
        self.send_keys_to_element(email_input, self.email_field)

    def get_error_add_email(self):
        error = self.get_error_add_email()
        message = error.text
        return message

    def enter_enquiry(self, enquiry_input):  # 10 - 3000 characters
        self.send_keys_to_element(enquiry_input, self.enquiry_field)

    def get_error_add_enquiry(self):
        error = self.get_error_after_add_enquiry()
        message = error.text
        return message

    def click_submit(self):
        self.click_element(self.submit_button, locator_type='css')

