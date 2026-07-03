
class Stock:
    def __init__(self, stock_code='', prices=None):
        self.stock_code = stock_code
        self.prices = prices

class MockStockBrokerDriver():
    def __init__(self):
        self.login_id = ''
        self.login_password = ''

        self.buy_stock_code = ''
        self.buy_price = 0
        self.buy_quantity = 0

        self.sell_stock_code = ''
        self.sell_price = 0
        self.sell_quantity = 0

        self.stocks = []

    def login(self, login_id, login_password):
        self.login_id = login_id
        self.login_password = login_password

    def buy(self, stock_code, price, quantity):
        self.buy_stock_code = stock_code
        self.buy_price = price
        self.buy_quantity = quantity

    def sell(self, stock_code, price, quantity):
        self.sell_stock_code = stock_code
        self.sell_price = price
        self.sell_quantity = quantity

    def set_prices(self, stock_code, prices):
        self.stocks.append(Stock(stock_code, prices))

    def get_price(self, stock_code):
        for stock in self.stocks:
            if stock.stock_code == stock_code:
                return stock.prices.pop(0)

        return 0