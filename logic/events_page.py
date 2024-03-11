import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from Logic.event_detail_page import eventDetailsPage


class eventsPage():
    ALLOW_NOTIFICATION_BUTTON = "com.android.permissioncontroller:id/permission_allow_button"
    def __init__(self, driver):
        self.driver = driver

    def choose_event_by_index(self,index):
        formated_event_string = f'//android.widget.ListView[@resource-id="com.claudivan.taskagenda:id/lvListaEventos"]/android.widget.FrameLayout[{index}]/android.widget.RelativeLayout'
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(AppiumBy.XPATH,formated_event_string)).click()


    def go_to_event_details_by_index(self,index):
        self.choose_event_by_index(index)
        self.event_details_page = eventDetailsPage(self.driver)
        return self.event_details_page


    def click_allow_notification(self):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(AppiumBy.ID,self.ALLOW_NOTIFICATION_BUTTON)).click()
