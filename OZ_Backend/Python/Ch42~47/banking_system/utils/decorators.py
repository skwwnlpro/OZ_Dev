from utils.exceptions import NegativeAmountError


def validate_transaction(function: callable) -> callable:
    def wrapper(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError("금액은 0보다 커야 합니다.")
        return function(self, amount)

    return wrapper
