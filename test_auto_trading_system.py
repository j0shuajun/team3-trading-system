from auto_trading_system import AutoTradingSystem
from mock_stock_broker_driver import MockStockBrokerDriver, Stock


def test_login(mocker):
    mocker.patch(
        'mock_stock_broker_driver.MockStockBrokerDriver.login',
        return_value=True
    )
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    assert system.login("user.id", "password")


def test_select_stock_broker():
    system = AutoTradingSystem()

    system.select_stock_broker("mock")

    assert isinstance(system.stock_broker_driver, MockStockBrokerDriver)


def test_buy_stock(mocker):
    mocker.patch(
        'mock_stock_broker_driver.MockStockBrokerDriver.buy',
        return_value=Stock("005930", 70000, 3)
    )
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    stock = system.buy("005930", 70000, 3)

    assert stock.stock_code == "005930"
    assert stock.price == 70000
    assert stock.quantity == 3


def test_sell_stock(mocker):
    mocker.patch(
        'mock_stock_broker_driver.MockStockBrokerDriver.sell',
        return_value=Stock("000660", 180000, 2)
    )
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    stock = system.sell("000660", 180000, 2)

    assert stock.stock_code == "000660"
    assert stock.price == 180000
    assert stock.quantity == 2


def test_get_price(mocker):
    mocker.patch(
        'mock_stock_broker_driver.MockStockBrokerDriver.get_price',
        return_value=70000
    )
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    price = system.get_price("005930")

    assert price == 70000
