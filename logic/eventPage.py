from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from infra.base_page import BasePage


class EventPage(BasePage):
    FILL_EVENT_NAME = 'com.claudivan.taskagenda:id/btEventosSemana'
    SAVE = 'com.claudivan.taskagenda:id/hamburguer'
    CREATE_EVENT = '//android.widget.Button[@content-desc="Create Event"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.fill_event_name = self._driver.find_element(by=AppiumBy.ID, value=self.FILL_EVENT_NAME)
        self.save = self._driver.find_element(by=AppiumBy.ID, value=self.SAVE)

    def fill_event_name(self, text):
        self.fill_event_name(text)

    def save(self):
        self.save.click()