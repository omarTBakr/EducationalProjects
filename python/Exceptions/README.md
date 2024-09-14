# Exceptions 
Suppose we have a Widget online sales application. We want a base 
`WidgetException` class that we will use as the base class for all our custom 
exceptions we raise from our Widget application.

Furthermore, we have determined that we will need the following categories of exceptions:

1. Supplier exceptions
    1. Not manufactured anymore
    2. Production delayed
    3. Shipping delayed
    
2. Checkout exceptions
    1. Inventory type exceptions
        - out of stock
    2. Pricing exceptions
        - invalid coupon code
        - cannot stack coupons
Write an exception class hierarchy to capture this. 
In addition, we would like to implement the following functionality:

- implement separate internal error message and user error message
- implement an http status code associated to each exception type (keep it simple, use a 500 (server error) error for everything
except invalid coupon code, and cannot stack coupons, these can be 400 (bad request)
- implement a logging function that can be called to log the exception details, time it occurred, etc.
- implement a function that can be called to produce a json string containing the exception details you want to display to
your user (include http status code (e.g. 400), the user error message, etc)
- implement a function that logs the traceback of the exception
## my approach 
1. make  base class (root) for all exceptions
```python 
from http import HTTPStatus
import json
import logging

# configurations for debugging  
logging.basicConfig(level = 'DEBUG' , filename='debugging.log' ,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
class WidgetException( Exception):

    """ base exception class for our Widget store"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_error_message = " API exception occurred"
    user_error_message = " we are sorry , An unexpected error occurred"

    def __init__(self , *args, user_error_message=None):
        if args:
            self.internal_error_message = args[0]
            super().__init__(*args)

        else :
            super().__init__(user_error_message)

        if user_error_message is not None:
            self.user_error_message = user_error_message

    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_error_message}
        return json.dumps(err_object)

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_error_message,
            "args": self.args[1:]
        }
        logging.error(exception)

```
2. make the hierarchy  as needed  like below 

```python 

class SupplierException(WidgetException):
    pass

class NotManufacturedException(SupplierException):
    pass

class ProductionDelayedException(SupplierException):
    pass

class ShippingDelayedException(SupplierException):
    pass


class CheckoutException(WidgetException):
    pass

class InventoryException(CheckoutException):
    pass

class OutOfStockException(InventoryException):
    pass

class PricingException(CheckoutException):
    http_status = HTTPStatus.BAD_REQUEST

class InvalidCouponException(PricingException):
    pass

class CannotStackCouponsException(PricingException):
    pass
```

3. check if everything is working as expected 
```python 
if __name__ == '__main__':
    try:
        raise InventoryException('inventory is empty')

    except InventoryException as exp:
        print(exp.to_json())
        exp.log_exception()

```
4. logging the traceback
you can use `traceback.TracebackException`[here is a link](https://docs.python.org/3/library/traceback.html#tracebackexception-objects)
```python
from traceback import TracebackException
  def log_trace_back(self):
        exp = TracebackException.from_exception(self)
        # lst = exp.format(chain= True)
        joined = ' '.join(exp.format(chain= True ))
        logging.debug(joined)
```
 
