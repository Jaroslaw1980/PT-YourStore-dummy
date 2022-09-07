from locators.locators import ProductDetailPageLocators
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductDetailPage(BasePage):

    set_product_quantity_ID = ProductDetailPageLocators.set_product_quantity_ID
    click_reviews_XPATH = ProductDetailPageLocators.click_reviews_XPATH
    click_description_XPATH = ProductDetailPageLocators.click_description_XPATH
    click_image_XPATH = ProductDetailPageLocators.click_image_XPATH
    click_arrow_right_XPATH = ProductDetailPageLocators.click_arrow_right_XPATH
    click_arrow_left_XPATH = ProductDetailPageLocators.click_arrow_left_XPATH
    close_preview_XPATH = ProductDetailPageLocators.close_preview_XPATH
    add_to_cart_XPATH = ProductDetailPageLocators.add_to_cart_XPATH

    def set_products_quantity(self, number):
        value = self.driver.find_element(By.ID, self.set_product_quantity_ID)
        value.clear()
        value.send_keys(number)

    def click_reviews(self):
        self.driver.find_element(By.XPATH, self.click_reviews_XPATH).click()

    def click_description(self):
        self.driver.find_element(By.XPATH, self.click_description_XPATH).click()

    def click_image(self):
        self.driver.find_element(By.XPATH, self.click_image_XPATH).click()

    def click_arrow_right(self, value):
        arrow = self.driver.find_element(By.XPATH, self.click_arrow_right_XPATH)
        for i in range(value):
            arrow.click()

    def click_arrow_left(self, value):
        arrow = self.driver.find_element(By.XPATH, self.click_arrow_left_XPATH)
        for i in range(value):
            arrow.click()

    def close_preview(self):
        self.driver.find_element(By.XPATH, self.close_preview_XPATH).click()

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_XPATH).click()

