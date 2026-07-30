from selenium.webdriver.common.by import By


class HeaderLocators:
    
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BTN = (By.XPATH, ".//p[text()='Лента Заказов']")
    
