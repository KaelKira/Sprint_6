from pages.main_page import MainPage


class TestOrderFromHeader:

    def test_main_logo_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_header()
        main_page.click_on_main_logo()
        main_page.check_header_text()

    def test_yandex_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        main_page.check_yandex_redirect()


