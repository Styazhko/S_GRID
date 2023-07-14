import allure

from .locators import AccountPageLocators
from .base_page import BasePage
from ..utils import fibonacci_from_today_plus_one

'''Страница выбора клиента'''
class AccountPage(BasePage):
      
    locators = AccountPageLocators()

    '''Пополнение счета'''    
    @allure.step("Пополнение счета")
    def deposit(self):
        self.element_is_visible(self.locators.DEPOSIT).click()
        deposit = self.element_is_visible(self.locators.AMOUNT_DEPOSIT)
        deposit.send_keys(fibonacci_from_today_plus_one())
        self.element_is_visible(self.locators.PUT_DEPOSIT).click()
        print(fibonacci_from_today_plus_one())

    '''Снятие со счета'''
    @allure.step("Снятие со счета")
    def withdrawl(self):
        self.element_is_visible(self.locators.WITHDRAWL).click()
        withdrawl = self.element_is_visible(self.locators.AMOUNT_WITHDRAWL)
        withdrawl.send_keys(fibonacci_from_today_plus_one())
        self.element_is_visible(self.locators.WITHDRAWL_DEPOSIT).click()

    '''Переход на страницу с транзакциями'''
    @allure.step("Переход на страницу с транзакциями")
    def go_to_transactions_page(self):
        self.element_is_visible(self.locators.TRANSACTIONS).click()

    '''Проверка баланса'''
    @allure.step("Проверка баланса")
    def should_be_zero(self):
        balance_on_page = self.element_is_visible(self.locators.BALANCE).text
        expected_balance = '0'
        assert balance_on_page == expected_balance, "Баланс не равен нулю"
    