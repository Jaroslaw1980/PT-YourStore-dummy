from base.selenium_driver import SeleniumDriver


class BasePage(SeleniumDriver):

    base_url = None

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver

    def go_to_page(self):
        self.driver.get(self.base_url)

