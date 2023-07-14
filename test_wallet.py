import allure

from .pages.transaction_page import TransactionPage
from .pages.login_page import LoginPage
from .pages.customer_page import CustomerPage
from .pages.account_page import AccountPage


'''Тест'''
class TestBank:

    @allure.feature("Банк")
    @allure.story("Взаимодействия в личном кабинете")
    @allure.title("Тест успешной обработки транзакций")
    def test_bank(self, browser):
        link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_customer_page()
        customer_page = CustomerPage(browser, browser.current_url)
        customer_page.user_select()
        customer_page.login()
        account_page = AccountPage(browser, browser.current_url)
        account_page.deposit()
        account_page.withdrawl()
        account_page.should_be_zero()
        account_page.go_to_transactions_page()
        transaction_page = TransactionPage(browser, browser.current_url)
        transaction_page.transaction_in_csv()
        