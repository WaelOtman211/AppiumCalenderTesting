import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy



class calendarPage():
    PENDING_EVENT = "com.claudivan.taskagenda:id/btEventosMes"

    def __init__(self, driver):
        self.driver = driver
        self.init_elements()

    def init_elements(self):
        time.sleep(1)
        self.pending_event = self.driver.find_element(by=AppiumBy.ID, value=self.PENDING_EVENT)



