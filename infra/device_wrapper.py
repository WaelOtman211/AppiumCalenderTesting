import selenium
from selenium import webdriver
from appium import webdriver
from infra.base_page import BasePage
from infra.config_reader import get_config_data


class BrowserWrapper(BasePage):
    def __init__(self):
        super().__init__(self.get_driver())
        desired_caps = get_config_data()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def get_driver(self):
        return self.driver
