
class Stock:
    def __init__(self):
        self.stock_code = ''
        self.prices = []
        self.quantity = 0

    def set_stock(self, stock_code, prices, quantity):
        self.stock_code = stock_code
        self.quantity = quantity
        if isinstance(prices, list):
            self.prices = prices
        else:
            self.prices.append(prices)

    def get_stock_price(self):
        return self.prices.pop(0)


class MockStockBrokerDriver():
    def __init__(self):
        self.login_id = ''
        self.login_password = ''
        self.stocks = []

    def login(self, login_id, login_password):
        self.login_id = login_id
        self.login_password = login_password

    def buy(self, stock_code, price, quantity):
        stock = Stock()
        stock.set_stock(stock_code, price, quantity)
        return stock

    def sell(self, stock_code, price, quantity):
        stock = Stock()
        stock.set_stock(stock_code, price, quantity)
        return stock

    def set_prices(self, stock_code, prices):
        stock = Stock()
        stock.set_stock(stock_code, prices, 0)
        self.stocks.append(stock)

    def get_price(self, stock_code):
        for stock in self.stocks:
            if stock.stock_code == stock_code:
                return stock.prices.pop(0)

        return 0