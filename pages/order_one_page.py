from selenium.webdriver.common.by import By
from locators.order_page_one_locators import OrderPageOneLocators
from constants import Constants


class OrderPageOne:
    name = OrderPageOneLocators.NAME
    surname = OrderPageOneLocators.SURNAME
    adress = OrderPageOneLocators.ADRESS
    metro = OrderPageOneLocators.METRO
    phone = OrderPageOneLocators.PHONE
    next_button = OrderPageOneLocators.NEXT_BUTTON
    metro_selector = OrderPageOneLocators.METRO_SELECTOR

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        self.driver.find_element(*self.name).send_keys(Constants.NAME)
        self.driver.find_element(*self.surname).send_keys(Constants.SURNAME)
        self.driver.find_element(*self.adress).send_keys(Constants.ADRESS)
        self.driver.find_element(*self.metro).send_keys(Constants.METRO)
        self.driver.find_element(*self.metro_selector).click()
        self.driver.find_element(*self.phone).send_keys(Constants.PHONE)

    def click_next(self):
        self.driver.find_element(*self.next_button).click()