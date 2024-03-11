import selenium
from selenium import webdriver
from appium import webdriver

from infra.base_page import BasePage


class BrowserWrapper(BasePage):
    def __init__(self):
        super().__init__(self.get_driver())
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.claudivan.taskagenda',
            'appActivity': '.Activities.MainActivity',
            'automationName': 'UiAutomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def get_driver(self):
        return self.driver
