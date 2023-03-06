from pytest import fixture
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@fixture(scope='session')
def auto_login(self):
    login = LoginPage(self.driver)
    login.go_to_page()
    login.enter_email("YaroBaro@gmail.com")
    login.enter_password("YaroBaro")
    login.click_submit()

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser to run tests")

@fixture(scope='class')
def setup(request):
    driver = webdriver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()



