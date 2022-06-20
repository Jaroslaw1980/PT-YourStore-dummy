from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from pytest import mark


@mark.regression
@mark.smoke
@mark.login
@mark.usefixtures("setup")
class LoginPossitiveTests:

    def test_myaccount_button(self):
        main = MainPage(self.driver)
        main.click_my_account()
        main.click_login()

    def test_login(self):
        login = LoginPage(self.driver)
        login.input_email("YaroBaro@gmail.com")
        login.input_password("YaroBaro")
        login.click_submit()


