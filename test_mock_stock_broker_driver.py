# test_mock_stock_broker_driver.py

from mock_stock_broker_driver import MockStockBrokerDriver


def test_login():
    driver = MockStockBrokerDriver()

    driver.login("user.id", "sk-1234")

    assert driver.login_id == "user.id"
    assert driver.login_password == "sk-1234"


def test_buy_request():
    driver = MockStockBrokerDriver()
    stock = driver.buy("005930", 70000, 3)

    assert stock.stock_code == "005930"
    assert stock.get_stock_price() == 70000
    assert stock.quantity == 3


def test_sell_request():
    driver = MockStockBrokerDriver()
    stock = driver.sell("000660", 180000, 2)

    assert stock.stock_code == "000660"
    assert stock.get_stock_price() == 180000
    assert stock.quantity == 2

def test_set_price():
    driver = MockStockBrokerDriver()
    driver.set_prices("005930", 73000)

    assert driver.get_price("005930") == 70000
    assert driver.get_price("005930") == 71000
    assert driver.get_price("005930") == 72000
    assert driver.get_price("005930") == 73000

def test_get_price():
    driver = MockStockBrokerDriver()

    assert driver.get_price("005930") == 70000
    assert driver.get_price("005930") == 71000
    assert driver.get_price("005930") == 72000
