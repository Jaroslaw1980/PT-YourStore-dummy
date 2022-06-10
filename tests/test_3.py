import pytest
from testData.registerAccountData import RegisterAccountData
from pages.mainPage import MainPage
from utilities.BaseClass import BaseClass


class TestThree(BaseClass):

    @pytest.fixture(params=RegisterAccountData.test_registeraccount_data)
    def getdata(self, request):
        return request.param

    def test_registration(self, getdata):

        log = self.getLogger()

        home = MainPage(self.driver)
        home.click_my_account()

        registerpage = home.click_register()
        registerpage.input_firstname(getdata["firstname"])
        log.info("Firstname = " + getdata["firstname"])
        registerpage.input_lastname(getdata["lastname"])
        log.info("Lastname = " + getdata["lastname"])

        self.driver.refresh() # przeładuj stronę



