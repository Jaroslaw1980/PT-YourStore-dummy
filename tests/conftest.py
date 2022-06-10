from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@fixture(scope="class")
def setup(request):
    s = Service('C:/Selenium - drivers/Chrome/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get('http://tutorialsninja.com/demo/index.php?route=common/home')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()



#def pytest_addoption(parser):
#    parser.addoption("--browser_name", action="store", default="chrome")

#@pytest.fixture(scope="class")
#def setup(request):
 #   browser_name = request.config.getoption("browser_name")
 #   if browser_name == "chrome":
 #       s = Service('C:/Selenium - dev/Drivers/chromedriver.exe')
 #       driver = webdriver.Chrome(service=s)
 #   elif browser_name == "firefox":
 #       s = Service('C:/Selenium - dev/Drivers/geckodriver.exe')
 #       driver = webdriver.Firefox(service=s)

   # driver.get('http://tutorialsninja.com/demo/index.php?route=common/home')
   # driver.maximize_window()
   # request.cls.driver = driver
   # yield
   # driver.close()
   # driver.quit()






