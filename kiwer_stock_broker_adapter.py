from stock_broker_driver import StockBrokerDriver
from kiwer_api import KiwerAPI


class KiwerStockBrokerAdapter(StockBrokerDriver):
    def __init__(self):
        self.api = KiwerAPI()

    def login(self, user_id: str, password: str) -> None:
        self.api.login(user_id, password)

    def buy(self, stock_code: str, price: int, quantity: int) -> None:
        self.api.buy(stock_code, quantity, price)

    def sell(self, stock_code: str, price: int, quantity: int) -> None:
        self.api.sell(stock_code, quantity, price)

    def get_price(self, stock_code: str) -> int:
        return self.api.current_price(stock_code)