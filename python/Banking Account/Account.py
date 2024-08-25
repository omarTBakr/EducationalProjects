from decimal import Decimal
from datetime import datetime, timezone, timedelta
from collections import namedtuple
from dateutil import parser
import itertools
from TimeZone import TimeZone

class Account:
    _INTEREST_RATE = Decimal('0.5')
    #TRANSACTION_NUMBER = 12335
    TRANSACTION_NUMBER = itertools.count(12345)
    TRANSACTION_CODES = {'deposit':'D' ,
                         'withdraw':'W' ,
                         'interest':'I' ,
                         'rejected' :'X'}

    def __init__(self, first, last,
                 balance, account_number,
                 time_zone=None):
        self.handle_name('first_name', first)
        self.handle_name('last_name', last)

        self.balance = Decimal(balance)
        self.account_number = account_number

        if time_zone is None:
            self._time_zone = TimeZone('UTC', 0 , 0)
        else:
            #use the setter to handle the checking
            self.time_zone = time_zone



    def handle_name(self, attribute_name, value):

        if not value.strip() or value.strip() is None:
            raise ValueError(f'{attribute_name} can not be empty')

        setattr(self, attribute_name , value.strip())
    @classmethod
    def get_interest_rate(cls):
        return cls._INTEREST_RATE


    @classmethod
    def set_interest_rate(cls, value):
        if value <=0:
            raise ValueError('interval must be positive')
        cls._INTEREST_RATE = value


    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        #check if it's instance of timezone
        if not isinstance(value,TimeZone):
            raise ValueError('TimeZone must be instance of TimeZone')
        self._time_zone = value

    @property
    def balance(self):
        return float(self._balance)

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('balance can not be negative.')

        self._balance = value

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'



    def return_confirmation(self, code):

        return (f'{code}-{self.account_number}-'
                f'{datetime.now().strftime("%Y%m%d%H%M%S")}-'
                f'{next(Account.TRANSACTION_NUMBER)}')

    def deposit(self, value):
        if value < 0:
            raise ValueError('deposit can not be negative.')

        self._balance += value

        return self.return_confirmation( Account.TRANSACTION_CODES['deposit'])

    def split_confirmation(self, confirmation_str):
        split = confirmation_str.split('-')
        Info = namedtuple('Info', 'transaction_id account_number datetime timezone  transition_id')

        parsed_date = parser.parse(split[2])
        timezone = self._time_zone
        transition_id = split[-1]
        return Info(split[0], split[1], parsed_date,
                    timezone, transition_id)

    def withdraw(self, amount):

        if amount < 0:
            raise ValueError('amount can not be negative')

        if amount > self._balance:
            raise ValueError(' amount can not be > balance')

        self._balance -= amount
        return self.return_confirmation( Account.TRANSACTION_CODES['withdraw'])

    def add_interest(self):
        self._balance += Account._INTEREST_RATE * self._balance
        return self.return_confirmation('I')


if __name__ == '__main__':
    account = Account('omar' , 'bakr' ,1000  , 123 , None)
    confirmation = account.deposit(190)
    print(confirmation)
    print(account.split_confirmation(confirmation))