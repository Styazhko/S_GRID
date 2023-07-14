import allure
import pytest

from .base_page import BasePage
from .locators import TransactionPageLocators
from ..settings import csv_file_path
from ..utils import write_transactions_to_csv, attach_csv_file


'''Страница с транзакциями'''
class TransactionPage(BasePage):

    locators = TransactionPageLocators()

    '''Получение данных и запись их в файл csv'''
    @allure.step("Получение данных транзакций и запись их в файл csv")
    def transaction_in_csv(self):
        transactions = []
        tables = self.elements_are_visible(self.locators.BODY_TRANSACTION)
        for table in tables:
            rows = table.find_elements(*self.locators.ROWS)
            if not rows:
                pytest.fail("Транзакции отсутствуют")
            for row in rows:
                date_time = row.find_element(*self.locators.DATE).text
                amount = row.find_element(*self.locators.AMOUNT).text
                transaction_type = row.find_element(*self.locators.TRANSACTION_TYPE).text
                transaction = {"timestamp": date_time, "amount": amount, "transaction_type": transaction_type}
                transactions.append(transaction)
        write_transactions_to_csv(transactions, csv_file_path)
        attach_csv_file(csv_file_path)
