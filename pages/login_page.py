from .locators import LoginPageLocators
from .base_page import BasePage


'''Главная страница'''
class LoginPage(BasePage):
    
    locators = LoginPageLocators()
    
    '''Переход к выбору пользователя'''
    def go_to_customer_page(self):
        self.element_is_visible(self.locators.CUSTOMER_LOGIN).click()
