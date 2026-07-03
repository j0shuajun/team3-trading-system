import time

from stub_auto_trading_system import StubAutoTradingSystem


class AutoTradingSystem(StubAutoTradingSystem):
    def buy_nice_timing(self, stock_code, amount):
        price = self._get_last_price_when_rising_or_fall_trend(stock_code, 'rising')
        if price is not None: self.buy(stock_code, price, amount // price)

    def sell_nice_timing(self, stock_code, quantity):
        price = self._get_last_price_when_rising_or_fall_trend(stock_code, 'fall')
        if price is not None: self.sell(stock_code, price, quantity)

    def _get_last_price_when_rising_or_fall_trend(self, stock_code, trend: str) -> int:
        price = self._stocker_broker.get_price(stock_code)
        for _ in range(2):
            current_price = self._stocker_broker.get_price(stock_code)
            if trend == "rising" and price >= current_price:
                return
            if trend == "fall" and price <= current_price:
                return
            price = current_price
            time.sleep(0.2)
        return price