import time


class AutoTradingSystem:
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