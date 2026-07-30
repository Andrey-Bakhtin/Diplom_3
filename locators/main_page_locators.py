from selenium.webdriver.common.by import By


class MainPageLocators:
    
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")

    FIRST_INGREDIENT = (By.XPATH, "(.//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    INGREDIENT_POPUP = (By.XPATH, ".//h2[normalize-space()='Детали ингредиента']")
    CLOSE_POPUP_BTN = (By.CSS_SELECTOR, "button[type='button'][class*='Modal_modal__close']")

    FIRST_INGREDIENT_COUNTER = (By.XPATH, "(.//p[contains(@class, 'counter_counter__num__3nue1')])[1]")
    BASKET_LIST = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
