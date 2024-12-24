from selenium.webdriver.common.by import By
from locators.order_page_one_locators import OrderPageOneLocators
from constants import Constants
from locators.order_second_page_locators import OrderSecondPageLocators


class OrderSecondPage:
    when = OrderSecondPageLocators.WHEN
    data = OrderSecondPageLocators.DATA
    time_rent = OrderSecondPageLocators.TIME_RENT_INPUT
    time_rent_value = OrderSecondPageLocators.TIME_RENT_ONE_DAY
    color = OrderSecondPageLocators.COLOR_BLACK
    comment = OrderSecondPageLocators.COMMENT
    order_button = OrderSecondPageLocators.ORDER_BUTTON
    confirmation_button = OrderSecondPageLocators.CONFIRMATION_BUTTON
    confirmation_text = OrderSecondPageLocators.CONFIRMATION_HEADER


    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        self.driver.find_element(*self.when).click()
        self.driver.find_element(*self.data).click()
        self.driver.find_element(*self.time_rent).click()
        self.driver.find_element(*self.time_rent_value).click()
        self.driver.find_element(*self.color).click()
        self.driver.find_element(*self.comment).send_keys(Constants.COMMENT)

    def click_order(self):
        self.driver.find_element(*self.order_button).click()

    def click_confirm(self):
        self.driver.find_element(*self.confirmation_button).click()

    def check_order_placed(self):
        text = self.driver.find_element(*self.confirmation_text).text
        assert 'Заказ оформлен' in text