from auto_trading_system import AutoTradingSystem
from mock_stock_broker_driver import MockStockBrokerDriver


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


def test_buy_nice_timing(mocker):
    sleep = mocker.patch("auto_trading_system.time.sleep")
    system = AutoTradingSystem()

    system.select_stock_broker("mock")
    get_price = mocker.patch.object(
        system.stock_broker_driver,
        "get_price",
        side_effect=[1000, 1100, 1200],
    )
    system.buy_nice_timing("005930", 5000)

    driver = system.stock_broker_driver
    assert get_price.call_count == 3
    assert driver.buy_stock_code == "005930"
    assert driver.buy_price == 1200
    assert driver.buy_quantity == 4
    assert sleep.call_count == 2


def test_sell_nice_timing(mocker):
    sleep = mocker.patch("auto_trading_system.time.sleep")
    system = AutoTradingSystem()

    system.select_stock_broker("mock")
    get_price = mocker.patch.object(
        system.stock_broker_driver,
        "get_price",
        side_effect=[1200, 1100, 1000],
    )
    system.sell_nice_timing("005930", 3)

    driver = system.stock_broker_driver
    assert get_price.call_count == 3
    assert driver.sell_stock_code == "005930"
    assert driver.sell_price == 1000
    assert driver.sell_quantity == 3
    assert sleep.call_count == 2
