# main_page.py
import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from urls import URL

class MainPage(BasePage):
    URL = URL.MAIN_URL

    @allure.step("Нажать на кнопку Лента заказов и дождаться отображения страницы ленты")
    def click_order_feed_btn(self):
        self.click_element(HeaderLocators.ORDER_FEED_BTN)
        self.wait_for_element(OrderPageLocators.ORDER_TITLE)

    @allure.step("Нажать на первый ингредиент")
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Проверить отображение Popup ингредиента")
    def is_ingredient_popup_displayed(self):
        return self.is_element_displayed(MainPageLocators.INGREDIENT_POPUP)

    @allure.step("Закрыть Popup ингредиента нажатием на крестик")
    def click_close_popup(self):
        return self.click_element(MainPageLocators.CLOSE_POPUP_BTN)

    @allure.step("Проверить, что Popup ингредиента закрылся")
    def is_ingredient_popup_closed(self):
        return self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_POPUP)

    @allure.step("Добавить первый ингредиент в корзину")
    def add_first_ingredient(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.BASKET_LIST))
        self.drag_and_drop(MainPageLocators.FIRST_INGREDIENT, MainPageLocators.BASKET_LIST)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter_value(self):
        return int(self.get_text_locator(MainPageLocators.FIRST_INGREDIENT_COUNTER))
