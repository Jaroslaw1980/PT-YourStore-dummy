from pages.product_returns_page import ProductReturnsPage
from pytest import mark


@mark.smoke
@mark.usefixtures("setup")
class ProductsReturnsTests:

    def test_product_returns(self):
        page = ProductReturnsPage(self.driver)
        page.go_to_page()

        page.add_firstname("Yaro")
        page.add_lastname("Baro")
        page.add_email("YaroBaro@gmail.com")
        page.add_telephone("123567890")
        page.add_order_id("1478")
        page.add_order_date("2022-04-30")
        page.add_product_name("iPhone")
        page.add_product_code("557738383")
        page.add_quantity("1")
        page.add_reason_for_return(4)
        page.check_if_product_was_opened(0)
        page.add_details("Bardzo niedobry telefon")
        page.click_submit_button()
