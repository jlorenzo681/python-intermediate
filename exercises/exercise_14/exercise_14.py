# Exercise 14: Custom Exceptions
# Objective: Create custom exception classes for better error handling

# Hints:
# - Inherit from Exception or specific exception type
# - Add __init__ to store custom attributes
# - Call super().__init__(message) for error message
# - Raise with: raise CustomException(args)
# - Catch specific exceptions before general ones
# - Use exception chaining: raise ... from ...

# Your code here:

class BankException(Exception):
    "Base exception for banking operations"
    pass


class InsufficientFundsError(BankException):
    "Raise when account has insufficient funds"
    def __init__(self, amount, balance, account_number):
        self.amount = amount
        self.balance = balance
        self.account_number= account_number
        message = (f'Error: Insufficient funds! Tried to withdraw ${amount} but only ${balance}' 
        f' available in account {account_number}')
        super().__init__(message)


class InvalidAmountError(BankException):
    "Raise when amount is invalid, 0 o or negative"
    def __init__(self, amount, operation):
        self.amount = amount
        self.operation = operation
        message = f'Error: Invalid amount! Cannot {operation} ${amount}. Amount must be positive.'
        super().__init__(message)


class AccountNotFoundError(BankException):
    "Raise when account doesn't exist"
    def __init__(self, account_number):
        self.account_number = account_number
        message = f'Account {account_number} not found in the system.'
        super().__init__(message)

class BankAccount:
    "Bank account with costum excepcion handling"
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount, "deposit")
        self.balance+=amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount, "withdraw")
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance, self.account_number)
        self.balance-= amount
        return self.balance
    
accounts = {}

def get_account(account_number):
    if account_number  not in accounts:
        raise AccountNotFoundError(account_number)
    return accounts[account_number]

print("Creating account 1001 with balance $1000")
account = BankAccount(1001, 1000)
accounts[1001] = account

try:
    new_balance = account.withdraw(500)
    print(f'Withdrawal successful: $500')
    print(f'New balance: ${new_balance}')
except BankException as e:
        print(f'Error: {e}')



try:
    account.withdraw(600)
except InsufficientFundsError as e:
    print(f'Error: {e}')




try:
    account.deposit(-50)
except InvalidAmountError as e:
    print(f'Error: {e}')




try:
    get_account(9999)
except AccountNotFoundError as e:
    print(f'Error: {e}')



print("Exception chaining: ")
try:
    try:
        account.withdraw(1000)
    except InsufficientFundsError as e:   
        raise Exception("Canot complete withdrawal") from e
except Exception as e:
    print(f'Error processing transaction: {e.__cause__}')
    print(f'Caused by {e}')
