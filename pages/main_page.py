from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('click_on_yandex_logo')
    def click_on_yandex_logo(self):
        self.find_element_and_click(MainPageLocators.YANDEX_LOGO)

    @allure.step('click_on_main_logo')
    def click_on_main_logo(self):
        self.find_element_and_click(MainPageLocators.SAMOKAT_LOGO)

    @allure.step('click_order_header')
    def click_order_header(self):
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('click_order_footer')
    def click_order_footer(self):
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step('assept_cookie')
    def assept_cookie(self):
        self.find_element_and_click(MainPageLocators.COOKIE)

    @allure.step('check_header_text')
    def check_header_text(self):
        text = self.find_element_get_text(MainPageLocators.HEADER)
        assert 'Самокат' in text

    @allure.step('check_yandex_redirect')
    def check_yandex_redirect(self):
        self.switch_window()
        current_url = self.get_url()
        assert 'ya.ru' or 'yandex.ru' in current_url