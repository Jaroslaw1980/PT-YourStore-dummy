from Selenium.PTYourStore.locators.locators import Locators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class ProductListPage:

    def __init__(self, driver):
        self.driver = driver

        self.sort_by_list_pLp_ID = Locators.sort_by_list_pLp_ID
        self.sort_by_grid_pLp_ID = Locators.sort_by_grid_pLp_ID
        self.sort_by_text_pLp_ID = Locators.sort_by_text_pLp_ID
        self.how_many_on_page_pLp_ID = Locators.how_many_on_page_pLp_ID

    def sort_by_list(self):
        self.driver.find_element(By.ID, self.sort_by_list_pLp_ID).click()

    def sort_by_grid(self):
        self.driver.find_element(By.ID, self.sort_by_grid_pLp_ID).click()

    def sort_by_text(self, text):
        sort = self.driver.find_element(By.ID, self.sort_by_text_pLp_ID)
        options = Select(sort)
        options.select_by_visible_text(text)

    def how_many_on_page(self, number):
        input_limit = self.driver.find_element(By.ID, self.how_many_on_page_pLp_ID)
        options = Select(input_limit)
        options.select_by_visible_text(number)


