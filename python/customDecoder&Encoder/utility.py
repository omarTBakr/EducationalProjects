import json
import re
from classes import Trade
from classes import Stock
from datetime import datetime ,date
from  decimal import Decimal

class CustomDecoder(json.JSONDecoder):
    # base_decoder = json.JSONDecoder(parse_float=Decimal)
    # or you can do it like this    def __init__(self,*args,**kwargs):
    # super().__init__()

    def decode(self, arg):
        data = json.loads(arg)
        return self.parse(data)
    def make_stock(self,obj):
        obj = Stock(
            obj['symbol'],
            datetime.strptime(obj['date'], '%Y-%m-%d').date(),
            Decimal(obj['open']),
            Decimal(obj['high']),
            Decimal(obj['low']),
            Decimal(obj['close']),
            int(obj['volume'])
        )
        return obj
    def make_trade(self,obj):
        obj = Trade(
            obj['symbol'],
            datetime.strptime(obj['timestamp'], '%Y-%m-%dT%H:%M:%S').date(),
            obj['order'],
            Decimal(obj['price']),
            Decimal(obj['commission']),
            obj['volume'])
        return obj

    def financial(self,obj):
        object_type = obj.get('object',None)
        if object_type == 'Trade':
            return self.make_trade(obj)
        elif object_type == 'Stock':
            return self.make_stock(obj)
        return obj

    def parse(self, obj):

        if isinstance(obj,dict):
            obj = self.financial(obj)
            # if the object still a dictionary
            # aka not either stock or trade
            if isinstance(obj,dict):
                for key , value in obj.items():
                    obj[key] = self.parse(value)
        elif isinstance(obj,list):
            for index, value in enumerate(obj):
                obj[index] = self.parse(value)

        return obj


##############################################################
from json import JSONEncoder


class CustomEncoder(JSONEncoder):

    def __init__(self, *args, **kwargs):
        # our default args
        kw = {'indent': 3, 'skipkeys': True, 'sort_keys': True,
              'allow_nan': False}
        # whatever conflict , update it
        kw.update(kwargs)

        super().__init__(*args, **kw)

    def default(self, arg):
        if (isinstance(arg, Stock) or
            isinstance(arg,Trade)):
            dictionary = arg.to_dictionary()
            dictionary['object'] = arg.__class__.__name__
            return dictionary

        elif isinstance(arg,Decimal):
            return str(arg)
        elif isinstance(arg, datetime):
            return arg.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(arg, date):
            return arg.strftime('%Y-%m-%d')

        super().default(arg)


