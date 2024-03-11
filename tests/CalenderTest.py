import time
import unittest

from infra.device_wrapper import DeviceWrapper
from logic.page_of_new_event import NewEventPage
from utils import *
from logic.page_of_week import WeekPage


class NewEventTest(unittest.TestCase):

    def setUp(self):
        self.wrapper = DeviceWrapper()
        self.driver = self.wrapper.get_driver()
        time.sleep(2)
        self.week_page = WeekPage(self.driver)

    def test_event_date_today(self):
        self.add_event_and_assert_date('Today', get_today_calendar_date())

    def test_event_date_tomorrow(self):
        self.add_event_and_assert_date('Tomorrow', get_tomorrow_calendar_date())

    def test_time_selection(self):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element('Today')
        self.event_page = NewEventPage(self.driver)
        hours, minutes = 7, 50
        self.event_page.choose_time(hours, minutes)
        time_display_hours, time_display_minutes = map(int, self.event_page.get_time_field_text().split("h"))
        self.assertEqual(hours, time_display_hours)
        self.assertEqual(minutes, time_display_minutes)

    def add_event_and_assert_date(self, day_name, expected_date):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element(day_name)
        self.event_page = NewEventPage(self.driver)
        calender_date = self.event_page.get_date_field_text()
        self.assertEqual(calender_date, expected_date)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

