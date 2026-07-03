from nemo_stock_broker_driver import NemoStockBrokerDriver
from stock_broker_driver import StockBrokerDriver


def test_nemo_driver_follows_stock_broker_driver_interface():
    driver = NemoStockBrokerDriver()

    assert isinstance(driver, StockBrokerDriver)


def test_nemo_driver_login(mocker):
    api = mocker.patch("nemo_stock_broker_driver.NemoAPI").return_value
    driver = NemoStockBrokerDriver()

    driver.login("user.id", "password")

    api.cerification.assert_called_once_with("user.id", "password")


def test_nemo_driver_buy(mocker):
    api = mocker.patch("nemo_stock_broker_driver.NemoAPI").return_value
    driver = NemoStockBrokerDriver()

    driver.buy("005930", 70000, 3)

    api.purchasing_stock.assert_called_once_with("005930", 70000, 3)


def test_nemo_driver_sell(mocker):
    api = mocker.patch("nemo_stock_broker_driver.NemoAPI").return_value
    driver = NemoStockBrokerDriver()

    driver.sell("005930", 70000, 3)

    api.selling_stock.assert_called_once_with("005930", 70000, 3)


def test_nemo_driver_get_price(mocker):
    api = mocker.patch("nemo_stock_broker_driver.NemoAPI").return_value
    api.get_market_price.return_value = 70000
    driver = NemoStockBrokerDriver()

    price = driver.get_price("005930")

    assert price == 70000
    api.get_market_price.assert_called_once_with("005930", 0)
