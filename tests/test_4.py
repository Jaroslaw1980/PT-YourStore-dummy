from Selenium.PTYourStore.pages.mainPage import MainPage
from Selenium.PTYourStore.pages.shoppingCart import ShoppingCart
from Selenium.PTYourStore.utilities.BaseClass import BaseClass


class TestFour(BaseClass):

    def test_total_cart(self):

        main = MainPage(self.driver)
        cart = ShoppingCart(self.driver)

        main.add_to_cart(0)
        main.add_to_cart(1)
        main.click_shopping_cart()
        cart.price_compare()
