from auto_trading_system import AutoTradingSystem
from mock_stock_broker_driver import MockStockBrokerDriver


def test_login():
    system = AutoTradingSystem()

    system.select_stock_broker("mock")
    system.login("user.id", "password")

    driver = system.stock_broker_driver
    assert driver.login_id == "user.id"
    assert driver.login_password == "password"


def test_select_stock_broker():
    system = AutoTradingSystem()

    system.select_stock_broker("mock")

    assert isinstance(system.stock_broker_driver, MockStockBrokerDriver)


def test_buy_stock():
    system = AutoTradingSystem()

    system.select_stock_broker("mock")
    system.buy("005930", 70000, 3)

    driver = system.stock_broker_driver
    assert driver.buy_stock_code == "005930"
    assert driver.buy_price == 70000
    assert driver.buy_quantity == 3


def test_sell_stock():
    system = AutoTradingSystem()

    system.select_stock_broker("mock")
    system.sell("000660", 180000, 2)

    driver = system.stock_broker_driver
    assert driver.sell_stock_code == "000660"
    assert driver.sell_price == 180000
    assert driver.sell_quantity == 2


def test_get_price():
    system = AutoTradingSystem()

    system.select_stock_broker("mock")
    system.stock_broker_driver.set_prices("005930", [70000])
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
