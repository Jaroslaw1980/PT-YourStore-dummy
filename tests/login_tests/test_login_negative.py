from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from pytest import mark


@mark.regression
@mark.smoke
@mark.login
@mark.usefixtures("setup")
class LoginNegativeTests:

    def test_myaccount_button(self):
        main = MainPage(self.driver)
        main.click_my_account()
        main.click_login()

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

