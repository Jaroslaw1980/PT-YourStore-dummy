from pages.login_page import LoginPage
from pytest import mark
from test_data.test_login_2_data import TestLogin2Data


@mark.regression
@mark.smoke
@mark.login
@mark.usefixtures("setup")
class LoginNegativeTests:

    def test_go_to_page(self):
        page = LoginPage(self.driver)
        page.go_to_page()

    @mark.parametrize('emails', TestLogin2Data.emails)
    def test_email_inputs(self, emails):
        login = LoginPage(self.driver)
        login.enter_email(emails)
        login.click_submit()
        assert login.get_wrong_login_popup_text().is_displayed(), 'No popup with wrong credentials'

    @mark.parametrize('logins', TestLogin2Data.logins)
    def test_login_inputs(self, logins):
        login = LoginPage(self.driver)
        login.enter_password(logins)
        login.click_submit()
        assert login.get_wrong_login_popup_text().is_displayed(), 'No popup with wrong credentials'

