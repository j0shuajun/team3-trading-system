# test_mock_stock_broker_driver.py

from mock_stock_broker_driver import MockStockBrokerDriver


def test_login():
    driver = MockStockBrokerDriver()

    driver.login("user.id", "sk-1234")

    assert driver.login_id == "user.id"
    assert driver.login_password == "sk-1234"


def test_buy_request():
    driver = MockStockBrokerDriver()

    driver.buy("005930", 70000, 3)

    assert driver.buy_stock_code == "005930"
    assert driver.buy_price == 70000
    assert driver.buy_quantity == 3


def test_sell_request():
    driver = MockStockBrokerDriver()

    driver.sell("000660", 180000, 2)

    assert driver.sell_stock_code == "000660"
    assert driver.sell_price == 180000
    assert driver.sell_quantity == 2


def test_get_price():
    driver = MockStockBrokerDriver()

    driver.set_prices("005930", [70000, 71000, 72000])

    assert driver.get_price("005930") == 70000
    assert driver.get_price("005930") == 71000
    assert driver.get_price("005930") == 72000
