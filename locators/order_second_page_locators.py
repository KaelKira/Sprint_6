from selenium.webdriver.common.by import By


class OrderSecondPageLocators:
    WHEN = [By.XPATH, './/div/input[@placeholder = "* Когда привезти самокат"]']
    DATA = [By.XPATH, './/div[@class = "react-datepicker__week"][last()]/div[last()]']
    TIME_RENT_INPUT = [By.XPATH, './/div[text() = "* Срок аренды"]']
    TIME_RENT_ONE_DAY = [By.XPATH, './/*[text() = "сутки"]']
    COLOR_BLACK = [By.XPATH, './/input[@id = "black"]']
    COLOR_GREY = [By.XPATH, './/input[@id = "grey"]']
    COMMENT = [By.XPATH, './/div/input[@placeholder = "Комментарий для курьера"]']
    ORDER_BUTTON = [By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text()= "Заказать"]']
    CONFIRMATION_BUTTON = [By.XPATH, './/button[text() = "Да"]']
    CONFIRMATION_HEADER = [By.XPATH, './/div[@class = "Order_ModalHeader__3FDaJ"]']
