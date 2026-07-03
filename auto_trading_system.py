from enum import Enum


class StockerBroker(Enum):
    KiwerStock = "kiwer"
    NemoStock = "nemo"
    MockStock = "mock"


class AutoTradingSystem:
    def __init__(self):
        self._stocker_broker = None

    def select_stocker_broker(self, name: str):
        if name == StockerBroker.KiwerStock.value:
            pass
        if name == StockerBroker.NemoStock.value:
            pass
        if name == StockerBroker.MockStock.value:
            pass

    def login(self, id: str, pw: str):
        if len(id) == 0 or len(pw) == 0:
            raise ValueError

        print(f"{id} 로그인 시도..")

    def buy(self, code: str, price: int, cnt: int):
        if len(code) == 0 or price <= 0 or cnt <= 0:
            raise ValueError

        print(f"{code} 종목 {price}원*{cnt}주 매수 시도..")

    def sell(self, code: str, price: int, cnt: int):
        if len(code) == 0 or price <= 0 or cnt <= 0:
            raise ValueError

        print(f"{code} 종목 {price}원*{cnt}주 매도 시도..")

    def get_price(self, code: str):
        if len(code) == 0:
            raise ValueError

        print(f"{code} 종목 가격 확인..")
