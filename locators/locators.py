class ProductListPageLocators:

    sort_by_list_pLp_ID = 'list-view'
    sort_by_grid_pLp_ID = 'grid-view'
    sort_by_text_pLp_ID = 'input-sort'
    how_many_on_page_pLp_ID = 'input-limit'


class LoginPageLocators:

    input_email_logPg_ID = "input-email"
    input_password_logPg_ID = "input-password"
    submit_button_logPg_XPATH = "//input[@type='submit']"
    popup_text_logPg_XPATH = "//*[text()=' Warning: No match for E-Mail Address and/or Password.']"


class ShoppingCartLocators:

    number_of_items_shpCrt_XPATH = "//input[contains(@name, 'quantity')]"
    submit_items_change_shpCrt_XPATH = "//button[@data-original-title='Update']"
    remove_from_cart_shpCrt_XPATH = "//button[@data-original-title='Remove']"
    use_coupon_shpCrt_XPATH = "//*[text()='Use Coupon Code ']"
    input_coupon_code_shpCrt_ID = "input-coupon"
    submit_coupon_shpCrt_CSS_SELECTOR = "input[type='button']"
    click_checkout_shpCrt_LINK_TEXT = "Checkout"
    product_list_cart_shpCrt_XPATH = "//table/tbody/tr/td[6]"
    cart_total_value_shpCrt_XPATH = "//table[@class='table table-bordered']/tbody/tr[4]/td[2])[2]"


class RegisterAccountLocators:

    input_firstname_RegAcc_ID = "input-firstname"
    error_popup_firstname_RegAcc_XPATH = "(//div[@class='text-danger'])[1]"
    input_lastname_RegAcc_ID = "input-lastname"
    error_popup_lastname_Regcc_XPATH = "(//div[@class='text-danger'])[2]"
    input_email_RegAcc_ID = "input-email"
    error_popup_email_RegAcc_XPATH = "(//div[@class='text-danger'])[3]"
    input_telephone_RegAcc_ID = "input-telephone"
    error_popup_telephone_RegAcc_XPATH = "(//div[@class='text-danger'])[4]"
    input_password_RegAcc_ID = "input-password"
    error_popup_password_RegAcc_XPATH = "(//div[@class='text-danger'])[5]"
    confirm_password_RegAcc_ID = "input-confirm"
    error_popup_confirm_password_RegAcc_XPATH = "//div[text()='Password confirmation does not match password!']"
    click_checkbox_RegAcc_XPATH = "//input[@type='checkbox']"
    error_popup_checkbox_RegAcc_XPATH = "//div[text()=' Warning: You must agree to the Privacy Policy!']"
    click_submit_RegAcc_XPATH = "//input[@type='submit']"


class ProductDetailPageLocators:

    set_product_quantity_pDp_ID = 'input-quantity'
    click_reviews_pDp_XPATH = "//a[contains(text(), 'Reviews')]"
    click_description_pDp_XPATH = "//a[text()='Description']"
    click_image_pDp_XPATH = "//div[@class='col-sm-8']/ul/li/a"
    click_arrow_right_pDp_XPATH = "//button[@title='Next (Right arrow key)']"
    click_arrow_left_pDp_XPATH = "//button[@title='Previous (Left arrow key)']"
    close_preview_pDp_XPATH = "//button[@title='Close (Esc)']"
    add_to_cart_pDp_XPATH = "(//*[text()='Add to Cart'])[1]"


class MainPageLocators:

    choose_currency_mainPg_XPATH = "//span[text()='Currency']"
    dropdown_elements_mainPg_XPATH = "//ul[@class='dropdown-menu']/li/button"
    click_currency_mainPg_CSS_SELECTOR = "button[class='btn btn-link dropdown-toggle']"
    choose_currency_mainPg_EUR_CSS_SELECTOR = "button[name='EUR']"
    choose_currency_mainPg_GBP_CSS_SELECTOR = "button[name='GBP']"
    choose_currency_mainPg_USD_CSS_SELECTOR = "button[name='USD']"
    your_store_button_mainPg_LINK_TEXT = "Your ClothStore"
    click_cart_mainPg_ID = "cart"
    searching_mainPg_NAME = "search"
    click_search_button_mainPg_CSS_SELECTOR = "button[class='btn btn-default btn-lg']"
    click_my_account_mainPg_CSS_SELECTOR = "a[title='My Account']"
    click_register_mainPg_XPATH = "//a[text()='Register']"
    click_login_mainPg_XPATH = "//a[text()='Login']"
    click_wish_list_mainPg_ID = "wishlist-total"
    click_shopping_cart_mainPg_CSS = "a[title='Shopping Cart']"
    click_checkout_mainPg_CSS = "a[title='Checkout']"
    mouse_over_bar_mainPg_LINK_TEXT = 'Components'
    click_logout_mainPg_XPATH = "(//a[text()='Logout'])[1]"
    click_continue_after_logout_mainPg_XPATH = "//a[text()='Continue']"
    add_to_cart_button_mainPG_XPATH = "//span[text()='Add to Cart']"


