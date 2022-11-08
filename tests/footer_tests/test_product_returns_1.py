from pages.product_returns_page import ProductReturnsPage
from pytest import mark


@mark.footerTests
@mark.smoke
@mark.usefixtures("setup")
class ProductsReturnsTests:

    def test_product_returns(self):
        page = ProductReturnsPage(self.driver)
        page.go_to_page()

        page.enter_firstname("Yaro")
        page.enter_lastname("Baro")
        page.enter_email("YaroBaro@gmail.com")
        page.enter_telephone("123567890")
        page.enter_order_id("1478")
        page.enter_order_date("2022-04-30")
        page.enter_product_name("iPhone")
        page.enter_product_code("557738383")
        page.enter_quantity("1")
        page.enter_reason_for_return(4)
        page.check_product_opened(0)
        page.enter_details("Bardzo niedobry telefon")
        page.click_submit_button()
