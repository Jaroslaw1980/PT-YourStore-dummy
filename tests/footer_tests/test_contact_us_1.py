from pages.contant_us_page import ContactUsPage
from pytest import mark


@mark.usefixtures("setup")
class ContactUsTests:

    def test_contact_us(self):
        page = ContactUsPage(self.driver)
        page.go_to_page()

        page.enter_name("Yaro")
        page.enter_email("YaroBaro@gmail.com")
        page.enter_enquiry("Tu się coś napisze będzie dobrze.")
        page.click_submit()
