# custom exceptions
class InsufficientBalanceError(Exception):
    pass
balance=5000
withdraw_amount=7000
try:
    if withdraw_amount>balance:
        raise InsufficientBalanceError('Insufficient account balance')
    balance-=withdraw_amount
except InsufficientBalanceError as ex:
    print('Transaction failed: ',ex)