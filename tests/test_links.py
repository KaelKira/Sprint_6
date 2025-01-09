import allure
from pages.main_page import MainPage



class TestOrderFromHeader:

    @allure.title('Тестируется переход на главную при клике на логотип')
    def test_main_logo_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_header()
        main_page.click_on_main_logo()
        main_page.check_header_text()

    @allure.title('Тестируется переход на главную Yandex при клике на логотип Yandex')
    def test_yandex_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        main_page.check_yandex_redirect()


