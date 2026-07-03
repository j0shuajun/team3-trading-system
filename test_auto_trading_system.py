from auto_trading_system import AutoTradingSystem
from mock_stock_broker_driver import MockStockBrokerDriver, Stock


def test_login(mocker):
    mock_login = mocker.patch('mock_stock_broker_driver.MockStockBrokerDriver.login')
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    system.login("user.id", "password")

    mock_login.assert_called_once_with("user.id", "password")


def test_select_stock_broker():
    system = AutoTradingSystem()

    system.select_stock_broker("mock")

    assert isinstance(system.stock_broker_driver, MockStockBrokerDriver)


def test_buy_stock(mocker):
    mock_buy = mocker.patch('mock_stock_broker_driver.MockStockBrokerDriver.buy')
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    system.buy("005930", 70000, 3)

    mock_buy.assert_called_once_with("005930", 70000, 3)


def test_sell_stock(mocker):
    mock_sell = mocker.patch('mock_stock_broker_driver.MockStockBrokerDriver.sell')
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    system.sell("000660", 180000, 2)

    mock_sell.assert_called_once_with("000660", 180000, 2)

def test_get_price(mocker):
    mocker.patch(
        'mock_stock_broker_driver.MockStockBrokerDriver.get_price',
        return_value=70000
    )
    system = AutoTradingSystem()
    system.select_stock_broker("mock")

    price = system.get_price("005930")

    assert price == 70000
