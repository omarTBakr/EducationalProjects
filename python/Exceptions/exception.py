from http import HTTPStatus
import json
import logging
from traceback import TracebackException

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


    def log_trace_back(self):
        exp = TracebackException(exc_type= type(self)  ,
                                 exc_value= self ,
                                exc_traceback = self.__traceback__
                                    )
        lst = exp.format(chain= True)
        joined = ' '.join(list(lst))
        logging.debug(joined)
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




if __name__ == '__main__':
    try:
        raise InventoryException('inventory is empty')

    except InventoryException as exp:
        print(exp.to_json())
        exp.log_exception()
        exp.log_trace_back()
