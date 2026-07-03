from mock_stock_broker_driver import MockStockBrokerDriver
from stock_broker_driver import StockBrokerDriver


def test_stock_broker_driver_has_login():
    assert hasattr(StockBrokerDriver, "login")


def test_stock_broker_driver_has_buy():
    assert hasattr(StockBrokerDriver, "buy")


def test_stock_broker_driver_has_sell():
    assert hasattr(StockBrokerDriver, "sell")


def test_stock_broker_driver_has_get_price():
    assert hasattr(StockBrokerDriver, "get_price")


def test_mock_driver_follows_stock_broker_driver_interface():
    driver = MockStockBrokerDriver()

    assert isinstance(driver, StockBrokerDriver)
