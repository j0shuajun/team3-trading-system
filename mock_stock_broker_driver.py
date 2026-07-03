
class MockStockBrokerDriver():
    def __init__(self):
        self.login_id = ''
        self.login_password = ''

        self.buy_stock_code = ''
        self.buy_price = 0
        self.buy_quantity = 0

    def login(self, login_id, login_password):
        self.login_id = login_id
        self.login_password = login_password

    def buy(self, stock_code, price, quantity):
        self.buy_stock_code = stock_code
        self.buy_price = price
        self.buy_quantity = quantity

    def sell(self, stock_code, price, quantity):
        pass

    def set_prices(self, stock_code, prices):
        pass
