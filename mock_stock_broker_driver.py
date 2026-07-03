class Stock:
    def __init__(self, stock_code, price, quantity):
        self.stock_code = stock_code
        self.price = price
        self.quantity = quantity


class MockStockBrokerDriver:
    def login(self, id: str, pw: str):
        ...

    def buy(self, stock_code, price, cnt):
        ...

    def sell(self, stock_code, price, cnt):
        ...

    def get_price(self, stock_code):
        ...
