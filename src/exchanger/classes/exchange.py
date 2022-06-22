class Exchange:

    def __init__(self, ccy, base_ccy, buy: float, sale: float):
        self.ccy = ccy
        self.base_ccy = base_ccy
        self.buy = buy
        self.sale = sale

    def __str__(self):
        return f'{self.ccy}{self.base_ccy}{self.buy}{self.sale}'
