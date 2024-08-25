## Simple Banking System  

This project is a basic implementation of a banking system in Python. It's designed to be easy to understand for beginner programmers, introducing concepts like:

* **Classes and Objects:** Learn how to model real-world entities (like bank accounts) using code.
* **Attributes and Methods:** Understand how objects have properties (balance, name) and actions (deposit, withdraw).
* **Error Handling:** See how to use `TypeError` and `ValueError` to prevent invalid operations.
* **Properties and Setters:** Learn how to control access to object attributes using properties.
* **Static Variables and Methods:** Understand how to share data and behavior across all instances of a class.
* **Datetime and Timezones:** Work with dates, times, and different time zones. 
* **Unit Testing:**  This project includes unit tests for the two main classes which are `TimeZone` and `Account`.

## problem statement 
We need to design and implement a class that will be used to represent bank accounts.

We want the following functionality and characteristics:

accounts are uniquely identified by an account number (assume it will just be passed in the initializer)
account holders have a first and last name
accounts have an associated preferred time zone offset (e.g. -7 for MST)
balances need to be zero or higher, and should not be directly settable.
but, deposits and withdrawals can be made (given sufficient funds)
if a withdrawal is attempted that would result in nagative funds, the transaction should be declined.
a monthly interest rate exists and is applicable to all accounts uniformly. There should be a method that can be called to calculate
the interest on the current balance using the current interest rate, and add it to the balance. 
for more indepth check[this link](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2003%20-%20Project%201/01%20-%20Project%201.ipynb)
__,but you can assume any missing information__
## my approach 

**Project Structure:**

* **account.py:** Contains the `Account` class, which represents a bank account and its functionalities.
* **TimeZone.py:** Contains the `TimeZone` class, which contains timezone information like `offset_hours`, `offset_minutes`.

**Steps**


1. **Create an Account:**
   ```python
   from account import Account

   # Example:
   my_account = Account("John", "Doe", 1000, "1234567890", timezone.utc)
   ```

2. **Perform Operations:**
   ```python
   my_account.deposit(500)         # Deposit money
   my_account.withdraw(200)        # Withdraw money
   print(my_account.balance)      # Check balance
   print(my_account.full_name)    # Get account holder's full name
   ```
3. **make a `TimeZone` class** that has the following attributes
   1. name 
   2. offset hours 
   3. offset minutes 
4. **make a unit test for each functinoality**
```python
from Account import Account
import unittest

class TestTimeZone(unittest.TestCase):
    def test_initialization(self):
       
    def test_float_offset_minutes(self):

    def test_offset_minutes_beyond_range(self):
       
    def test_invalid_offset_hours(self):

    def test_equality(self):

    def test_inequality_name(self):

    def test_inequality_hours(self):
   
    def test_inequality_minute(self):
      

class TestAccount(unittest.TestCase):


    def test_initialization(self):
  
    def test_deposit(self):

    def negative_balance_initialization(self):
 
    def test_negative_deposit(self):
         
    def test_negative_withdraw(self):
        
    def test_excessive_withdraw(self):

    def test_withdraw(self):
        

```

**Running the Unit Tests:**

```bash
python -m unittest   
```

## Area for improvements
1.  make a root class for all errors  and instantiate all errors from it 
2. more testing for the return of `deposit` , `add_interest` , `with_draw`
3. consistency with using either`float` or `decimal` accross the whole class 
4. more unittests for `TimeZone` class .