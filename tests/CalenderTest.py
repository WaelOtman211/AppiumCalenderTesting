import unittest

from infra.device_wrapper import BrowserWrapper
from logic.calenderSourcePage import CalendarPage
from logic.eventPage import EventPage


class CalenderTest(unittest.TestCase):

    def test_menu_item(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.calendar_page = CalendarPage(self.driver)
        self.calendar_page.menu.click()

    def test_show_event_item(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.calendar_page = CalendarPage(self.driver)
        self.calendar_page.show_event()

    def test_calendar_swap(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.calendar_page = CalendarPage(self.driver)
        self.calendar_page.press_lift_and_right()

    def test_create_event(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.calendar_page = CalendarPage(self.driver)
        self.calendar_page.create_event()
        self.fill_event = EventPage(self.driver)
        self.fill_event.fill_event_name("exam")
        self.fill_event.save.click()

    def test_press_calender_week(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.calendar_page = CalendarPage(self.driver)
        self.test_press_calender_week()
