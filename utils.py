import csv
import allure
import datetime


'''Вычисление N-го числа Фибоначчи, где N это текущий день запуска теста + 1'''
def fibonacci_from_today_plus_one():
    current_day = datetime.datetime.now().date().day
    current_day_plus_one = current_day + 1
    fibonacci_number = fibonacci(current_day_plus_one)
    return fibonacci_number

'''Вычисление числа Фибоначчи'''
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

'''Запись данных в csv файл'''    
def write_transactions_to_csv(transactions, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for transaction in transactions:
            timestamp = transaction["timestamp"]
            amount = transaction["amount"]
            transaction_type = transaction["transaction_type"]
            writer.writerow([timestamp, amount, transaction_type])

'''Прикрепление csv файла к allure отчету'''
@allure.step("CSV-файл")
def attach_csv_file(file_path):
    with open(file_path, "rb") as file:
        allure.attach(file.read(), name="transactions.csv", attachment_type=allure.attachment_type.CSV)
        