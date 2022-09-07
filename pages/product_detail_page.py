from locators.locators import ProductDetailPageLocators
from base.base_page import BasePage


class ProductDetailPage(BasePage):

    # Locators
    set_product_quantity = ProductDetailPageLocators.set_product_quantity_ID
    reviews_button = ProductDetailPageLocators.click_reviews_XPATH
    description_button = ProductDetailPageLocators.click_description_XPATH
    image = ProductDetailPageLocators.click_image_XPATH
    arrow_right = ProductDetailPageLocators.click_arrow_right_XPATH
    arrow_left = ProductDetailPageLocators.click_arrow_left_XPATH
    close_preview_button = ProductDetailPageLocators.close_preview_XPATH
    add_to_cart_button = ProductDetailPageLocators.add_to_cart_XPATH

    # Page elements
    def get_products_quantity(self):
        return self.get_element(self.set_product_quantity)

    def get_reviews_button(self):
        return self.get_element(self.reviews_button, locator_type='xpath')

    def get_description_button(self):
        return self.get_element(self.description_button, locator_type='xpath')

    def get_image(self):
        return self.get_element(self.image, locator_type='xpath')

    def get_arrow_right(self):
        return self.get_element(self.arrow_right, locator_type='xpath')

    def get_arrow_left(self):
        return self.get_element(self.arrow_left, locator_type='xpath')

    def get_close_preview_button(self):
        return self.get_element(self.close_preview_button, locator_type='xpath')

    def get_add_to_cart_button(self):
        return self.get_element(self.add_to_cart_button, locator_type='xpath')

    # Page actions
    def set_products_quantity(self, number):
        self.send_keys_to_element(number, self.set_product_quantity)

    def click_reviews(self):
        self.click_element(self.reviews_button, locator_type='xpath')

    def click_description(self):
        self.click_element(self.description_button, locator_type='xpath')

    def click_image(self):
        self.click_element(self.image, locator_type='xpath')

    def click_arrow_right(self, value):
        arrow = self.get_arrow_right()
        for i in range(value):
            arrow.click()

    def click_arrow_left(self, value):
        arrow = self.get_arrow_left()
        for i in range(value):
            arrow.click()

    def close_preview(self):
        self.click_element(self.close_preview_button, locator_type='xpath')

    def add_to_cart(self):
        self.click_element(self.add_to_cart_button, locator_type='xpath')

