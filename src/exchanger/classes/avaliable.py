class Avaliable:

    def __init__(self, currency, available: float):
        self.currency = currency
        self.available = available

    def __str__(self):
        return f'{self.currency}{self.available}'