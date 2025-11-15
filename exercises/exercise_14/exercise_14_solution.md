# Exercise 14: Solution

## Code
```python
# Custom exception hierarchy
class BankException(Exception):
    """Base exception for banking operations."""
    pass


class InsufficientFundsError(BankException):
    """Raised when account has insufficient funds."""

    def __init__(self, account_number, balance, amount):
        self.account_number = account_number
        self.balance = balance
        self.amount = amount
        message = (f"Insufficient funds! Tried to withdraw ${amount} "
                   f"but only ${balance} available in account {account_number}")
        super().__init__(message)


class InvalidAmountError(BankException):
    """Raised when amount is invalid (negative or zero)."""

    def __init__(self, amount, operation):
        self.amount = amount
        self.operation = operation
        message = f"Invalid amount! Cannot {operation} ${amount}. Amount must be positive."
        super().__init__(message)


class AccountNotFoundError(BankException):
    """Raised when account doesn't exist."""

    def __init__(self, account_number):
        self.account_number = account_number
        message = f"Account {account_number} not found in the system"
        super().__init__(message)


# Banking class using custom exceptions
class BankAccount:
    """Bank account with custom exception handling."""

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into account."""
        if amount <= 0:
            raise InvalidAmountError(amount, "deposit")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount <= 0:
            raise InvalidAmountError(amount, "withdraw")
        if amount > self.balance:
            raise InsufficientFundsError(self.account_number, self.balance, amount)
        self.balance -= amount
        return self.balance


# Simulated account database
accounts = {}


def get_account(account_number):
    """Get account or raise exception."""
    if account_number not in accounts:
        raise AccountNotFoundError(account_number)
    return accounts[account_number]


# Demo
print("Creating account 1001 with balance $1000")
account = BankAccount(1001, 1000)
accounts[1001] = account

# Successful withdrawal
try:
    new_balance = account.withdraw(500)
    print(f"\nWithdrawal successful: $500")
    print(f"New balance: ${new_balance}")
except BankException as e:
    print(f"Error: {e}")

# Test insufficient funds
try:
    account.withdraw(600)
except InsufficientFundsError as e:
    print(f"\nError: {e}")

# Test invalid amount
try:
    account.deposit(-50)
except InvalidAmountError as e:
    print(f"\nError: {e}")

# Test account not found
try:
    get_account(9999)
except AccountNotFoundError as e:
    print(f"\nError: {e}")

# Exception chaining
print("\nException chaining:")
try:
    try:
        account.withdraw(1000)
    except InsufficientFundsError as e:
        raise Exception("Cannot complete withdrawal") from e
except Exception as e:
    print(f"Error processing transaction: {e.__cause__}")
    print(f"Caused by: {e}")
```

## Explanation

**Why Custom Exceptions?**

1. **Clarity**: `InsufficientFundsError` is clearer than generic `ValueError`
2. **Specific Handling**: Catch specific errors differently
3. **Context**: Store relevant data (account number, amount)
4. **Organization**: Group related errors in hierarchy

**Creating Custom Exceptions:**

```python
class MyException(Exception):
    def __init__(self, custom_data):
        self.custom_data = custom_data
        message = f"Error with {custom_data}"
        super().__init__(message)
```

Key points:
- Inherit from `Exception` or a more specific exception
- Add `__init__` to store custom attributes
- Call `super().__init__(message)` to set the error message

**Exception Hierarchy:**

```
Exception (built-in)
└── BankException (our base)
    ├── InsufficientFundsError
    ├── InvalidAmountError
    └── AccountNotFoundError
```

Benefits:
- Catch all bank errors: `except BankException:`
- Catch specific error: `except InsufficientFundsError:`
- Catch any error: `except Exception:`

**Raising Exceptions:**

```python
raise InsufficientFundsError(account_number, balance, amount)
```

Python creates the exception object and stops normal execution.

**Catching Specific Exceptions:**

Order matters! Specific exceptions before general:

```python
try:
    risky_operation()
except InsufficientFundsError as e:
    # Handle insufficient funds specifically
    print(f"Need ${e.amount - e.balance} more")
except BankException as e:
    # Handle other bank errors
    print(f"Bank error: {e}")
except Exception as e:
    # Handle any other error
    print(f"Unexpected error: {e}")
```

**Exception Attributes:**

Store useful information:
```python
except InsufficientFundsError as e:
    print(f"Account: {e.account_number}")
    print(f"Balance: {e.balance}")
    print(f"Attempted: {e.amount}")
```

**Exception Chaining:**

Show causality with `from`:
```python
try:
    do_something()
except OriginalError as e:
    raise NewError("Context") from e
```

Access with `e.__cause__`.

**Best Practices:**

1. **Specific Names**: `InsufficientFundsError` not `BankError1`
2. **Docstrings**: Document when exception is raised
3. **Hierarchy**: Group related exceptions
4. **Attributes**: Store relevant context
5. **Messages**: Make errors actionable
6. **Don't Overuse**: Only create when built-ins aren't suitable

**When to Create Custom Exceptions:**

- ✓ Domain-specific errors (banking, gaming, etc.)
- ✓ Need to store custom data
- ✓ Need to catch specific errors differently
- ✗ Built-in exception works fine (ValueError, TypeError, etc.)
- ✗ Simple scripts without complex error handling

## Key Concepts

1. **Custom Exceptions**: Application-specific error types
2. **Exception Hierarchy**: Organizing related exceptions
3. **Exception Attributes**: Storing error context
4. **Inheritance**: Building on Exception base class
5. **Specific Handling**: Catching different exceptions differently
6. **Exception Chaining**: Showing causality with `from`
7. **Error Messages**: Clear, actionable messages
