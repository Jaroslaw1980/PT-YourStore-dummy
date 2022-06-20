from pytest import mark
from pages.mainPage import MainPage
from pages.registerAccount import RegisterAccount


@mark.usefixtures("setup")
class RegisterPossitiveTests:

    def test_registration_path(self):
        main = MainPage(self.driver)
        main.click_my_account()
        main.click_register()

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



