### "Product list page" URL, Locators, Page elements and Page actions ###

from locators.locators import ProductListPageLocators
from selenium.webdriver.support.select import Select
from base.base_page import BasePage


class ProductListPage(BasePage):

    # Locators
    sort_by_list = ProductListPageLocators.sort_by_list_ID
    sort_by_grid = ProductListPageLocators.sort_by_grid_ID
    sort_by_text = ProductListPageLocators.sort_by_text_ID
    how_many_on_page = ProductListPageLocators.how_many_on_page_ID

    # Page elements

    def get_sort_by_list_option(self):
        return self.get_element(self.sort_by_list)

    def get_sort_by_grid_option(self):
        return self.get_element(self.sort_by_grid)

    def get_sort_by_text_option(self):
        return self.get_element(self.sort_by_text)

    def get_how_many_on_page_option(self):
        return self.get_element(self.how_many_on_page)

    # Page actions
    def click_on_sort_by_list(self):
        self.click_element(self.sort_by_list)

    def click_on_sort_by_grid(self):
        self.click_element(self.sort_by_grid)

    def choose_sort_by_text(self, text):
        sort = self.get_sort_by_text_option()
        options = Select(sort)
        options.select_by_visible_text(text)

    def set_how_many_on_page(self, number):
        input_limit = self.get_how_many_on_page_option()
        options = Select(input_limit)
        options.select_by_visible_text(number)


