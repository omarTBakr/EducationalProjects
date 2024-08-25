
from Account import Account
from TimeZone import TimeZone
import unittest

class TestTimeZone(unittest.TestCase):
    def test_initialization(self):
        name  , offset_hours , offset_minutes = ' ABC' , 4 ,3
        timezone = TimeZone(name, offset_hours, offset_minutes)

        self.assertEqual(name.strip() , timezone.name)
        self.assertEqual(offset_hours, timezone._offset_hours)
        self.assertEqual(offset_minutes , timezone._offset_minutes)

    def test_float_offset_minutes(self):
        name  , offset_hours , offset_minutes = ' ABC' , 4 ,3.8
        self.assertRaises(ValueError,TimeZone , name , offset_hours, offset_minutes)

    def test_offset_minutes_beyond_range(self):
        name, offset_hours, offset_minutes = ' ABC', 4, 120
        self.assertRaises(ValueError, TimeZone, name, offset_hours, offset_minutes)


    def test_invalid_offset_hours(self):
        name, offset_hours, offset_minutes = ' ABC', 20, 0
        self.assertRaises(ValueError, TimeZone, name, offset_hours, offset_minutes)


    def test_equality(self):
        first = TimeZone('ABC ', 1  ,1)
        second = TimeZone(' ABC' , 1  ,1)
        self.assertEqual(first, second)

    def test_inequality_name(self):
        first = TimeZone('ABC z', 1, 1)
        second = TimeZone(' ABC', 1, 1)
        self.assertNotEqual(first, second)

    def test_inequality_hours(self):
        first = TimeZone('ABC z', 3, 1)
        second = TimeZone(' ABC', 1, 1)
        self.assertNotEqual(first, second)


    def test_inequality_minute(self):
        first = TimeZone('ABC z', 1, 44)
        second = TimeZone(' ABC', 1, 1)
        self.assertNotEqual(first, second)

class TestAccount(unittest.TestCase):


    def test_initialization(self):
        first_name, last_name, balance, account_number = 'omar', 'bakr', 1000, 1234
        account = Account(first_name, last_name, balance, account_number)
        # check each parameter of the initialization
        self.assertEqual(account.full_name , f'{first_name} {last_name}')
        self.assertEqual(account.balance , balance)
        self.assertEqual(account.account_number , account_number)

    def test_deposit(self):

        first_name , last_name , balance , account_number = 'omar', 'bakr', 1000, 1234
        account = Account(first_name , last_name ,balance, account_number)
        amount = 199
        account.deposit(amount)
        balance += amount
        self.assertEqual( account.balance , balance)

    def negative_balance_initialization(self):

        '''
        Tests initializing balance with negtive number
        '''

        first_name, last_name, balance, account_number = 'omar', 'bakr', -1000, 1234
        # Account(first_name, last_name, balance, account_number)

        self.assertRaises(ValueError , Account , first_name, last_name, balance, account_number)

    def test_negative_deposit(self):
        first_name, last_name, balance, account_number = 'omar', 'bakr', 1000, 1234
        account = Account(first_name, last_name, balance, account_number)
        amount = -199

        self.assertRaises(ValueError, account.deposit , amount)


    def test_negative_withdraw(self):
        '''
        Test negative withdraw
        '''
        first_name, last_name, balance, account_number = 'omar', 'bakr', 1000, 1234
        account = Account(first_name, last_name, balance, account_number)
        amount = -199

        self.assertRaises(ValueError, account.withdraw, amount)

    def test_excessive_withdraw(self):
        '''
         test , with draw more than the maximum capacity of the account.
        '''
        first_name, last_name, balance, account_number = 'omar', 'bakr', 1000, 1234
        account = Account(first_name, last_name, balance, account_number)
        amount = 2000

        self.assertRaises(ValueError, account.withdraw, amount)

    def test_withdraw(self):
        first_name, last_name, balance, account_number = 'omar', 'bakr', 1000, 1234
        account = Account(first_name, last_name, balance, account_number)
        amount = 199
        account.withdraw(amount)
        balance -= amount
        self.assertEqual(account.balance, balance  )


