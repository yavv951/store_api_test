# Дипломный проект по автоматизации API тестирования для store. 
<a target="_blank" href="https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/">Веб сайт store</a>

## :memo: Содержание:

- [Реализованные проверки](#boom-Реализованные-проверки)
- [Технологии](#classical_building-Технологии)
- [Сборка в Jenkins](#man_cook-Jenkins-job)
- [Запуск из терминала](#electron-Запуск-тестов-из-терминала)
- [Allure отчет](#bar_chart-Allure-отчет)
- [Allure TestOps](#Allure-TestOps)
- [Отчет в Telegram](#envelope-Уведомление-в-Telegram-при-помощи-бота)

## :boom: Реализованные проверки

- ✓ Проверка логотипа
- ✓ Проверка функции поиска по тексту
- ✓ Проверка текста ошибки на странице авторизации/регистрации
- ✓ Проверка страницы Адреса
- ✓ Проверка функции поиска по фото
- ✓ Проверка поиска через меню (бургер)

## :classical_building: Технологии

<p align="center">
<img width="6%" title="Idea" src="images/logo/Pycharm.svg">
<img width="6%" title="Java" src="images/logo/Python.svg">
<img width="6%" title="Allure Report" src="images/logo/Allure.svg">
<img width="6%" title="JUnit5" src="images/logo/Pytest.svg">
<img width="6%" title="GitHub" src="images/logo/GitHub.svg">
<img width="6%" title="Jenkins" src="images/logo/Jenkins.svg">
<img width="6%" title="Telegram" src="images/logo/Telegram.svg">
<img width="6%" title="Telegram" src="images/logo/Allure_TO.svg">
</p>

## :man_cook: Jenkins job
<img src="images/logo/Jenkins.svg" width="25" height="25"  alt="Jenkins"/></a>  <a target="_blank" href="https://jenkins.autotests.cloud/job/store_api_test/">Jenkins job</a>
<p align="center">
<a href="https://jenkins.autotests.cloud/job/store_api_test/"><img src="images/image/Jenkins.jpg" alt="Jenkins"/></a>
</p>

## :electron: Запуск тестов из терминала

Локальный запуск:

Create and activate virtual environments

```
python3 -m venv venv
source venv/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

### Run all tests

```
pytest
```

## :bar_chart: Allure-отчет
<img src="images/logo/Allure.svg" width="25" height="25"  alt="Allure"/></a> Отчет в <a target="_blank" href="https://jenkins.autotests.cloud/job/store_api_test/allure/#graph">Allure report</a>
<p align="center">
<a href="https://jenkins.autotests.cloud/job/store_api_test/allure/"><img src="images/image/Allure3.jpg" alt="Allure-отчет"/></a>
</p>


## :envelope: Уведомление-в-Telegram-при-помощи-бота
<p align="center">
<img src="images/image/telegram.jpg" alt="Telegram"/></a>
</p>