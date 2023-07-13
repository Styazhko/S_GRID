import datetime
import time

from .locators import AccountPageLocators
from .base_page import BasePage


'''Страница выбора клиента'''
class AccountPage(BasePage):
      
    locators = AccountPageLocators()

    '''Вычисление N-го числа Фибоначчи, где N это текущий день запуска теста + 1'''
    def fibonacci_from_today_plus_one(self):
        current_day = datetime.datetime.now().date().day
        current_day_plus_one = current_day + 1
        fibonacci_number = self.fibonacci(current_day_plus_one)
        return fibonacci_number

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    '''Пополнение счета'''    
    def deposit(self):
        self.element_is_visible(self.locators.DEPOSIT).click()
        deposit = self.element_is_visible(self.locators.AMOUNT_DEPOSIT)
        deposit.send_keys(self.fibonacci_from_today_plus_one())
        self.element_is_visible(self.locators.PUT_DEPOSIT).click()

    '''Снятие со счета'''
    def withdrawl(self):
        self.element_is_visible(self.locators.WITHDRAWL).click()
        withdrawl = self.element_is_visible(self.locators.AMOUNT_WITHDRAWL)
        withdrawl.send_keys(self.fibonacci_from_today_plus_one())
        self.element_is_visible(self.locators.WITHDRAWL_DEPOSIT).click()

    '''Переход на страницу с транзакциями'''
    def go_to_transactions_page(self):
        self.element_is_visible(self.locators.TRANSACTIONS).click()

    '''Проверка баланса'''
    def should_be_zero(self):
        balance_on_page = self.element_is_visible(self.locators.BALANCE).text
        expected_balance = '0'
        assert balance_on_page == expected_balance, "Баланс не равен нулю"
    