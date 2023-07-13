import csv
import allure
import pytest

from .base_page import BasePage
from .locators import TransactionPageLocators
from ..settings import csv_file_path


'''Страница с транзакциями'''
class TransactionPage(BasePage):

    locators = TransactionPageLocators()

    '''Получение данных и запись их в файл csv'''
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
        
        @allure.step("CSV-файл")
        def attach_csv_file(file_path):
            with open(file_path, "rb") as file:
                allure.attach(file.read(), name=csv_file_path, attachment_type=allure.attachment_type.CSV)

        with open(csv_file_path, "w", newline="") as file:
            writer = csv.writer(file)
            for transaction in transactions:
                timestamp = transaction["timestamp"]
                amount = transaction["amount"]
                transaction_type = transaction["transaction_type"]
                writer.writerow([timestamp, amount, transaction_type])

        attach_csv_file(csv_file_path)
