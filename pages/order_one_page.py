import allure
from locators.order_page_one_locators import OrderPageOneLocators
from constants import Constants
from pages.base_page import BasePage


class OrderPageOne(BasePage):

    @allure.step('fill_first_form')
    def fill_form(self):
        self.send_key(OrderPageOneLocators.NAME, Constants.NAME)
        self.send_key(OrderPageOneLocators.SURNAME,Constants.SURNAME)
        self.send_key(OrderPageOneLocators.ADRESS,Constants.ADRESS)
        self.send_key(OrderPageOneLocators.METRO,Constants.METRO)
        self.find_element_and_click(OrderPageOneLocators.METRO_SELECTOR)
        self.send_key(OrderPageOneLocators.PHONE,Constants.PHONE)

    @allure.step('click_next')
    def click_next(self):
        self.find_element_and_click(OrderPageOneLocators.NEXT_BUTTON)