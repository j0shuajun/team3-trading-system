from auto_trading_system import AutoTradingSystem
# from mock_stock_broker_driver import MockStockBrokerDriver


def test_login(mocker):
    driver = mocker.Mock()
    system = AutoTradingSystem()

    system.select_stock_broker(driver)
    system.login("user.id", "password")

    assert driver.login_id == "user.id"
    assert driver.login_password == "password"


def test_select_stock_broker(mocker):
    driver = mocker.Mock()
    system = AutoTradingSystem()

    system.select_stock_broker(driver)

    assert system.stock_broker_driver == driver


def test_buy_stock(mocker):
    driver = mocker.Mock()
    system = AutoTradingSystem()

    system.select_stock_broker(driver)
    system.buy("005930", 70000, 3)

    assert driver.buy_stock_code == "005930"
    assert driver.buy_price == 70000
    assert driver.buy_quantity == 3


def test_sell_stock(mocker):
    driver = mocker.Mock()
    system = AutoTradingSystem()

    system.select_stock_broker(driver)
    system.sell("000660", 180000, 2)

    assert driver.sell_stock_code == "000660"
    assert driver.sell_price == 180000
    assert driver.sell_quantity == 2


def test_get_price(mocker):
    driver = mocker.Mock()
    system = AutoTradingSystem()
    driver.set_prices("005930", [70000])

    system.select_stock_broker(driver)
    price = system.get_price("005930")

    assert price == 70000
