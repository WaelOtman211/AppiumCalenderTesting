
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options
from config_reader import *

class deviceWrapper():

    def __init__(self):
        capabilities = get_config_data()

        appium_server_url = 'http://localhost:4723'

        # Converts capabilities to AppiumOptions instance
        capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=capabilities_options
        )

    def get_driver(self):
        return self.driver