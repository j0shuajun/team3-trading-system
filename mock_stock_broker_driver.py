
class MockStockBrokerDriver():
    def __init__(self):
        self.login_id = ""
        self.login_password = ""

    def login(self, login_id, login_password):
        self.login_id = login_id
        self.login_password = login_password
