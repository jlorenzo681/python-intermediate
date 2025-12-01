# Exercise 14: Custom Exceptions SI

**Difficulty:** Advanced

## Objective
Create custom exception classes for better error handling in a banking application.

## Requirements
1. Create a base `BankException` class inheriting from Exception
2. Create specific exceptions: `InsufficientFundsError`, `InvalidAmountError`, `AccountNotFoundError`
3. Add custom attributes to exceptions (account number, amount, etc.)
4. Create a `BankAccount` class that raises these exceptions appropriately
5. Demonstrate exception chaining with `raise ... from ...`
6. Show how to catch specific vs general exceptions
7. Display helpful error messages with exception attributes

## Expected Output
```
Creating account 1001 with balance $1000

Withdrawal successful: $500
New balance: $500

Error: Insufficient funds! Tried to withdraw $600 but only $500 available in account 1001

Error: Invalid amount! Cannot deposit -$50. Amount must be positive.

Error: Account 9999 not found in the system

Exception chaining:
Error processing transaction: Insufficient funds! Tried to withdraw $1000 but only $500 available in account 1001
Caused by: Cannot complete withdrawal
```

## Hints
- Inherit from Exception or appropriate base exception
- Add `__init__` to store custom attributes
- Override `__str__` for custom error messages
- Raise exceptions: `raise CustomException("message")`
- Exception chaining: `raise NewException() from original_exception`
- Catch specific exceptions before general ones

## Key Concepts
- Custom exception classes
- Exception hierarchy
- Exception attributes
- Error messages
- Exception chaining
- Specific exception handling
