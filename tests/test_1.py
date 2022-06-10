from pages.mainPage import MainPage
from utilities.BaseClass import BaseClass
from parameterized import parameterized
from pytest import mark


@mark.login
class TestOne(BaseClass): # testing footer links

    @parameterized.expand([
        "About Us",
        "Delivery Information",
        "Privacy Policy",
        "Terms & Conditions"])
    def test_links(self, link):
        home = MainPage(self.driver)
        home.link_checker(link)












