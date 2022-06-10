from locators.locators import Locators
from selenium.webdriver.common.by import By


class ProductDetailPage:

    def __init__(self, driver):

        self.driver = driver

        self.set_product_quantity_pDp_ID = Locators.set_product_quantity_pDp_ID
        self.click_reviews_pDp_XPATH = Locators.click_reviews_pDp_XPATH
        self.click_description_pDp_XPATH = Locators.click_description_pDp_XPATH
        self.click_image_pDp_XPATH = Locators.click_image_pDp_XPATH
        self.click_arrow_right_pDp_XPATH = Locators.click_arrow_right_pDp_XPATH
        self.click_arrow_left_pDp_XPATH = Locators.click_arrow_left_pDp_XPATH
        self.close_preview_pDp_XPATH = Locators.close_preview_pDp_XPATH
        self.add_to_cart_pDp_XPATH = Locators.add_to_cart_pDp_XPATH

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

