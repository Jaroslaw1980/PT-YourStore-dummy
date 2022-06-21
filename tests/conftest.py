from pytest import fixture
from selenium import webdriver


@fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()




# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action="store", default="chrome", help="Browser to run tests")


# @fixture(scope='session')
# def browser_setup(request):
#     browser_name = request.config.getoption("--browser_name")
#     if browser_name == "chrome":
#         s = Service('C:/Selenium - drivers/Chrome/chromedriver.exe')
#         driver = webdriver.Chrome(service=s)
#     elif browser_name == "firefox":
#         s = Service('C:/Selenium - drivers/Firefox/geckodriver.exe')
#         driver = webdriver.Firefox(service=s)
#     driver.get('http://tutorialsninja.com/demo/index.php?route=common/home')
#     driver.maximize_window()
#     request.driver = driver
#     yield
#     driver.close()
#     driver.quit()




