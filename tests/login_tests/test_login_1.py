from pages.login_page import LoginPage
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
        login.enter_email("YaroBaro@gmail.com")
        login.enter_password("YaroBaro")
        login.click_submit()


