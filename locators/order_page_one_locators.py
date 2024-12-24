from selenium.webdriver.common.by import By


class OrderPageOneLocators:
    NAME = [By.XPATH, './/div/input[@placeholder = "* Имя"]']
    SURNAME = [By.XPATH, './/div/input[@placeholder = "* Фамилия"]']
    ADRESS = [By.XPATH, './/div/input[@placeholder = "* Адрес: куда привезти заказ"]']
    METRO = [By.XPATH, './/div/input[@placeholder = "* Станция метро"]']
    PHONE = [By.XPATH, './/div/input[@placeholder = "* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, './/button[text() = "Далее"]']
    METRO_SELECTOR = [By.XPATH, './/*[text() = "Белорусская"]']