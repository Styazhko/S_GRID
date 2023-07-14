import pytest

from selenium import webdriver
from .settings import host


'''Фикстура для открытия Chrome в начале теста и закрытие по завершению теста'''
@pytest.fixture(scope="class")
def browser(): 
    print("\nstart chrome browser for test..")
    browser = webdriver.Remote(
        command_executor=host + "/wd/hub",
        options=webdriver.ChromeOptions()
    )
    # browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    