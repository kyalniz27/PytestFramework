import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action = "store", default="chrome", help="Type in browser name e.g chrome OR firefox")


@pytest.fixture(scope="class")
def setUp(request):

    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C://Users//seker//PycharmProjects//PytestFramework//drivers//chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C://Users//seker//PycharmProjects//PytestFramework//drivers//geckodriver.exe")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()