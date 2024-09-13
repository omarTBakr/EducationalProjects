import enum


@enum.unique
class AppException(enum.Enum):
    def __new__(cls, code, type_, message):
        member= object.__new__(cls)
        member.code = code
        member._value_ = code
        member.message= message
        member.type = type_
        return member

    def throw(self , message =None):
        if message is None:
            raise self.type(self.message)

        raise self.type(message)

    # -----------------------------members----------------------------------
    Timeout = (100, TimeoutError, 'default time out error')
    Arithmetic = (200 , ArithmeticError , 'default arithmatic error')


if __name__ =='__main__':
    # accessing by the code
   AppException(100) # <AppException.Timeout: 100>

   print(list(AppException)) # listing all avialable exceptions



   try:
        AppException.Timeout.throw() # throw with the default message
   except TimeoutError as error:
       print('caught time out error', error)




   try:
       AppException.Arithmetic.throw('custom error message')

   except ArithmeticError as error:
        print('caught  arithmatic error', error)

