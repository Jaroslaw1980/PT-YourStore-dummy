from pytest import mark
from pages.register_account_page import RegisterAccount


@mark.usefixtures("setup")
class RegisterPossitiveTests:

    def test_go_to_page(self):
        page = RegisterAccount(self.driver)
        page.go_to_page()

    def test_registration_form(self):
        register = RegisterAccount(self.driver)
        register.input_firstname("Yaro")
        register.input_lastname("Baro")
        register.input_email("YaroBaro@gmail.com")
        register.input_telephone('345345345')
        register.input_password("YaroBaro")
        register.confirm_password("YaroBaro")
        register.click_checkbox()
        assert register.checkbox().is_selected(), 'Checkbox is not selected'



