from locators.locators import RegisterAccountLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.base_urls import BaseUrls


class RegisterAccount(BasePage):

    base_url = BaseUrls.register_page_url

    input_firstname_RegAcc_ID = RegisterAccountLocators.input_firstname_RegAcc_ID
    error_popup_firstname_RegAcc_XPATH = RegisterAccountLocators.error_popup_firstname_RegAcc_XPATH
    input_lastname_RegAcc_ID = RegisterAccountLocators.input_lastname_RegAcc_ID
    error_popup_lastname_Regcc_XPATH = RegisterAccountLocators.error_popup_lastname_Regcc_XPATH
    input_email_RegAcc_ID = RegisterAccountLocators.input_email_RegAcc_ID
    error_popup_email_RegAcc_XPATH = RegisterAccountLocators.error_popup_email_RegAcc_XPATH
    input_telephone_RegAcc_ID = RegisterAccountLocators.input_telephone_RegAcc_ID
    error_popup_telephone_RegAcc_XPATH = RegisterAccountLocators.error_popup_telephone_RegAcc_XPATH
    input_password_RegAcc_ID = RegisterAccountLocators.input_password_RegAcc_ID
    error_popup_password_RegAcc_XPATH = RegisterAccountLocators.error_popup_password_RegAcc_XPATH
    confirm_password_RegAcc_ID = RegisterAccountLocators.confirm_password_RegAcc_ID
    error_popup_confirm_password_RegAcc_XPATH = RegisterAccountLocators.error_popup_confirm_password_RegAcc_XPATH
    click_checkbox_RegAcc_XPATH = RegisterAccountLocators.click_checkbox_RegAcc_XPATH
    error_popup_checkbox_RegACC_XPATH = RegisterAccountLocators.error_popup_checkbox_RegAcc_XPATH
    click_submit_RegAcc_XPATH = RegisterAccountLocators.click_submit_RegAcc_XPATH

    def input_firstname(self, firstname):
        self.driver.find_element(By.ID, self.input_firstname_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_firstname_RegAcc_ID).send_keys(firstname)

    def error_popup_firstname(self):
        popup = self.driver.find_element(By.XPATH, self.error_popup_firstname_RegAcc_XPATH)
        return popup

    def input_lastname(self, lastname):
        self.driver.find_element(By.ID, self.input_lastname_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_lastname_RegAcc_ID).send_keys(lastname)

    def error_popup_lastname(self):
        popup = self.driver.find_element(By.XPATH, self.error_popup_lastname_Regcc_XPATH)
        return popup

    def input_email(self, email):
        self.driver.find_element(By.ID, self.input_email_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_email_RegAcc_ID).send_keys(email)

    def error_popup_email(self):
        popup = self.driver.find_element(By.XPATH, self.error_popup_email_RegAcc_XPATH)
        return popup

    def input_telephone(self, telephone):
        self.driver.find_element(By.ID, self.input_telephone_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_telephone_RegAcc_ID).send_keys(telephone)

    def error_popup_telephone(self):
        popup = self.driver.find_element(By.XPATH, self.error_popup_telephone_RegAcc_XPATH)
        return popup

    def input_password(self, password):
        self.driver.find_element(By.ID, self.input_password_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_password_RegAcc_ID).send_keys(password)

    def error_popup_password(self):
        popup = self.driver.find_element(By.XPATH, self.error_popup_password_RegAcc_XPATH)
        return popup

    def confirm_password(self, confirm):
        self.driver.find_element(By.ID, self.confirm_password_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.confirm_password_RegAcc_ID).send_keys(confirm)

    def error_popup_confirm_password(self):
        popup = self.driver.find_element(By.XPATH, self.error_popup_confirm_password_RegAcc_XPATH)
        return popup

    def checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, self.click_checkbox_RegAcc_XPATH)
        return checkbox

    def click_checkbox(self):
        self.driver.find_element(By.XPATH, self.click_checkbox_RegAcc_XPATH).click()

    def error_popup_checkbox(self):
        popup = self.driver.find_element(By.XPATH, self.error_popup_checkbox_RegACC_XPATH)
        return popup

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.click_submit_RegAcc_XPATH).click()

