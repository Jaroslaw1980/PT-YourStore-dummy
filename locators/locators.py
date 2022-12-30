### Container class for all pages locators values ###

class ProductListPageLocators:

    sort_by_list_ID = 'list-view'
    sort_by_grid_ID = 'grid-view'
    sort_by_text_ID = 'input-sort'
    how_many_on_page_ID = 'input-limit'


class LoginPageLocators:

    input_email_ID = "input-email"
    input_password_ID = "input-password"
    submit_button_XPATH = "//input[@type='submit']"
    popup_text_XPATH = "//*[text()=' Warning: No match for E-Mail Address and/or Password.']"


class ShoppingCartLocators:

    number_of_items_XPATH = "//input[contains(@name, 'quantity')]"
    submit_items_change_XPATH = "//button[@data-original-title='Update']"
    remove_from_cart_XPATH = "//button[@data-original-title='Remove']"
    use_coupon_XPATH = "//*[text()='Use Coupon Code ']"
    input_coupon_code_ID = "input-coupon"
    submit_coupon_CSS_SELECTOR = "input[type='button']"
    click_checkout_LINK_TEXT = "Checkout"
    product_list_cart_XPATH = "//table/tbody/tr/td[6]"
    cart_total_value_XPATH = "//table[@class='table table-bordered']/tbody/tr[4]/td[2])[2]"


class RegisterAccountLocators:

    input_firstname_ID = "input-firstname"
    error_popup_firstname_XPATH = "(//div[@class='text-danger'])[1]"
    input_lastname_ID = "input-lastname"
    error_popup_lastname_XPATH = "(//div[@class='text-danger'])[2]"
    input_email_ID = "input-email"
    error_popup_email_XPATH = "(//div[@class='text-danger'])[3]"
    input_telephone_ID = "input-telephone"
    error_popup_telephone_XPATH = "(//div[@class='text-danger'])[4]"
    input_password_ID = "input-password"
    error_popup_password_XPATH = "(//div[@class='text-danger'])[5]"
    confirm_password_ID = "input-confirm"
    error_popup_confirm_password_XPATH = "//div[text()='Password confirmation does not match password!']"
    click_checkbox_XPATH = "//input[@type='checkbox']"
    error_popup_checkbox_XPATH = "//div[text()=' Warning: You must agree to the Privacy Policy!']"
    click_submit_XPATH = "//input[@type='submit']"


class ProductDetailPageLocators:

    set_product_quantity_ID = 'input-quantity'
    click_reviews_XPATH = "//a[contains(text(), 'Reviews')]"
    click_description_XPATH = "//a[text()='Description']"
    click_image_XPATH = "//div[@class='col-sm-8']/ul/li/a"
    click_arrow_right_XPATH = "//button[@title='Next (Right arrow key)']"
    click_arrow_left_XPATH = "//button[@title='Previous (Left arrow key)']"
    close_preview_XPATH = "//button[@title='Close (Esc)']"
    add_to_cart_XPATH = "(//*[text()='Add to Cart'])[1]"


class MainPageLocators:

    choose_currency_XPATH = "//span[text()='Currency']"
    dropdown_elements_XPATH = "//ul[@class='dropdown-menu']/li/button"
    click_currency_CSS_SELECTOR = "button[class='btn btn-link dropdown-toggle']"
    choose_currency_EUR_CSS_SELECTOR = "button[name='EUR']"
    choose_currency_GBP_CSS_SELECTOR = "button[name='GBP']"
    choose_currency_USD_CSS_SELECTOR = "button[name='USD']"
    your_store_button_LINK_TEXT = "Your ClothStore"
    click_cart_ID = "cart"
    searching_NAME = "search"
    click_search_button_CSS_SELECTOR = "button[class='btn btn-default btn-lg']"
    click_my_account_CSS_SELECTOR = "a[title='My Account']"
    click_register_XPATH = "//a[text()='Register']"
    click_login_XPATH = "//a[text()='Login']"
    click_wish_list_ID = "wishlist-total"
    click_shopping_cart_CSS_SELECTOR = "a[title='Shopping Cart']"
    click_checkout_CSS_SELECTOR = "a[title='Checkout']"
    mouse_over_bar_LINK_TEXT = 'Components'
    click_logout_XPATH = "(//a[text()='Logout'])[1]"
    click_continue_after_logout_XPATH = "//a[text()='Continue']"
    add_to_cart_button_XPATH = "//span[text()='Add to Cart']"


class ContantUSLocators:

    input_name_ID = "input-name"
    error_add_name_XPATH = "//div[text()='Name must be between 3 and 32 characters!']"
    input_email_ID = "input-email"
    error_add_email_XPATH = "//div[text()='E-Mail Address does not appear to be valid!']"
    input_enquiry_ID = "input-enquiry"
    error_add_enquiry_XPATH = "//div[text()='Enquiry must be between 10 and 3000 characters!']"
    click_submit_CSS = "input[type='submit']"


class ProductReturnsPageLocators:

    add_firstname_ID = "input-firstname"
    error_add_firstname_XPATH = "//div[text()='First Name must be between 1 and 32 characters!']"
    add_lastname_ID = "input-lastname"
    error_add_lastname_XPATH = "//div[text()='Last Name must be between 1 and 32 characters!']"
    add_email_ID = "input-email"
    add_error_email_XPATH = "//div[text()='E-Mail Address does not appear to be valid!']"
    add_telephone_ID = "input-telephone"
    error_add_telephone_XPATH = "//div[text()='Telephone must be between 3 and 32 characters!']"
    add_order_id_ID = "input-order-id"
    error_order_id_XPATH = "//div[text()='Order ID required!']"
    add_order_date_ID = "input-date-ordered"
    add_product_name_ID = "input-product"
    error_add_product_name_XPATH = "//div[text()='Product Name must be greater than 3 and less than 255 characters!']"
    add_product_code_ID = "input-model"
    error_product_code_XPATH = "//div[text()='Product Model must be greater than 3 and less than 64 characters!']"
    add_quantity_ID = "input-quantity"
    add_reason_for_return_XPATH = "//div[@class='col-sm-10']/div[@class='radio']"
    error_reason_for_reutrn_XPATH = "//div[text()='You must select a return product reason!']"
    check_if_product_was_opened_XPATH = "//div[@class='col-sm-10']/label[@class='radio-inline']"
    add_details_ID = "input-comment"
    click_back_button_LINK_TEXT = "Back"
    click_submit_button_CSS_SELECTOR = "input[type=submit]"







