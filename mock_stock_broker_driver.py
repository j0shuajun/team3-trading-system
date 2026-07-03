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
        stock = Stock()
        stock.set_stock('005930', [70000, 71000, 72000], 0)
        self.stocks = [stock]

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

    def find_stock(self, stock_code):
        for stock in self.stocks:
            if stock.stock_code == stock_code:
                return stock
        return None

    def set_prices(self, stock_code, prices):
        stock = self.find_stock(stock_code)
        if stock is not None:
            stock.set_stock(stock_code, prices, 0)
            return

        stock = Stock()
        stock.set_stock(stock_code, prices, 0)
        self.stocks.append(stock)

    def get_price(self, stock_code):
        stock = self.find_stock(stock_code)
        if stock is not None:
                return stock.prices.pop(0)

        return 0
