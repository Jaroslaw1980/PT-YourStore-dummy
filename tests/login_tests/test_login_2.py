from pages.main_page import MainPage
from pages.login_page import LoginPage
from pytest import mark


@mark.regression
@mark.smoke
@mark.login
@mark.usefixtures("setup")
class LoginNegativeTests:

    def test_go_to_page(self):
        page = LoginPage(self.driver)
        page.go_to_page()

    @mark.parametrize('emails', ["a", "Yaro", "Baro", "YaroBaro.com", "@", " "])
    def test_email_inputs(self, emails):
        login = LoginPage(self.driver)
        login.input_email(emails)
        login.click_submit()
        assert login.wrong_login_popup_text().is_displayed(), 'No popup about wrong credentials'

    @mark.parametrize('logins', ["B", "Baro", "BaroYaro", " ", "@"])
    def test_login_inputs(self, logins):
        login = LoginPage(self.driver)
        login.input_password(logins)
        login.click_submit()
        assert login.wrong_login_popup_text().is_displayed(), 'No popup about wrong credentials'

