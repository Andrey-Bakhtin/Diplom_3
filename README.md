# Автотесты UI для Stellar Burgers

## Описание

Проект содержит UI-автотесты для веб-приложения Stellar Burgers. Тесты покрывают основные сценарии пользовательского взаимодействия, включая переходы по разделам, оформление заказа и проверку ключевых элементов интерфейса.

## Стек технологий

- Python 3
- Pytest
- Selenium
- Allure
- Faker
- Requests

## Структура проекта

- conftest.py — фикстуры pytest
- helpers.py — тестовые данные
- js_helpers.py — js-code drag_and_drop
- locators/ — локаторы
- pages/ — page object модели
- tests/ — тестовые сценарии
- requirements.txt — зависимости
- allure_results/ — сгенерированные отчеты

## Base URL

https://stellarburgers.education-services.ru/

## Реализованные сценарии
Тесты покрывают основные сценарии пользовательского взаимодействия, включая переходы по разделам, оформление заказа и проверку ключевых элементов интерфейса.

## Установка и запуск тестов

1. Клонируйте репозиторий:
git clone <ссылка_на_репозиторий>
cd Diplom_3
   
2. Создайте и активируйте виртуальное окружение:
python -m venv .venv
.venv\Scripts\activate
  
3. Установите зависимости:
pip install -r requirements.txt

4. Запустите тесты:
pytest -v

## Запуск Allure-отчёта
1. Запустите тесты с сохранением результатов в директорию Allure:
pytest -v --alluredir=allure_results

2. Сформируйте и откройте отчёт:
allure serve allure_results
