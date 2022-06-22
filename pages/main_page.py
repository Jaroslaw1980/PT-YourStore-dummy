from pages.register_account_page import RegisterAccount
from pages.login_page import LoginPage
from locators.locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.base_urls import BaseUrls


class MainPage(BasePage):

    base_url = BaseUrls.main_page_url

    choose_currency_XPATH = MainPageLocators.choose_currency_XPATH
    dropdown_elements_XPATH = MainPageLocators.dropdown_elements_XPATH
    click_currency_CSS_SELECTOR = MainPageLocators.click_currency_CSS_SELECTOR
    choose_currency_EUR_CSS_SELECTOR = MainPageLocators.choose_currency_EUR_CSS_SELECTOR
    choose_currency_GBP_CSS_SELECTOR = MainPageLocators.choose_currency_GBP_CSS_SELECTOR
    choose_currency_USD_CSS_SELECTOR = MainPageLocators.choose_currency_USD_CSS_SELECTOR
    your_store_button_LINK_TEXT = MainPageLocators.your_store_button_LINK_TEXT
    click_cart_ID = MainPageLocators.click_cart_ID
    searching_NAME = MainPageLocators.searching_NAME
    click_search_button_CSS_SELECTOR = MainPageLocators.click_search_button_CSS_SELECTOR
    click_my_account_CSS_SELECTOR = MainPageLocators.click_my_account_CSS_SELECTOR
    click_register_XPATH = MainPageLocators.click_register_XPATH
    click_login_XPATH = MainPageLocators.click_login_XPATH
    click_wish_list_ID = MainPageLocators.click_wish_list_ID
    click_shopping_cart_CSS_SELECTOR = MainPageLocators.click_shopping_cart_CSS_SELECTOR
    click_checkout_CSS_SELECTOR = MainPageLocators.click_checkout_CSS_SELECTOR
    mouse_over_bar_LINK_TEXT = MainPageLocators.mouse_over_bar_LINK_TEXT
    click_logout_XPATH = MainPageLocators.click_logout_XPATH
    click_continue_after_logout_XPATH = MainPageLocators.click_continue_after_logout_XPATH
    add_to_cart_button_XPATH = MainPageLocators.add_to_cart_button_XPATH

    def choose_currency(self, currency):  # "€ Euro","£ Pound Sterling","$ US Dollar"
        self.driver.find_element(By.XPATH, self.choose_currency_XPATH).click()
        elements = self.driver.find_elements(By.XPATH, self.dropdown_elements_XPATH)
        for element in elements:
            if element.text == currency:
                element.click()
                break

    def click_currency(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_currency_CSS_SELECTOR).click()

    def choose_currency_eur(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_currency_EUR_CSS_SELECTOR).click()

    def choose_currency_gbp(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_currency_GBP_CSS_SELECTOR).click()

    def choose_currency_usd(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_currency_USD_CSS_SELECTOR).click()

    def click_yourstore_button(self):
        self.driver.find_element(By.LINK_TEXT, self.your_store_button_LINK_TEXT).click()

    def click_cart(self):
        self.driver.find_element(By.ID, self.click_cart_ID).click()

    def searching(self, search):
        self.driver.find_element(By.NAME, self.searching_NAME).clear()
        self.driver.find_element(By.NAME, self.searching_NAME).send_keys(search)

    def click_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_search_button_CSS_SELECTOR).click()

    def click_my_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_my_account_CSS_SELECTOR).click()

    def click_register(self):
        self.driver.find_element(By.XPATH, self.click_register_XPATH).click()
        registerpage = RegisterAccount(self.driver)
        return registerpage

    def click_login(self):
        self.driver.find_element(By.XPATH, self.click_login_XPATH).click()
        loginpage = LoginPage(self.driver)
        return loginpage

    def click_wish_list(self):
        self.driver.find_element(By.ID, self.click_wish_list_ID).click()

    def click_shopping_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_shopping_cart_CSS_SELECTOR).click()

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_checkout_CSS_SELECTOR).click()

    def mouse_over_bar(self):
        mouse = self.driver.find_element(By.LINK_TEXT, self.mouse_over_bar_LINK_TEXT)
        webdriver.ActionChains(self.driver).move_to_element(mouse).perform()
        self.driver.find_element(By.XPATH, "//a[text()='Monitors (2)']").click() # monitors

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.click_logout_XPATH).click()

    def click_continue_after_logout(self):
        self.driver.find_element(By.XPATH, self.click_continue_after_logout_XPATH).click()

    def link_checker(self, link):
        page = self.driver.find_element(By.LINK_TEXT, link)
        page.click()
        pagetitle = self.driver.title
        assert pagetitle == link
        self.driver.back()

    def add_to_cart(self, value):
        product_list = self.driver.find_elements(By.XPATH, self.add_to_cart_button_XPATH)
        product_list[value].click()






