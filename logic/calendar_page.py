import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from Logic.events_page import eventsPage


class calendarPage():
    PENDING_EVENT = "com.claudivan.taskagenda:id/btEventosMes"

    def __init__(self, driver):
        self.driver = driver
        self.init_elements()

    def init_elements(self):
        time.sleep(1)
        self.pending_event = self.driver.find_element(by=AppiumBy.ID, value=self.PENDING_EVENT)


    def go_to_events_list(self):
        self.pending_event.click()
        self.events_page = eventsPage(self.driver)
        return self.events_page

