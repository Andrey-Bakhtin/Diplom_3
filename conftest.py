import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers import Orders, Users


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    options = ChromeOptions() if request.param == 'chrome' else FirefoxOptions()
    driver_cls = webdriver.Chrome if request.param == 'chrome' else webdriver.Firefox

    options.add_argument("--window-size=1920,1080")

    driver = driver_cls(options=options)
    try:
        driver.maximize_window()
        yield driver
    finally:
        driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.wait_for_element(MainPageLocators.CONSTRUCTOR_TITLE)
    return main_page

@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)
    order_page.open()
    order_page.wait_for_element(OrderPageLocators.ORDER_TITLE)
    return order_page

@pytest.fixture
def create_user_and_delete_after_test():
    response = Users.register()
    yield response
    token = response.json()["accessToken"]
    if token:
        Users.delete(token)

@pytest.fixture
def create_order(create_user_and_delete_after_test):
    response = Orders.create_for_user(create_user_and_delete_after_test)
    data = response.json()
    number = data.get("order").get("number")
    order_number = str(number).zfill(6)
    return {"order_number": order_number}
