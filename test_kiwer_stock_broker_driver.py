from kiwer_stock_broker_driver import KiwerStockBrokerDriver
from stock_broker_driver import StockBrokerDriver


def test_kiwer_driver_follows_stock_broker_driver_interface():
    driver = KiwerStockBrokerDriver()

    assert isinstance(driver, StockBrokerDriver)


def test_kiwer_driver_login(mocker):
    api = mocker.patch("kiwer_stock_broker_driver.KiwerAPI").return_value
    driver = KiwerStockBrokerDriver()

    driver.login("user.id", "password")

    api.login.assert_called_once_with("user.id", "password")


def test_kiwer_driver_buy(mocker):
    api = mocker.patch("kiwer_stock_broker_driver.KiwerAPI").return_value
    driver = KiwerStockBrokerDriver()

    driver.buy("005930", 70000, 3)

    api.buy.assert_called_once_with("005930", 3, 70000)


def test_kiwer_driver_sell(mocker):
    api = mocker.patch("kiwer_stock_broker_driver.KiwerAPI").return_value
    driver = KiwerStockBrokerDriver()

    driver.sell("005930", 70000, 3)

    api.sell.assert_called_once_with("005930", 3, 70000)


def test_kiwer_driver_get_price(mocker):
    api = mocker.patch("kiwer_stock_broker_driver.KiwerAPI").return_value
    api.current_price.return_value = 70000
    driver = KiwerStockBrokerDriver()

    price = driver.get_price("005930")

    assert price == 70000
    api.current_price.assert_called_once_with("005930")
