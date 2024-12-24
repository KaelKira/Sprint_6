import time

from selenium import webdriver
from constants import Constants
from pages.order_one_page import OrderPageOne
from pages.order_second_page import OrderSecondPage
from pages.main_page import MainPage


class TestOrderFromHeader:
    def test_order_form_header(self, driver):
        main_page = MainPage(driver)
        order_one_page = OrderPageOne(driver)
        order_second_page = OrderSecondPage(driver)
        main_page.click_order_header()
        order_one_page.fill_form()
        order_one_page.click_next()
        order_second_page.fill_form()
        order_second_page.click_order()
        order_second_page.click_confirm()
        order_second_page.check_order_placed()

    def test_order_form_footer(self, driver):
        main_page = MainPage(driver)
        order_one_page = OrderPageOne(driver)
        order_second_page = OrderSecondPage(driver)
        main_page.assept_cookie()
        main_page.click_order_footer()
        order_one_page.fill_form()
        order_one_page.click_next()
        order_second_page.fill_form()
        order_second_page.click_order()
        order_second_page.click_confirm()
        order_second_page.check_order_placed()

