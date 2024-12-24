import time

from locators.main_page_locators import MainPageLocators


class MainPage:
    yandex_logo = MainPageLocators.YANDEX_LOGO
    main_logo = MainPageLocators.SAMOKAT_LOGO
    order_button_header = MainPageLocators.ORDER_BUTTON_HEADER
    order_button_footer = MainPageLocators.ORDER_BUTTON_FOOTER
    cookie_button = MainPageLocators.COOKIE
    header = MainPageLocators.HEADER

    def __init__(self, driver):
        self.driver = driver

    def click_on_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def click_on_main_logo(self):
        self.driver.find_element(*self.main_logo).click()

    def click_order_header(self):
        self.driver.find_element(*self.order_button_header).click()

    def click_order_footer(self):
        self.driver.find_element(*self.order_button_footer).click()

    def assept_cookie(self):
        self.driver.find_element(*self.cookie_button).click()

    def check_header_text(self):
        text = self.driver.find_element(*self.header).text
        assert 'Самокат' in text

    def check_yandex_redirect(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])
        current_url = self.driver.current_url
        assert 'ya.ru' or 'yandex.ru' in current_url

