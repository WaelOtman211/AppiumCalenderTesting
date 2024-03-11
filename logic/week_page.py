import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from Logic.calendar_page import calendarPage
from Logic.events_page import eventsPage
from Logic.new_event_page import newEventPage


class weekPage():
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



    def click_add_event_button(self):
        self.add_event_button.click()

    def click_calendar_button(self):
        self.calendar_button.click()

    def choose_add_event_day_element(self,text):
        #text should be either "Today", "Tomorrow", "Other"
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.XPATH, value=f"//android.widget.TextView[@resource-id='android:id/text1' and @text='{text}']").click()


    def add_new_event(self,event_name,hour,minute,type,description):
        self.event_page = newEventPage(self.driver)
        self.event_page.create_event(event_name,hour,minute,type,description)



    def go_to_calender_page(self):
        self.calendar_button.click()

        self.calendar_page = calendarPage(self.driver)
        return self.calendar_page
    def init_pending_event(self):
        self.pending_event=self.driver.find_element(by=AppiumBy.ID, value=self.PENDING_EVENT)


    def go_to_pending_events_list(self):
        self.init_pending_event()
        self.pending_event.click()
        self.events_list_page = eventsPage(self.driver)
        return self.events_list_page



