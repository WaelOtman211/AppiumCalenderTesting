from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from infra.base_page import BasePage


class CalendarPage(BasePage):
    SHOW_PENDING_EVENT = 'com.claudivan.taskagenda:id/btEventosSemana'
    MENU = 'com.claudivan.taskagenda:id/hamburguer'
    CREATE_EVENT = '//android.widget.Button[@content-desc="Create Event"]'
    LIFT = '(//android.widget.ImageView[@content-desc="Image"])[1]'
    RIGHT = '(//android.widget.ImageView[@content-desc="Image"])[2]'
    CALENDER = '//android.widget.TextView[@text="Calendar"]'
    WEEK = '//android.widget.TextView[@text="Week"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.show_pending_event = self._driver.find_element(by=AppiumBy.ID, vslue=self.SHOW_PENDING_EVENT)
        self.menu = self._driver.find_element(by=AppiumBy.ID, vslue=self.menu)
        self.create_event = self._driver.find_element(by=AppiumBy.XPATH,vslue= self.CREATE_EVENT)
        self.right = self._driver.find_element(by=AppiumBy.XPATH,vslue= self.RIGHT)
        self.lift = self._driver.find_element(by=AppiumBy.XPATH, vslue=self.LIFT)
        self.calender = self._driver.find_element(by=AppiumBy.XPATH, vslue=self.CALENDER)
        self.week = self._driver.find_element(by=AppiumBy.XPATH,vslue= self.WEEK)

    def show_event(self):
        self.show_pending_event().click()

    def menu(self):
        self.menu().click()

    def create_event(self, event_title):
        self.create_event.click()

    def press_right(self):
        self.right.click()

    def press_lift(self):
        self.lift.click()

    def press_lift_and_right(self):
        self.press_lift()
        self.press_right()

    def press_week(self):
        self.week.click()

    def press_calender(self):
        self.calender.click()

    def press_calender_week(self):
        self.press_calender()
        self.press_week()
        self.press_calender()
        self.press_week()