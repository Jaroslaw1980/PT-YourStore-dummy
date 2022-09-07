from base.base_page import BasePage
from utilities.base_urls import BaseUrls
from selenium.webdriver.common.by import By
from locators.locators import ProductReturnsPageLocators


class ProductReturnsPage(BasePage):
    # Url for product returns page locators
    base_url = BaseUrls.product_returns_page_url

    # Locators
    firstname_field = ProductReturnsPageLocators.add_firstname_ID
    error_add_firstname = ProductReturnsPageLocators.error_add_firstname_XPATH
    lastname_field = ProductReturnsPageLocators.add_lastname_ID
    error_add_lastname = ProductReturnsPageLocators.error_add_lastname_XPATH
    email_field = ProductReturnsPageLocators.add_email_ID
    error_add_email = ProductReturnsPageLocators.add_error_email_XPATH
    telephone_field = ProductReturnsPageLocators.add_telephone_ID
    error_add_telephone = ProductReturnsPageLocators.error_add_telephone_XPATH
    order_id_field = ProductReturnsPageLocators.add_order_id_ID
    error_after_order_id = ProductReturnsPageLocators.error_order_id_XPATH
    order_date_field = ProductReturnsPageLocators.add_order_date_ID
    product_name_field = ProductReturnsPageLocators.add_product_name_ID
    error_after_add_product_name = ProductReturnsPageLocators.error_add_product_name_XPATH
    product_code_field = ProductReturnsPageLocators.add_product_code_ID
    error_product_code = ProductReturnsPageLocators.error_product_code_XPATH
    quantity_field = ProductReturnsPageLocators.add_quantity_ID
    reason_for_return_field = ProductReturnsPageLocators.add_reason_for_return_XPATH
    error_reason_for_return = ProductReturnsPageLocators.error_reason_for_reutrn_XPATH
    check_if_product_was_opened = ProductReturnsPageLocators.check_if_product_was_opened_XPATH
    details_field = ProductReturnsPageLocators.add_details_ID
    back_button = ProductReturnsPageLocators.click_back_button_LINK_TEXT
    submit_button = ProductReturnsPageLocators.click_submit_button_CSS_SELECTOR

    # Page elements

    def get_firstname_field(self):
        return self.get_element(self.firstname_field)

    def get_error_after_add_firstname(self):
        return self.get_element(self.error_add_firstname, locator_type='xpath')

    def get_lastname_field(self):
        return self.get_element(self.lastname_field)

    def get_error_after_add_lastname(self):
        return self.get_element(self.error_add_lastname, locator_type='xpath')

    def get_email_field(self):
        return self.get_element(self.email_field)

    def get_error_after_add_email(self):
        return self.get_element(self.error_add_email, locator_type='xpath')

    def get_telephone_field(self):
        return self.get_element(self.telephone_field)

    def get_error_after_add_telephone(self):
        return self.get_element(self.error_add_telephone, locator_type='xpath')

    def get_order_id_field(self):
        return self.get_element(self.order_id_field)

    def get_error_after_order_id_input(self):
        return self.get_element(self.error_after_order_id, locator_type='xpath')

    def get_order_date_field(self):
        return self.get_element(self.order_date_field)

    def get_product_name_field(self):
        return self.get_element(self.product_name_field)

    def get_error_afer_add_product_name(self):
        return self.get_element(self.error_after_add_product_name, locator_type='xpath')

    def get_product_code_field(self):
        return self.get_element(self.product_code_field)

    def get_error_after_product_code_input(self):
        return self.get_element(self.error_product_code, locator_type='xpath')

    def get_quantity_field(self):
        return self.get_element(self.quantity_field)

    def get_reason_for_return_field(self):
        return self.get_elements(self.reason_for_return_field, locator_type='xpath')

    def get_error_reason_for_return(self):
        return self.get_element(self.error_reason_for_return, locator_type='xpath')

    def get_check_if_product_was_opened(self):
        return self.get_elements(self.check_if_product_was_opened, locator_type='xpath')

    def get_add_details_field(self):
        return self.get_element(self.details_field)

    def get_back_button(self):
        return self.get_element(self.back_button, locator_type='link_text')

    def get_submit_button(self):
        return self.get_element(self.submit_button, locator_type='css')

    # Page actions

    def enter_firstname(self, name):
        self.send_keys_to_element(name, self.firstname_field)

    def find_error_add_firstname(self):
        error_name = self.get_error_after_add_firstname()
        return error_name

    def enter_lastname(self, lastname):
        self.send_keys_to_element(lastname, self.lastname_field)

    def find_error_add_lastname(self):
        error_lastname = self.get_error_after_add_lastname()
        return error_lastname

    def enter_email(self, email):
        self.send_keys_to_element(email, self.email_field)

    def find_error_add_email(self):
        error_email = self.get_error_after_add_email()
        return error_email

    def enter_telephone(self, telephone):
        self.send_keys_to_element(telephone, self.telephone_field)

    def find_error_add_telephone(self):
        telephone_error = self.get_error_after_add_telephone()
        return telephone_error

    def enter_order_id(self, order_id):
        self.send_keys_to_element(order_id, self.order_id_field)

    def find_error_order_id(self):
        error_order = self.get_error_after_order_id_input()
        return error_order

    def enter_order_date(self, date):
        self.send_keys_to_element(date, self.order_date_field)

    def enter_product_name(self, product_name):
        self.send_keys_to_element(product_name, self.product_name_field)

    def find_error_add_product_name(self):
        error_product = self.get_error_afer_add_product_name()
        return error_product

    def enter_product_code(self, product_code):
        self.send_keys_to_element(product_code, self.product_code_field)

    def find_error_add_product_code(self):
        error = self.get_error_after_product_code_input()
        return error

    def enter_quantity(self, quantity):
        self.send_keys_to_element(quantity, self.quantity_field)

    def enter_reason_for_return(self, reason):
        radio_list = self.get_reason_for_return_field()
        radio_list[reason].click()
        return radio_list

    def find_error_add_reason_for_return(self):
        error = self.get_error_reason_for_return()
        return error

    def check_product_opened(self, check):
        radio_list = self.get_check_if_product_was_opened()
        radio_list[check].click()
        return radio_list

    def enter_details(self, details):
        self.send_keys_to_element(details, self.details_field)

    def click_back_button(self):
        self.click_element(self.back_button, locator_type='link_text')

    def click_submit_button(self):
        self.click_element(self.submit_button, locator_type='css')
