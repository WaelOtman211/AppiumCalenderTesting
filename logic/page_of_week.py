import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from logic.page_of_new_event import NewEventPage


class WeekPage():
    ADD_EVENT= "com.claudivan.taskagenda:id/btNovoEvento"
    CALENDER_BUTTON = "//android.widget.TextView[@text='Calendar']"
    PENDING_EVENT = "com.claudivan.taskagenda:id/btEventosSemana"

    def __init__(self,driver):
        self.driver=driver
        self.init_elements()

    def init_elements(self):
        time.sleep(1)
        self.add_event_button = self.driver.find_element(by=AppiumBy.ID, value=self.ADD_EVENT)
        self.calendar_button = self.driver.find_element(by=AppiumBy.XPATH, value=self.CALENDER_BUTTON)
        time.sleep(1)


    def click_add_event_button(self):
        self.add_event_button.click()

    def click_calendar_button(self):
        self.calendar_button.click()

    def choose_add_event_day_element(self,text):
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.XPATH, value=f"//android.widget.TextView[@resource-id='android:id/text1' and @text='{text}']").click()

    def init_pending_event(self):
        self.pending_event=self.driver.find_element(by=AppiumBy.ID, value=self.PENDING_EVENT)





