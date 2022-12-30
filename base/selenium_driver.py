### Selenium driver class with methods used commonly with selenium
# webdriver ###

from selenium.webdriver.common.by import By
import utilities.logger as log


class SeleniumDriver:
    log = log.logger()

    def __init__(self, driver):
        self.driver = driver

    ### Method used to check locator type
    # returns By.locator type ###
    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class_name":
            return By.CLASS_NAME
        elif locator_type == "link_text":
            return By.LINK_TEXT
        elif locator_type == "partial_link":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            raise TypeError("Bad locator type")

    ### Method used to find element on the page
    # Returns ready to use page element ###
    def get_element(self, locator, locator_type='id'):
        element = None
        locator_type = locator_type.lower()
        if locator:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f'Element found with "{locator_type}" locator type and "{locator}" locator')
        else:
            self.log.info(f'Element not found with "{locator_type}" locator type and "{locator}" locator')
        return element

    # Method used to find elements on the page
    def get_elements(self, locator, locator_type='id'):
        elements = None
        locator_type = locator_type.lower()
        if locator:
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info(f'Elements found with "{locator_type}" locator type and "{locator}" locator')
        else:
            self.log.info(f'Elements not found with "{locator_type}" locator type and "{locator}" locator')
        return elements

    # Method used to send keys to page element
    def send_keys_to_element(self, data, locator, locator_type='id', element=None):

        if locator:
            element = self.get_element(locator, locator_type)
            self.log.info(f'Element used to type with "{locator_type}" locator type and "{locator}" locator')
        else:
            self.log.info(f'Element not found with "{locator_type}" locator type and "{locator}" locator')
        element.clear()
        element.send_keys(data)

    # Method used to click element on the page
    def click_element(self, locator, locator_type='id', element=None):
        if locator:
            element = self.get_element(locator, locator_type)
            self.log.info(f'Element clicked with "{locator_type}" locator type and "{locator}" locator')
        else:
            self.log.info(f'Element not found with "{locator_type}" locator type and "{locator}" locator')
        element.click()

    # Method used to clear element content
    def clear_element(self, locator, locator_type='id', element=None):
        if locator:
            element = self.get_element(locator, locator_type)
            self.log.info(f'Element cleared with "{locator_type}" locator type and "{locator}" locator')
        else:
            self.log.info(f'Element not found with "{locator_type}" locator type and "{locator}" locator')
        element.clear()