from abc import ABC, abstractmethod


class StockBrokerDriver(ABC):

    @abstractmethod
    def login(self, user_id: str, password: str) -> None:
        pass

    @abstractmethod
    def buy(self, stock_code: str, price: int, quantity: int) -> None:
        pass

    @abstractmethod
    def sell(self, stock_code: str, price: int, quantity: int) -> None:
        pass

    @abstractmethod
    def get_price(self, stock_code: str) -> int:
        pass