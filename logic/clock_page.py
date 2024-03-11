import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy


class clockPage():
    OK_BUTTON = "android:id/button1"
    CANCEL_BUTTON = "android:id/button2"

    def __init__(self, driver):
        self.driver = driver
        self.init_elements()

    def init_elements(self):
        time.sleep(1)
        self.ok_button = self.driver.find_element(by=AppiumBy.ID, value=self.OK_BUTTON)
        self.cancel_button = self.driver.find_element(by=AppiumBy.ID, value=self.CANCEL_BUTTON)

    def click_ok_button(self):
        self.ok_button.click()

    def click_cancel_button(self):
        self.cancel_button.click()

    def fill_time(self, hour, minutes):
        self.time_hours = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value=f"//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='{hour}']").click()
        time.sleep(1)
        self.time_minute = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value=f"//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='{minutes}']").click()
        self.click_ok_button()
