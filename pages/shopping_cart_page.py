from locators.locators import ShoppingCartLocators
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ShoppingCart(BasePage):
    # Locators
    number_of_items = ShoppingCartLocators.number_of_items_XPATH
    items_change_button = ShoppingCartLocators.number_of_items_XPATH
    remove_from_cart_button = ShoppingCartLocators.remove_from_cart_XPATH
    use_coupon_bar = ShoppingCartLocators.use_coupon_XPATH
    coupon_code_field = ShoppingCartLocators.input_coupon_code_ID
    apply_coupon_button = ShoppingCartLocators.submit_coupon_CSS_SELECTOR
    checkout_button = ShoppingCartLocators.click_checkout_LINK_TEXT
    product_list_in_cart = ShoppingCartLocators.product_list_cart_XPATH
    cart_total_value = ShoppingCartLocators.cart_total_value_XPATH

    # Page elements

    def get_change_number_of_items(self):
        return self.get_element(self.number_of_items, locator_type='xpath')

    def get_items_change_button(self):
        return self.get_element(self.items_change_button, locator_type='xpath')

    def get_remove_from_cart_button(self):
        return self.get_element(self.remove_from_cart_button, locator_type='xpath')

    def get_use_coupon_bar(self):
        return self.get_element(self.use_coupon_bar, locator_type='xpath')

    def get_coupon_code_field(self):
        return self.get_element(self.coupon_code_field)

    def get_apply_coupon_button(self):
        return self.get_element(self.apply_coupon_button, locator_type='css')

    def get_checkout_button(self):
        return self.get_element(self.checkout_button, locator_type='link_text')

    # Page actions

    def change_number_of_items(self, number):
        self.send_keys_to_element(number, self.number_of_items, locator_type='xpath')

    def submit_items_change(self):
        self.click_element(self.items_change_button, locator_type='xpath')

    def remove_from_cart(self):
        self.click_element(self.remove_from_cart_button, locator_type='xpath')

    def use_coupon(self):
        self.click_element(self.use_coupon_bar, locator_type='xpath')

    def enter_coupon_code(self, code):
        self.send_keys_to_element(code, self.coupon_code_field)

    def submit_coupon(self):
        self.click_element(self.apply_coupon_button, locator_type='css')

    def click_checkout(self):
        self.click_element(self.checkout_button, locator_type='link_text')

    def price_compare(self):

        """Method comparing summ of the all produts prices in cart with total price in the cart"""

        products_list = self.driver.find_elements(By.XPATH, self.product_list_in_cart)
        products_text = []
        removed_currency = []

        for product in products_list:
            products_text.append(product.get_attribute("innerHTML"))

        for element in products_text:
            removed_currency.append(float(element[1:]))

        sum_total = 0
        for i in removed_currency:
            sum_total = i + sum_total

        total_cart = self.driver.find_element(By.XPATH, self.cart_total_value).text
        total_cart = float(total_cart[1:])

        assert sum_total == total_cart, "Prices are not match"
