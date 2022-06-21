from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from pytest import mark


@mark.regression
@mark.smoke
@mark.login
@mark.usefixtures("setup")
class LoginPossitiveTests:

    def test_go_to_page(self):
        page = LoginPage(self.driver)
        page.go_to_page()

    def test_login(self):
        login = LoginPage(self.driver)
        login.input_email("YaroBaro@gmail.com")
        login.input_password("YaroBaro")
        login.click_submit()


