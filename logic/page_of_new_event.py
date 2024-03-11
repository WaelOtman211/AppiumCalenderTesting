
from appium.webdriver.common.appiumby import AppiumBy


class NewEventPage:
    LOCATORS = {
        "EVENT_NAME": (AppiumBy.ID, "com.claudivan.taskagenda:id/etTitulo"),
        "SAVE_EVENT": (AppiumBy.ID, "com.claudivan.taskagenda:id/item_salvar"),
        "TIME_FIELD": (AppiumBy.ID, "com.claudivan.taskagenda:id/btHora"),
        "TASK_TYPE": (AppiumBy.ID, "com.claudivan.taskagenda:id/tvTipo"),
        "DESCRIPTION": (AppiumBy.ID, "com.claudivan.taskagenda:id/etDescricao"),
        "ADD_REMINDER": (AppiumBy.ID, "com.claudivan.taskagenda:id/btAdicionarNotificacao"),
        "IMPORTANT_EVENT": (AppiumBy.XPATH, "//android.widget.ListView[@resource-id='android:id/select_dialog_listview']/android.widget.RelativeLayout[1]"),
        "TASK_EVENT": (AppiumBy.XPATH, "//android.widget.ListView[@resource-id='android:id/select_dialog_listview']/android.widget.RelativeLayout[2]"),
        "NOT_FORGET_EVENT": (AppiumBy.XPATH, "//android.widget.ListView[@resource-id='android:id/select_dialog_listview']/android.widget.RelativeLayout[3]"),
        "DATE_FIELD": (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.claudivan.taskagenda:id/btData']"),
        "DATE_YEAR": (AppiumBy.ID, "android:id/date_picker_header_year")
    }

    def __init__(self, driver):
        self.driver = driver
        self.initialize_elements()

    def initialize_elements(self):
        self.elements = {name: self.driver.find_element(*locator) for name, locator in self.LOCATORS.items()}

    def click_add_reminder_button(self):
        self.elements["ADD_REMINDER"].click()

    def enter_description(self, text):
        self.elements["DESCRIPTION"].send_keys(text)

    def enter_event_name(self, text):
        self.elements["EVENT_NAME"].send_keys(text)

    def click_time_field(self):
        self.elements["TIME_FIELD"].click()

    def select_event_type(self, event_type):
        element = self.LOCATORS.get(event_type.upper() + "_EVENT")
        if not element:
            raise ValueError("Invalid event type")
        self.driver.find_element(*element).click()

    def get_time_field_text(self):
        return self.elements["TIME_FIELD"].text

    def get_date_field_text(self):
        return self.elements["DATE_FIELD"].text

    def choose_year_for_date(self, year):
        pass

    def enter_date(self, date):
        pass

    def initialize_time_field(self):
        self.elements["TIME_FIELD"] = self.driver.find_element(*self.LOCATORS["TIME_FIELD"])
