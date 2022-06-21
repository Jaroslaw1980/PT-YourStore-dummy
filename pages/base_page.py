

class BasePage(object):

    base_url = None

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(self.base_url)

