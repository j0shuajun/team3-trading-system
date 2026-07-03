class AutoTradingSystem:
    def __init__(self):
        self._stocker_broker = None

    def select_stocker_broker(self, name:str):
        ...

    def login(self, id:str, pw:str):
        ...

    def buy(self, code:str, price:str, cnt:str):
        ...

    def sell(self, code:str, price:str, cnt:str):
        ...

    def get_price(self, code:str):
        ...
