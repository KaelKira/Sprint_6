import allure
from constants import Constants
from locators.order_second_page_locators import OrderSecondPageLocators
from pages.base_page import BasePage


class OrderSecondPage(BasePage):

    @allure.step('fill_second_form')
    def fill_form(self):
        self.find_element_and_click(OrderSecondPageLocators.WHEN)
        self.find_element_and_click(OrderSecondPageLocators.DATA)
        self.find_element_and_click(OrderSecondPageLocators.TIME_RENT_INPUT)
        self.find_element_and_click(OrderSecondPageLocators.TIME_RENT_ONE_DAY)
        self.find_element_and_click(OrderSecondPageLocators.COLOR_BLACK)
        self.send_key(OrderSecondPageLocators.COMMENT, Constants.COMMENT)

    @allure.step('click_order')
    def click_order(self):
        self.find_element_and_click(OrderSecondPageLocators.ORDER_BUTTON)

    @allure.step('click_confirm')
    def click_confirm(self):
        self.find_element_and_click(OrderSecondPageLocators.CONFIRMATION_BUTTON)

    @allure.step('check_order_placed')
    def check_order_placed(self):
        text = self.find_element_get_text(OrderSecondPageLocators.CONFIRMATION_HEADER)
        assert 'Заказ оформлен' in text