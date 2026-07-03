class Stock:
    def __init__(self, stock_code, price, quantity):
        self.stock_code = stock_code
        self.quantity = quantity
        self.price = price

class MockStockBrokerDriver():
    def __init__(self):
        self.login_id = ''
        self.login_password = ''
        self.user_stocks = []

        self.stocks = []
        self.stocks.append(Stock('005930', 70000, 0))
        self.stocks.append(Stock('005930', 71000, 0))
        self.stocks.append(Stock('005930', 72000, 0))

    def login(self, login_id, login_password):
        self.login_id = login_id
        self.login_password = login_password

    def buy(self, stock_code, price, quantity):
        stock = Stock(stock_code, price, quantity)
        self.user_stocks.append(stock)
        return stock

    def sell(self, stock_code, price, quantity):
        stock = self.find_stock(self.user_stocks, stock_code)
        if stock is not None:
            self.user_stocks.remove(stock)
            return stock
        return None

    def find_stock(self, stocks, stock_code):
        for stock in stocks:
            if stock.stock_code == stock_code:
                return stock
        return None

    def set_prices(self, stock_code, price):
        stock = self.find_stock(self.stocks, stock_code)
        if stock is not None:
            stock.price = price
            return

        self.stocks.append(Stock(stock_code, price, 0))

    def get_price(self, stock_code):
        stock = self.find_stock(self.stocks, stock_code)
        if stock is not None:
            return stock.price

        return 0
