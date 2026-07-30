import allure
from selenium.webdriver.common.by import By

from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from urls import URL


class OrderPage(BasePage):

    URL = URL.ORDER_FEED_URL

    @allure.step("Нажать на кнопку Конструктор и дождаться отображения главной страницы")
    def click_constructor_btn(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_BTN)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Получить значение счётчика «Выполнено за всё время»")
    def get_total_orders_quantity(self):
        return int(self.get_text_locator(OrderPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_today_orders_quantity(self):
        return int(self.get_text_locator(OrderPageLocators.TODAY_ORDERS_COUNTER))
        
    @allure.step("Дождаться увеличения значения счётчика «Выполнено за всё время»")
    def wait_for_total_counter_to_increase(self, quantity_before: int):
        self.wait.until(lambda _: self.get_total_orders_quantity() > quantity_before)
        
    @allure.step("Дождаться увеличения значения счётчика «Выполнено за сегодня»")
    def wait_for_today_counter_to_increase(self, quantity_before: int):
        self.wait.until(lambda _: self.get_today_orders_quantity() > quantity_before)

    @allure.step("Проверить, что номер заказа {order_number} появился в разделе «В работе»")
    def is_order_number_visible_in_progress_section(self, order_number):
        xpath = OrderPageLocators.ORDER_IN_PROGRESS.format(order_number)
        locator = (By.XPATH, xpath)
        return self.is_element_displayed(locator)
