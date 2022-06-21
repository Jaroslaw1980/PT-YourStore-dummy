from pages.contant_us_page import ContactUsPage
from pytest import mark
import time


@mark.usefixtures("setup")
class ContactUsTests:

    def test_contact_us(self):
        page = ContactUsPage(self.driver)
        page.go_to_page()

        page.add_name("Yaro")
        page.add_email("YaroBaro@gmail.com")
        page.add_enquiry("Tu się coś napisze będzie dobrze.")
        page.click_submit()

