from pages.base_page import BasePage
from utilities.base_urls import BaseUrls
from selenium.webdriver.common.by import By
from locators.locators import ProductReturnsPageLocators


class ProductReturnsPage(BasePage):

    base_url = BaseUrls.product_returns_page_url

    add_firstname_ID = ProductReturnsPageLocators.add_firstname_ID
    error_add_firstname_XPATH = ProductReturnsPageLocators.error_add_firstname_XPATH
    add_lastname_ID = ProductReturnsPageLocators.add_lastname_ID
    error_add_lastname_XPATH = ProductReturnsPageLocators.error_add_lastname_XPATH
    add_email_ID = ProductReturnsPageLocators.add_email_ID
    add_error_email_XPATH = ProductReturnsPageLocators.add_error_email_XPATH
    add_telephone_ID = ProductReturnsPageLocators.add_telephone_ID
    error_add_telephone_XPATH = ProductReturnsPageLocators.error_add_telephone_XPATH
    add_order_id_ID = ProductReturnsPageLocators.add_order_id_ID
    error_order_id_XPATH = ProductReturnsPageLocators.error_order_id_XPATH
    add_order_date_ID = ProductReturnsPageLocators.add_order_date_ID
    add_product_name_ID = ProductReturnsPageLocators.add_product_name_ID
    error_add_product_name_XPATH = ProductReturnsPageLocators.error_add_product_name_XPATH
    add_product_code_ID = ProductReturnsPageLocators.add_product_code_ID
    error_product_code_XPATH = ProductReturnsPageLocators.error_product_code_XPATH
    add_quantity_ID = ProductReturnsPageLocators.add_quantity_ID
    add_reason_for_return_XPATH = ProductReturnsPageLocators.add_reason_for_return_XPATH
    error_reason_for_reutrn_XPATH = ProductReturnsPageLocators.error_reason_for_reutrn_XPATH
    check_if_product_was_opened_XPATH = ProductReturnsPageLocators.check_if_product_was_opened_XPATH
    add_details_ID = ProductReturnsPageLocators.add_details_ID
    click_back_button_LINK_TEXT = ProductReturnsPageLocators.click_back_button_LINK_TEXT
    click_submit_button_CSS_SELECTOR = ProductReturnsPageLocators.click_submit_button_CSS_SELECTOR

    def add_firstname(self, name):
        first_name = self.driver.find_element(By.ID, self.add_firstname_ID)
        first_name.clear()
        first_name.send_keys(name)

    def error_add_firstname(self):
        error_name = self.driver.find_element(By.XPATH, self.error_add_firstname_XPATH)
        return error_name

    def add_lastname(self, lastname):
        last_name = self.driver.find_element(By.ID, self.add_lastname_ID)
        last_name.clear()
        last_name.send_keys(lastname)

    def error_add_lastname(self):
        error_lastname = self.driver.find_element(By.XPATH, self.error_add_lastname_XPATH)
        return error_lastname

    def add_email(self, email):
        email_input = self.driver.find_element(By.ID, self.add_email_ID)
        email_input.clear()
        email_input.send_keys(email)

    def error_add_email(self):
        self.driver.find_element(By.XPATH, self.add_error_email_XPATH)

    def add_telephone(self, telephone):
        telephone_input = self.driver.find_element(By.ID, self.add_telephone_ID)
        telephone_input.clear()
        telephone_input.send_keys(telephone)

    def error_add_telephone(self):
        self.driver.find_element(By.XPATH, self.error_add_telephone_XPATH)

    def add_order_id(self, order_id):
        order_input = self.driver.find_element(By.ID, self.add_order_id_ID)
        order_input.clear()
        order_input.send_keys(order_id)

    def error_order_id(self):
        self.driver.find_element(By.XPATH, self.error_order_id_XPATH)

    def add_order_date(self, date):
        date_input = self.driver.find_element(By.ID, self.add_order_date_ID)
        date_input.clear()
        date_input.send_keys(date)

    def add_product_name(self, product_name):
        product = self.driver.find_element(By.ID, self.add_product_name_ID)
        product.clear()
        product.send_keys(product_name)

    def error_add_product_name(self):
        self.driver.find_element(By.XPATH, self.error_add_product_name_XPATH)

    def add_product_code(self, product_code):
        code = self.driver.find_element(By.ID, self.add_product_code_ID)
        code.clear()
        code.send_keys(product_code)

    def error_add_product_code(self):
        self.driver.find_element(By.XPATH, self.error_product_code_XPATH)

    def add_quantity(self, quantity):
        quantity_input = self.driver.find_element(By.ID, self.add_quantity_ID)
        quantity_input.clear()
        quantity_input.send_keys(quantity)

    def add_reason_for_return(self, reason):
        radio_list = self.driver.find_elements(By.XPATH, self.add_reason_for_return_XPATH)
        radio_list[reason].click()
        return radio_list

    def error_add_reason_for_return(self):
        self.driver.find_element(By.XPATH, self.error_reason_for_reutrn_XPATH)

    def check_if_product_was_opened(self, check):
        radio_list2 = self.driver.find_elements(By.XPATH, self.check_if_product_was_opened_XPATH)
        radio_list2[check].click()
        return radio_list2

    def add_details(self, details):
        details_input = self.driver.find_element(By.ID, self.add_details_ID)
        details_input.clear()
        details_input.send_keys(details)

    def click_back_button(self):
        self.driver.find_element(By.LINK_TEXT, self.click_back_button_LINK_TEXT)

    def click_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_submit_button_CSS_SELECTOR)

