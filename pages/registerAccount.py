from Selenium.PTYourStore.locators.locators import Locators
from selenium.webdriver.common.by import By

class RegisterAccount:
    def __init__(self, driver):
        self.driver = driver


        self.input_firstname_RegAcc_ID = Locators.input_firstname_RegAcc_ID
        self.input_lastname_RegAcc_ID = Locators.input_lastname_RegAcc_ID
        self.input_email_RegAcc_ID = Locators.input_email_RegAcc_ID
        self.input_telephone_RegAcc_ID = Locators.input_telephone_RegAcc_ID
        self.input_password_RegAcc_ID = Locators.input_password_RegAcc_ID
        self.confirm_password_RegAcc_ID = Locators.confirm_password_RegAcc_ID
        self.click_checkbox_RegAcc_XPATH = Locators.click_checkbox_RegAcc_XPATH
        self.click_submit_RegAcc_XPATH = Locators.click_submit_RegAcc_XPATH

    def input_firstname(self, firstname):
        self.driver.find_element(By.ID, self.input_firstname_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_firstname_RegAcc_ID).send_keys(firstname)

    def input_lastname(self, lastname):
        self.driver.find_element(By.ID, self.input_lastname_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_lastname_RegAcc_ID).send_keys(lastname)

    def input_email(self, email):
        self.driver.find_element(By.ID, self.input_email_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_email_RegAcc_ID).send_keys(email)

    def input_telephone(self, telephone):
        self.driver.find_element(By.ID, self.input_telephone_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_telephone_RegAcc_ID).send_keys(telephone)

    def input_password(self, password):
        self.driver.find_element(By.ID, self.input_password_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.input_password_RegAcc_ID).send_keys(password)

    def confirm_password(self, confirm):
        self.driver.find_element(By.ID, self.confirm_password_RegAcc_ID).clear()
        self.driver.find_element(By.ID, self.confirm_password_RegAcc_ID).send_keys(confirm)

    def click_checkbox(self):
        self.driver.find_element(By.XPATH, self.click_checkbox_RegAcc_XPATH).click()

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.click_submit_RegAcc_XPATH).click()

