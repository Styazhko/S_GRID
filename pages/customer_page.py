import allure

from .locators import CustomerPageLocators
from .base_page import BasePage


'''Страница выбора клиента'''
class CustomerPage(BasePage):
    
    locators = CustomerPageLocators()

    '''Выбор клиента из settings.py'''
    @allure.step("Выбор клиента")
    def user_select(self):
        self.element_is_visible(self.locators.YOUR_NAME).click() # Можно не использовать в данном случае
        self.element_is_visible(self.locators.USER_SELECT).click()

    '''Нажатие на кнопку входа'''
    @allure.step("Нажатие кнопки входа")
    def login(self):
        self.element_is_visible(self.locators.LOGIN).click()
