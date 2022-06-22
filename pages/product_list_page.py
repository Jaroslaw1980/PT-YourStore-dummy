from locators.locators import ProductListPageLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductListPage(BasePage):

    sort_by_list_ID = ProductListPageLocators.sort_by_list_ID
    sort_by_grid_ID = ProductListPageLocators.sort_by_grid_ID
    sort_by_text_ID = ProductListPageLocators.sort_by_text_ID
    how_many_on_page_ID = ProductListPageLocators.how_many_on_page_ID

    def sort_by_list(self):
        self.driver.find_element(By.ID, self.sort_by_list_ID).click()

    def sort_by_grid(self):
        self.driver.find_element(By.ID, self.sort_by_grid_ID).click()

    def sort_by_text(self, text):
        sort = self.driver.find_element(By.ID, self.sort_by_text_ID)
        options = Select(sort)
        options.select_by_visible_text(text)

    def how_many_on_page(self, number):
        input_limit = self.driver.find_element(By.ID, self.how_many_on_page_ID)
        options = Select(input_limit)
        options.select_by_visible_text(number)


