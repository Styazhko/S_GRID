from selenium.webdriver.common.by import By
from ..settings import customer


class LoginPageLocators:
    CUSTOMER_LOGIN = (By.XPATH, "//*[text()='Customer Login']")
    
    
class CustomerPageLocators:
    YOUR_NAME = (By.ID, "userSelect")
    USER_SELECT = (By.XPATH, "//*[text()='{}']".format(customer))
    LOGIN = (By.CSS_SELECTOR, ".btn.btn-default")


class AccountPageLocators:
    TRANSACTIONS = (By.CSS_SELECTOR, "div:nth-child(5) > button:nth-child(1)")
    DEPOSIT = (By.CSS_SELECTOR, "div:nth-child(5) > button:nth-child(2)")
    WITHDRAWL = (By.CSS_SELECTOR, "div:nth-child(5) > button:nth-child(3)")
    AMOUNT_DEPOSIT = (By.XPATH, "//label[text()='Amount to be Deposited :']/following-sibling::input[@placeholder='amount']")
    AMOUNT_WITHDRAWL = (By.XPATH, "//label[text()='Amount to be Withdrawn :']/following-sibling::input[@placeholder='amount']")
    PUT_DEPOSIT = (By.XPATH, "//*[text()='Deposit']")
    WITHDRAWL_DEPOSIT = (By.XPATH, "//*[text()='Withdraw']")
    BALANCE = (By.CSS_SELECTOR, "div:nth-child(3) > strong:nth-child(2)")


class TransactionPageLocators:
    DATE = (By.CSS_SELECTOR, "td.ng-binding:nth-child(1)")
    AMOUNT = (By.CSS_SELECTOR, "td.ng-binding:nth-child(2)")
    TRANSACTION_TYPE = (By.CSS_SELECTOR, "td.ng-binding:nth-child(3)")
    BODY_TRANSACTION = (By.CSS_SELECTOR, "table.table.table-bordered.table-striped > tbody")
    ROWS = (By.CSS_SELECTOR, "tr[id^='anchor']")
    