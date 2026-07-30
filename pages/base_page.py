import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from js_helpers import HTML5_DRAG_AND_DROP

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Нажать на элемент с локатором")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.execute_script("arguments[0].click();", element)

    @allure.step("Ожидать элемент по локатору")
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проверить отображение элемента по локатору")
    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except Exception:
            return False

    @allure.step("Дождаться появления элемента по локатору")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Получить текст элемента по локатору и очистить от лишних пробелов")
    def get_text_locator(self, locator):
        element = self.wait_for_element(locator)
        return element.text.strip()

    @allure.step("Дождаться исчезновения элемента")
    def wait_for_element_to_disappear(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.element_to_be_clickable(source_locator))
        target = self.wait.until(EC.element_to_be_clickable(target_locator))
        self.driver.execute_script(HTML5_DRAG_AND_DROP, source, target)
