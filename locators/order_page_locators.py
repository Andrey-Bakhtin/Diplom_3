from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    ORDER_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    ORDER_IN_PROGRESS = ".//ul[contains(@class, 'OrderFeed_orderList')]//li[text()='{}']"
