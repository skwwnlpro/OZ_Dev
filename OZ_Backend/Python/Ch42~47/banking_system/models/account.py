from .transaction import Transaction
from utils.decorators import validate_transaction
from utils.exceptions import InsufficientFundsError, NegativeAmountError


class Account:

    bank_name = "K Bank"

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name

    def __init__(self) -> None:
        self.__balance = 0
        self.transactions = []

    @validate_transaction
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        self.transactions.append(Transaction("입금", amount, self.__balance))
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        if amount > self.__balance:
            raise InsufficientFundsError()
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))

    def get_balance(self) -> int:
        return self.__balance

    def get_transactions(self) -> list:
        return self.transactions
