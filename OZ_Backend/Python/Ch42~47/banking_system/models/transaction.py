class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:
        return (
            f"거래 유형: {self.transaction_type}\n"
            f"거래 금액: {self.amount}\n"
            f"거래 잔고: {self.balance}"
        )

    def to_tuple(self) -> tuple[str, int, int]:
        return self.transaction_type, self.amount, self.balance
