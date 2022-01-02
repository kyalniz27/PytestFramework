from selenium import webdriver
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import utilClass as util

@pytest.mark.usefixtures("setUp")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(util.url)
        login = LoginPage(driver)
        login.enter_username(util.username)
        login.enter_password(util.password)
        login.click_login()
        title = driver.title
        assert title == "OrangeHRM"

    def test_logout(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.click_welcome()
        homePage.click_logout()
        title = driver.title
        assert title == "OrangeHRM"








