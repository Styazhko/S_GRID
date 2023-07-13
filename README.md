# Тестовое задание
## Предварительно необходимо установить Allure, Selenium GRID
## Установка и запуск
1. Склонировать репозиторий с Github:
````
git clone https://github.com/Styazhko/S_GRID
````
2. Перейти в директорию проекта
3. Создать виртуальное окружение:
````
python -m venv venv
````
4. Активировать окружение: 
````
venv\Scripts\activate
````
5. Установка зависимостей:
```
pip install -r requirements.txt
```
6. Добавить нужные данные в файл 'settings.py'
7. Запустить Selenium GRID в консоле:
```
java -jar selenium-server-X.X.X.jar standalone
```
8. Запустить тест:
```
pytest test_wallet.py --alluredir=allureress
```
9. Запустить просмотр отчетов:
```
allure serve allureress
```