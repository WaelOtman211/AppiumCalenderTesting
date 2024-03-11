import time
import unittest
# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options
from infra import *
from infra.device_wrapper import deviceWrapper
from logic.new_event_page import newEventPage
from utils import *
from logic.week_page import weekPage


class newEventTest(unittest.TestCase):
    def setUp(self) -> None:
        self.wrapper = deviceWrapper()
        self.driver = self.wrapper.get_driver()
        time.sleep(2)
        self.week_page = weekPage(self.driver)

    def test_datetime_today_in_event_pag(self):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element('Today')
        self.event_page = newEventPage(self.driver)
        calender_date = self.event_page.get_date_field_text()
        date_today = get_today_date_in_calendar_format()
        self.assertEqual(calender_date,date_today)



    def test_datetime_tommorow_in_event_page(self):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element('Tomorrow')
        self.event_page = newEventPage(self.driver)
        calender_date = self.event_page.get_date_field_text()
        date_today = get_tomorrow_date_in_calendar_format()
        self.assertEqual(calender_date, date_today)

    def test_time_hours_minutes_selection(self):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element('Today')

        self.event_page = newEventPage(self.driver)
        hours=9
        minutes = 30
        self.event_page.choose_time(hours,minutes)
        time_field_display = self.event_page.get_time_field_text().split("h")
        time_display_hours = int(time_field_display[0])
        time_display_minutes = int(time_field_display[1])
        self.assertEqual(hours,time_display_hours)
        self.assertEqual(minutes,time_display_minutes)

    def test_add_event(self):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element('Tomorrow')
        event_name = 'lesson'
        hour = 9
        minute = 30
        event_type = 'task'
        event_description = 'appium lesson'
        self.week_page.add_new_event(event_name,hour,minute,event_type,event_description)
        self.events_page = self.week_page.go_to_pending_events_list()
        self.events_page.click_allow_notification()
        self.events_details = self.events_page.go_to_event_details_by_index(1)
        self.assertEqual(event_name,self.events_details.get_event_name())
        self.assertEqual(event_type,self.events_details.get_event_type().lower())
        self.assertEqual(hour,int(self.events_details.get_event_time()[0]))
        self.assertEqual(minute,int(self.events_details.get_event_time()[1]))
        self.assertEqual(event_description,self.events_details.get_event_description())





def tearDown(self) -> None:
    if self.driver:
        self.driver.quit()