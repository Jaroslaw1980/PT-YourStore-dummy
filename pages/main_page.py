### "Main Page" URL, Locators, Page elements and Page actions ###

from locators.locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.base_urls import BaseUrls


class MainPage(BasePage):

    # Url for main page locators
    base_url = BaseUrls.main_page_url

    # Locators
    choose_currency = MainPageLocators.choose_currency_XPATH
    dropdown_elements = MainPageLocators.dropdown_elements_XPATH
    currency_button = MainPageLocators.click_currency_CSS_SELECTOR
    currency_euro = MainPageLocators.choose_currency_EUR_CSS_SELECTOR
    currency_gbp = MainPageLocators.choose_currency_GBP_CSS_SELECTOR
    currency_usd = MainPageLocators.choose_currency_USD_CSS_SELECTOR
    your_store_button = MainPageLocators.your_store_button_LINK_TEXT
    cart_button = MainPageLocators.click_cart_ID
    search_bar = MainPageLocators.searching_NAME
    search_button = MainPageLocators.click_search_button_CSS_SELECTOR
    my_account_button = MainPageLocators.click_my_account_CSS_SELECTOR
    register_button = MainPageLocators.click_register_XPATH
    login_button = MainPageLocators.click_login_XPATH
    wishlist_button = MainPageLocators.click_wish_list_ID
    shopping_cart_button = MainPageLocators.click_shopping_cart_CSS_SELECTOR
    checkout_button = MainPageLocators.click_checkout_CSS_SELECTOR
    mouse_over_bar = MainPageLocators.mouse_over_bar_LINK_TEXT
    logout_button = MainPageLocators.click_logout_XPATH
    continue_after_logout_button = MainPageLocators.click_continue_after_logout_XPATH
    add_to_cart_button = MainPageLocators.add_to_cart_button_XPATH

    # Page elements

    def get_choose_currency(self):
        return self.get_element(self.choose_currency, locator_type='xpath')

    def get_currency_button(self):
        return self.get_element(self.currency_button, locator_type='css')

    def get_currency_euro(self):
        return self.get_element(self.currency_euro, locator_type='css')

    def get_currency_gbp(self):
        return self.get_element(self.currency_gbp, locator_type='css')

    def get_currency_usd(self):
        return self.get_element(self.currency_usd, locator_type='css')

    def get_your_store_button(self):
        return self.get_element(self.your_store_button, locator_type='link_text')

    def get_cart_button(self):
        return self.get_element(self.cart_button)

    def get_search_bar(self):
        return self.get_element(self.search_bar, locator_type='name')

    def get_search_button(self):
        return self.get_element(self.search_button, locator_type='css')

    def get_my_account_button(self):
        return self.get_element(self.my_account_button, locator_type='css')

    def get_register_button(self):
        return self.get_element(self.register_button, locator_type='xpath')

    def get_login_button(self):
        return self.get_element(self.login_button, locator_type='xpath')

    def get_wishlist_button(self):
        return self.get_element(self.wishlist_button)

    def get_shopping_cart_button(self):
        return self.get_element(self.shopping_cart_button, locator_type='css')

    def get_checkout_button(self):
        return self.get_element(self.checkout_button, locator_type='css')

    def get_mouse_over_bar(self):
        return self.get_element(self.mouse_over_bar, locator_type='link_text')

    def get_logout_button(self):
        return self.get_element(self.logout_button, locator_type='xpath')

    def get_continue_after_logout_button(self):
        return self.get_element(self.continue_after_logout_button, locator_type='xpath')

    def get_add_to_cart_button(self):
        return self.get_element(self.add_to_cart_button, locator_type='xpath')

    # Page actions
    def get_currency(self, currency):  # "€ Euro","£ Pound Sterling","$ US Dollar"
        self.get_choose_currency()
        elements = self.get_elements(self.dropdown_elements, locator_type='xpath')
        for element in elements:
            if element.text == currency:
                element.click()
                break

    def click_currency(self):
        self.click_element(self.currency_button, locator_type='css')

    def choose_currency_eur(self):
        self.click_element(self.currency_euro, locator_type='css')

    def choose_currency_gbp(self):
        self.click_element(self.currency_gbp, locator_type='css')

    def choose_currency_usd(self):
        self.click_element(self.currency_usd, locator_type='css')

    def click_yourstore_button(self):
        self.click_element(self.your_store_button, locator_type='link_text')

    def click_cart(self):
        self.click_element(self.cart_button)

    def searching(self, search):
        self.send_keys_to_element(search, self.search_bar, locator_type='name')

    def click_search_button(self):
        self.click_element(self.search_button, locator_type='css')

    def click_my_account(self):
        self.click_element(self.my_account_button, locator_type='css')

    def click_register(self):
        self.click_element(self.register_button, locator_type='xpath')

    def click_login(self):
        self.click_element(self.login_button, locator_type='xpath')

    def click_wish_list(self):
        self.click_element(self.wishlist_button)

    def click_shopping_cart(self):
        self.click_element(self.shopping_cart_button, locator_type='css')

    def click_checkout(self):
        self.click_element(self.checkout_button, locator_type='css')

    def perform_mouse_over_bar(self):
        mouse = self.get_element(self.mouse_over_bar, locator_type='link_text')
        webdriver.ActionChains(self.driver).move_to_element(mouse).perform()
        self.driver.find_element(By.XPATH, "//a[text()='Monitors (2)']").click() # monitors

    def click_logout(self):
        self.click_element(self.logout_button, locator_type='xpath')

    def click_continue_after_logout(self):
        self.click_element(self.continue_after_logout_button, locator_type='xpath')

    def link_checker(self, link):
        page = self.driver.find_element(By.LINK_TEXT, link)
        page.click()
        pagetitle = self.driver.title
        assert pagetitle == link
        self.driver.back()

    def add_to_cart(self, value):
        product_list = self.get_elements(self.add_to_cart_button, locator_type='xpath')
        product_list[value].click()






