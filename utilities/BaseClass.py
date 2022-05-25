import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler = logging.FileHandler("C:/Python/Selenium/MyStore/utilities/logfile.log")
        logger.addHandler(filehandler)
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifiy_links(self, link):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link)))







