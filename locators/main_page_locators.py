from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_HEADER = [By.XPATH, './/div[@class = "Header_Nav__AGCXC" ]/button']
    ORDER_BUTTON_FOOTER = [By.XPATH, './/div[@class = "Home_FinishButton__1_cWm" ]/button']
    YANDEX_LOGO = [By.XPATH, './/div/a[@href = "//yandex.ru"]']
    SAMOKAT_LOGO = [By.XPATH, './/div/a[@href = "/"]']
    COOKIE = [By.XPATH, './/button[text() = "да все привыкли"]']
    HEADER = [By.XPATH, './/div[@class = "Home_Header__iJKdX"]']

