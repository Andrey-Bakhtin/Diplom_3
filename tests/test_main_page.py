import allure

from urls import URL


class TestMainPage:
    
    @allure.title("Проверка, что при нажатии на кнопку Конструктор происходит переход на главную страницу")
    def test_click_constructor_btn_opens_main_page(self, order_page):
        order_page.click_constructor_btn()
        assert order_page.get_current_url() == f"{URL.MAIN_URL}/"

    @allure.title("Проверка, что при нажатии на кнопку Лента заказов происходит переход на раздел «Лента заказов»")
    def test_click_order_feed_btn_opens_order_feed_page(self, main_page):
        main_page.click_order_feed_btn()
        assert main_page.get_current_url() == URL.ORDER_FEED_URL

    @allure.title("Проверка, что при нажатии на ингредиент появляется всплывающее окно с деталями")
    def test_click_ingredient_opens_popup(self, main_page):
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_popup_displayed()
        
    @allure.title("Проверка, что при нажатии на крестик всплывающее окно с деталями ингредиента закрывается")
    def test_click_close_btn_closes_ingredient_popup(self, main_page):
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_popup_displayed()
        main_page.click_close_popup()
        assert main_page.is_ingredient_popup_closed()
        
    @allure.title("Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_adding_ingredient_increases_ingredient_counter(self, main_page):
        quantity_before = main_page.get_ingredient_counter_value()
        main_page.add_first_ingredient()
        quantity_after = main_page.get_ingredient_counter_value() 
        assert quantity_after > quantity_before
