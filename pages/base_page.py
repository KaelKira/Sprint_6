from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.MAIN_URL

    def go_to_site(self):
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message = f'Not find element{locator}')

    def find_element_and_click(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message = f'Not find element{locator}').click()

    def find_element_get_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message = f'Not find element{locator}').text

    def send_key(self, locator, key, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                               message=f'Not find element{locator}').send_keys(key)
    def switch_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])

    def get_url(self):
        return self.driver.current_url