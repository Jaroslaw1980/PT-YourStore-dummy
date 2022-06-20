from pytest import mark
from pages.mainPage import MainPage
from pages.registerAccount import RegisterAccount


@mark.usefixtures("setup")
class RegisterNegativeTests:

    def test_registration_path(self):
        main = MainPage(self.driver)
        main.click_my_account()
        main.click_register()

    def test_checkbox(self):
        register = RegisterAccount(self.driver)
        register.click_submit()
        assert register.error_popup_checkbox().is_displayed(), 'No error message'

    @mark.parametrize("confirm", ["", " ", "0", "a", "passwor", "passworda"])
    def test_registration_confirm_password(self, confirm):
        register = RegisterAccount(self.driver)
        register.input_password('password')
        register.confirm_password(confirm)
        register.click_checkbox()
        register.click_submit()
        assert register.error_popup_confirm_password().is_displayed(), 'No popup error'

    @mark.parametrize("firstname", ["", " ", "Name", "ajsndkfiemcjtugjfheowlqpdlvmxnze4"])
    def test_registration_firstname(self, firstname):
        register = RegisterAccount(self.driver)
        register.input_firstname(firstname)
        register.click_checkbox()
        register.click_submit()
        assert register.error_popup_firstname().is_displayed(), 'No error popup'

    @mark.parametrize("lastname", ["", " ", "ajsndkfiemcjtugjfheowlqpdlvmxnze4"])
    def test_registration_lastname(self, lastname):
        register = RegisterAccount(self.driver)
        register.input_lastname(lastname)
        register.click_checkbox()
        register.click_submit()
        assert register.error_popup_lastname().is_displayed(), 'No error popup'

    @mark.parametrize("email", ["", " ", "ajsndkfiemcjtugjfheowlqpdlvmxnze4"])
    def test_registration_email(self, email):
        register = RegisterAccount(self.driver)
        register.input_email(email)
        register.click_checkbox()
        register.click_submit()
        assert register.error_popup_email().is_displayed(), 'No error popup'

    @mark.parametrize("telephone", ["", " ", "0", "1", "12", "123456789098765432123456789098765"])
    def test_registration_telephone(self, telephone):
        register = RegisterAccount(self.driver)
        register.input_telephone(telephone)
        register.click_checkbox()
        register.click_submit()
        assert register.error_popup_telephone().is_displayed(), 'No popup error'

    @mark.parametrize("password", ["", " ", "0", "a", "ab", "abc", "mbnfjdksoejdkfirytjgo"])
    def test_registration_password(self, password):
        register = RegisterAccount(self.driver)
        register.input_password(password)
        register.click_checkbox()
        register.click_submit()
        assert register.error_popup_password().is_displayed(), 'No popup error'




