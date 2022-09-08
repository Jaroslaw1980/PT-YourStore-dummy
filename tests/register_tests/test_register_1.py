from pytest import mark
from pages.register_account_page import RegisterAccount


@mark.usefixtures("setup")
class RegisterPossitiveTests:

    def test_go_to_page(self):
        page = RegisterAccount(self.driver)
        page.go_to_page()

    def test_registration_form(self):
        register = RegisterAccount(self.driver)
        register.enter_firstname("Yaro")
        register.enter_lastname("Baro")
        register.enter_email("YaroBaro@gmail.com")
        register.enter_telephone('345345345')
        register.enter_password("YaroBaro")
        register.enter_confirm_password("YaroBaro")
        register.click_checkbox()
        assert register.get_checkbox().is_selected(), 'Checkbox is not selected'



