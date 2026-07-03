import time
from enum import Enum

from mock_stock_broker_driver import MockStockBrokerDriver


class StocBroker(Enum):
    KiwerStock = "kiwer"
    NemoStock = "nemo"
    MockStock = "mock"


class AutoTradingSystem:
    def __init__(self):
        self._stock_broker = None

    @property
    def stock_broker_driver(self):
        return self._stock_broker

    def select_stock_broker(self, name: str):
        if name == StocBroker.KiwerStock.value:
            pass
        if name == StocBroker.NemoStock.value:
            pass
        if name == StocBroker.MockStock.value:
            self._stock_broker = MockStockBrokerDriver()

    def login(self, id: str, pw: str):
        if len(id) == 0 or len(pw) == 0:
            raise ValueError

        print(f"{id} 로그인 시도..")
        return self._stock_broker.login(id, pw)

    def buy(self, code: str, price: int, cnt: int):
        if len(code) == 0 or price <= 0 or cnt <= 0:
            raise ValueError

        print(f"{code} 종목 {price}원*{cnt}주 매수 시도..")
        return self._stock_broker.buy(code, price, cnt)

    def sell(self, code: str, price: int, cnt: int):
        if len(code) == 0 or price <= 0 or cnt <= 0:
            raise ValueError

        print(f"{code} 종목 {price}원*{cnt}주 매도 시도..")
        return self._stock_broker.sell(code, price, cnt)

    def get_price(self, code: str):
        if len(code) == 0:
            raise ValueError

        print(f"{code} 종목 가격 확인..")
        return self._stock_broker.get_price(code)
      
    def buy_nice_timing(self, stock_code, amount):
        price = self._get_last_price_when_rising_or_fall_trend(stock_code, 'rising')
        if price is not None: self.buy(stock_code, price, amount // price)

    def sell_nice_timing(self, stock_code, quantity):
        price = self._get_last_price_when_rising_or_fall_trend(stock_code, 'fall')
        if price is not None: self.sell(stock_code, price, quantity)

    def _get_last_price_when_rising_or_fall_trend(self, stock_code, trend: str):
        price = self._stocker_broker.get_price(stock_code)
        for _ in range(2):
            current_price = self._stocker_broker.get_price(stock_code)
            if not self._is_rising_or_fall_trend(price, current_price, trend):
                return None
            price = current_price
            time.sleep(0.2)
        return price

    def _is_rising_or_fall_trend(self, prev_price, current_price, trend: str) -> bool:
        if trend == 'rising':
            return prev_price < current_price
        elif trend == 'fall':
            return prev_price > current_price
        return False
