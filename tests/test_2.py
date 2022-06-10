import pytest
from testData.loginData import LoginData
from pages.mainPage import MainPage
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass): # testing loggin happy path

    @pytest.fixture(params=LoginData.test_login_data)
    def getdata(self, request):
        return request.param

    def test_login(self, getdata):

        log = self.getLogger()

        home = MainPage(self.driver)
        home.click_my_account()
        loginpage = home.click_login()

        loginpage.input_email(getdata['email'])
        log.info("e-mail = " + getdata['email'])
        loginpage.input_password(getdata['password'])
        log.info("password = " + getdata['password'])
        loginpage.click_submit()


