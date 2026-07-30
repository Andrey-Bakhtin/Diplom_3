import allure

from helpers import Orders


class TestOrdersSection:

    @allure.title("Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_creating_order_updates_total_orders_counter(self, order_page, create_user_and_delete_after_test):
        total_quantity_before = order_page.get_total_orders_quantity()
        Orders.create_for_user(create_user_and_delete_after_test)
        order_page.wait_for_total_counter_to_increase(total_quantity_before)
        total_quantity_after = order_page.get_total_orders_quantity()
        assert total_quantity_after > total_quantity_before

    @allure.title("Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_creating_order_updates_today_orders_counter(self, order_page, create_user_and_delete_after_test):
        today_quantity_before = order_page.get_today_orders_quantity()
        Orders.create_for_user(create_user_and_delete_after_test)
        order_page.wait_for_today_counter_to_increase(today_quantity_before)
        today_quantity_after = order_page.get_today_orders_quantity()
        assert today_quantity_after > today_quantity_before

    @allure.title("Проверка, что после оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_is_shown_in_progress_section(self, order_page, create_order):
        order_number = create_order["order_number"]
        assert order_page.is_order_number_visible_in_progress_section(order_number)
