import time

from stub_auto_trading_system import StubAutoTradingSystem


class AutoTradingSystem(StubAutoTradingSystem):
    def buy_nice_timing(self, stock_code, amount):
        price = self._stocker_broker.get_price(stock_code)
        for _ in range(2):
            current_price = self._stocker_broker.get_price(stock_code)
            if price >= current_price:
                return
            price = current_price
            time.sleep(0.2)
        self.buy(stock_code, price, amount // price)

    def sell_nice_timing(self, stock_code, quantity):
        price = self._stocker_broker.get_price(stock_code)
        for _ in range(2):
            current_price = self._stocker_broker.get_price(stock_code)
            if price <= current_price:
                return
            price = current_price
            time.sleep(0.2)
        if price is not None: self.sell(stock_code, price, quantity)