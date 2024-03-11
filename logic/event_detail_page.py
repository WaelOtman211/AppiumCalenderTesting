import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy


class eventDetailsPage():
    EVENT_NAME = "com.claudivan.taskagenda:id/tvTitulo"
    EVENT_DESCRIPTION = "com.claudivan.taskagenda:id/tvDescricao"
    EVENT_DATE ="com.claudivan.taskagenda:id/tvDescricao"
    EVENT_TYPE = "com.claudivan.taskagenda:id/tvTipo"
    EVEN_TIME ="com.claudivan.taskagenda:id/tvHora"

    def __init__(self, driver):
        self.driver = driver
        self.init_elements()

    def init_elements(self):
        time.sleep(1)
        self.event_name = self.driver.find_element(by=AppiumBy.ID, value=self.EVENT_NAME)
        self.event_type = self.driver.find_element(by=AppiumBy.ID, value=self.EVENT_TYPE)

        self.event_description = self.driver.find_element(by=AppiumBy.ID, value=self.EVENT_DESCRIPTION)
        self.event_date = self.driver.find_element(by=AppiumBy.ID, value=self.EVENT_DATE)
        self.event_time = self.driver.find_element(by=AppiumBy.ID, value=self.EVEN_TIME)


    def choose_event_by_index(self, index):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value=f'//android.widget.ListView[@resource-id="com.claudivan.taskagenda:id/lvListaEventos"]/android.widget.FrameLayout[{index}]/android.widget.RelativeLayout').click()



    def get_event_name(self):
        return self.event_name.text

    def get_event_type(self):
        return self.event_type.text

    def get_event_date(self):
        return self.event_date.text

    def get_event_description(self):
        return self.event_description.text

    def get_event_time(self):
       return self.event_time.text.split("h")


        #return self.event_time.text.split("h")