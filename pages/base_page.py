import allure

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


'''Базовый класс для работы со страницами'''
class BasePage:
    
    '''Инициализация browser and url с неявным ожиданием 20с.'''
    def __init__(self, browser, url, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    '''Открытие страницы по заданному url'''
    @allure.step("Открытие страницы по заданному url")
    def open(self):
        self.browser.get(self.url)

    '''Явное ожидание появления элемента по заданному locator'''
    def element_is_visible(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    '''Явное ожидание появления элементов по заданному locator'''
    def elements_are_visible(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))
