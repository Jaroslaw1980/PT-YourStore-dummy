from locators.locators import ProductDetailPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductDetailPage(BasePage):

    set_product_quantity_pDp_ID = ProductDetailPageLocators.set_product_quantity_pDp_ID
    click_reviews_pDp_XPATH = ProductDetailPageLocators.click_reviews_pDp_XPATH
    click_description_pDp_XPATH = ProductDetailPageLocators.click_description_pDp_XPATH
    click_image_pDp_XPATH = ProductDetailPageLocators.click_image_pDp_XPATH
    click_arrow_right_pDp_XPATH = ProductDetailPageLocators.click_arrow_right_pDp_XPATH
    click_arrow_left_pDp_XPATH = ProductDetailPageLocators.click_arrow_left_pDp_XPATH
    close_preview_pDp_XPATH = ProductDetailPageLocators.close_preview_pDp_XPATH
    add_to_cart_pDp_XPATH = ProductDetailPageLocators.add_to_cart_pDp_XPATH

    def set_products_quantity(self, number):
        self.driver.find_element(By.ID, self.set_product_quantity_pDp_ID).clear()
        self.driver.find_element(By.ID, self.set_product_quantity_pDp_ID).send_keys(number)

    def click_reviews(self):
        self.driver.find_element(By.XPATH, self.click_reviews_pDp_XPATH).click()

    def click_description(self):
        self.driver.find_element(By.XPATH, self.click_description_pDp_XPATH).click()

    def click_image(self):
        self.driver.find_element(By.XPATH, self.click_image_pDp_XPATH).click()

    def click_arrow_right(self, value):
        arrow = self.driver.find_element(By.XPATH, self.click_arrow_right_pDp_XPATH)
        for i in range(value):
            arrow.click()

    def click_arrow_left(self, value):
        arrow = self.driver.find_element(By.XPATH, self.click_arrow_left_pDp_XPATH)
        for i in range(value):
            arrow.click()

    def close_preview(self):
        self.driver.find_element(By.XPATH, self.close_preview_pDp_XPATH).click()

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_pDp_XPATH).click()

