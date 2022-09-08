from pages.register_account_page import RegisterAccount
from pytest import mark
from test_data.test_register_2_data import TestRegister2Data


# TODO: write comments


@mark.usefixtures("setup")
class RegisterNegativeTests:

    def test_go_to_page(self):
        page = RegisterAccount(self.driver)
        page.go_to_page()

    def test_checkbox(self):
        register = RegisterAccount(self.driver)
        register.click_submit()
        assert register.get_error_popup_checkbox().is_displayed(), 'No error message'

    @mark.parametrize("confirm", TestRegister2Data.confirm_password)
    def test_registration_confirm_password(self, confirm):
        register = RegisterAccount(self.driver)
        register.enter_password('password')
        register.enter_confirm_password(confirm)
        register.click_checkbox()
        register.click_submit()
        assert register.get_error_popup_confirm_password().is_displayed(), 'No popup error'

    @mark.parametrize("firstname", TestRegister2Data.register_first_name)
    def test_registration_firstname(self, firstname):
        register = RegisterAccount(self.driver)
        register.enter_firstname(firstname)
        register.click_checkbox()
        register.click_submit()
        assert register.get_error_popup_firstname().is_displayed(), 'No error popup'

    @mark.parametrize("lastname", TestRegister2Data.register_last_name)
    def test_registration_lastname(self, lastname):
        register = RegisterAccount(self.driver)
        register.enter_lastname(lastname)
        register.click_checkbox()
        register.click_submit()
        assert register.get_error_popup_lastname().is_displayed(), 'No error popup'

    @mark.parametrize("email", TestRegister2Data.register_email)
    def test_registration_email(self, email):
        register = RegisterAccount(self.driver)
        register.enter_email(email)
        register.click_checkbox()
        register.click_submit()
        assert register.get_error_popup_email().is_displayed(), 'No error popup'

    @mark.parametrize("telephone", TestRegister2Data.register_telephone)
    def test_registration_telephone(self, telephone):
        register = RegisterAccount(self.driver)
        register.enter_telephone(telephone)
        register.click_checkbox()
        register.click_submit()
        assert register.get_error_popup_telephone().is_displayed(), 'No popup error'

    @mark.parametrize("password", TestRegister2Data.register_password)
    def test_registration_password(self, password):
        register = RegisterAccount(self.driver)
        register.enter_password(password)
        register.click_checkbox()
        register.click_submit()
        assert register.get_error_popup_password().is_displayed(), 'No popup error'
