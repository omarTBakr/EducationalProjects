class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def to_dictionary(self):
        return vars(self)

    def __repr__(self):
        string = ', '.join([f'{key} = {value}'
                           for key ,value in self.to_dictionary().items()])

        return f'Stock( {string} )'


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def to_dictionary(self):
        return vars(self)

    def __repr__(self):
        string = ', '.join([f'{key} = {value}'
                           for key, value in self.to_dictionary().items()])

        return f'Trade ({string} )'
