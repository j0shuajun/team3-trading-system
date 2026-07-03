from stock_brocker_driver import StockBrockerDriver
from nemo_api import NemoAPI


class NemoStockBrokerDriver(StockBrockerDriver):
    def __init__(self):
        self.api = NemoAPI()

    def login(self, user_id: str, password: str) -> None:
        self.api.cerification(user_id, password)

    def buy(self, stock_code: str, price: int, quantity: int) -> None:
        self.api.purchasing_stock(stock_code, price, quantity)

    def sell(self, stock_code: str, price: int, quantity: int) -> None:
        self.api.selling_stock(stock_code, price, quantity)

    def get_price(self, stock_code: str) -> int:
        return self.api.get_market_price(stock_code, 0)


