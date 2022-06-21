from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.locators import ContantUSLocators
from utilities.base_urls import BaseUrls


class ContactUsPage(BasePage):

    base_url = BaseUrls.contact_us_page_url

    input_name_ID = ContantUSLocators.input_name_ID
    error_add_name_XPATH = ContantUSLocators.error_add_name_XPATH
    input_email_ID = ContantUSLocators.input_email_ID
    error_add_email_XPATH = ContantUSLocators.error_add_email_XPATH
    input_enquiry_ID = ContantUSLocators.input_enquiry_ID
    error_add_enquiry_XPATH = ContantUSLocators.error_add_enquiry_XPATH
    click_submit_CSS = ContantUSLocators.click_submit_CSS

    def add_name(self, name):  # 3 - 32 characters
        first_name = self.driver.find_element(By.ID, self.input_name_ID)
        first_name.clear()
        first_name.send_keys(name)

    def error_add_name(self):
        error = self.driver.find_element(By.XPATH, self.error_add_name_XPATH)
        message = error.text
        return message

    def add_email(self, email_input):
        email = self.driver.find_element(By.ID, self.input_email_ID)
        email.clear()
        email.send_keys(email_input)

    def error_add_email(self):
        error = self.driver.find_element(By.XPATH, self.error_add_email_XPATH)
        message = error.text
        return message

    def add_enquiry(self, enquiry_input):  # 10 - 3000 characters
        enquiry = self.driver.find_element(By.ID, self.input_enquiry_ID)
        enquiry.clear()
        enquiry.send_keys(enquiry_input)

    def error_add_enquiry(self):
        error = self.driver.find_element(By.XPATH, self.error_add_enquiry_XPATH)
        message = error.text
        return message

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_submit_CSS).click()

