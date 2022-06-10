from locators.locators import Locators
from selenium.webdriver.common.by import By


class ShoppingCart:

    def __init__(self, driver):
        self.driver = driver

        self.number_of_items_shpCrt_XPATH = Locators.number_of_items_shpCrt_XPATH
        self.submit_items_change_shpCrt_XPATH = Locators.number_of_items_shpCrt_XPATH
        self.remove_from_cart_shpCrt_XPATH = Locators.remove_from_cart_shpCrt_XPATH
        self.use_coupon_shpCrt_XPATH = Locators.use_coupon_shpCrt_XPATH
        self.input_coupon_code_shpCrt_ID = Locators.input_coupon_code_shpCrt_ID
        self.submit_coupon_shpCrt_CSS_SELECTOR = Locators.submit_coupon_shpCrt_CSS_SELECTOR
        self.click_checkout_shpCrt_LINK_TEXT = Locators.click_checkout_shpCrt_LINK_TEXT
        self.product_list_cart_shpCrt_XPATH = Locators.product_list_cart_shpCrt_XPATH
        self.cart_total_value_shpCrt_XPATH = Locators.cart_total_value_shpCrt_XPATH

    def change_number_of_items(self, number):
        self.driver.find_element(By.XPATH, self.number_of_items_shpCrt_XPATH).send_keys(number)

    def submit_items_change(self):
        self.driver.find_element(By.XPATH, self.submit_items_change_shpCrt_XPATH).click()

    def remove_from_cart(self):
        self.driver.find_element(By.XPATH, self.remove_from_cart_shpCrt_XPATH).click()

    def use_coupon(self):
        self.driver.find_element(By.XPATH, self.use_coupon_shpCrt_XPATH).click()

    def input_coupon_code(self, code):
        self.driver.find_element(By.ID, self.input_coupon_code_shpCrt_ID).send_keys(code)

    def submit_coupon(self):
        self.driver.find_element(By.CSS_SELECTOR, self.submit_coupon_shpCrt_CSS_SELECTOR).click()

    def click_checkout(self):
        self.driver.find_element(By.LINK_TEXT, self.click_checkout_shpCrt_LINK_TEXT).click()

    def price_compare(self):

        """Method comparing summ of the all produts prices in cart with total price in the cart"""

        products_list = self.driver.find_elements(By.XPATH, self.product_list_cart_shpCrt_XPATH)
        products_text = []
        removed_currency = []

        for product in products_list:
            products_text.append(product.get_attribute("innerHTML"))

        for element in products_text:
            removed_currency.append(float(element[1:]))

        sum_total = 0
        for i in removed_currency:
            sum_total = i + sum_total

        total_cart = self.driver.find_element(By.XPATH, self.cart_total_value_shpCrt_XPATH).text
        total_cart = float(total_cart[1:])

        assert sum_total == total_cart, "Prices are not match"
