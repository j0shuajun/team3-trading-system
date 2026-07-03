from unittest.mock import Mock

from stock_broker_driver import StockBrokerDriver
from kiwer_stock_broker_adapter import KiwerStockBrokerAdapter
from nemo_stock_broker_adapter import NemoStockBrokerAdapter


def test_stock_broker_driver_has_login():
    assert hasattr(StockBrokerDriver, "login")


def test_stock_broker_driver_has_buy():
    assert hasattr(StockBrokerDriver, "buy")


def test_stock_broker_driver_has_sell():
    assert hasattr(StockBrokerDriver, "sell")


def test_stock_broker_driver_has_get_price():
    assert hasattr(StockBrokerDriver, "get_price")


def test_kiwer_adapter_is_stock_broker_driver():
    adapter = KiwerStockBrokerAdapter()

    assert isinstance(adapter, StockBrokerDriver)


def test_nemo_adapter_is_stock_broker_driver():
    adapter = NemoStockBrokerAdapter()

    assert isinstance(adapter, StockBrokerDriver)


def test_kiwer_adapter_login_calls_kiwer_api_login():
    adapter = KiwerStockBrokerAdapter()
    adapter.api = Mock()

    adapter.login("user.id", "sk-1234")

    adapter.api.login.assert_called_once_with("user.id", "sk-1234")


def test_kiwer_adapter_buy_calls_kiwer_api_buy_with_changed_order():
    adapter = KiwerStockBrokerAdapter()
    adapter.api = Mock()

    adapter.buy("005930", 70000, 3)

    adapter.api.buy.assert_called_once_with("005930", 3, 70000)


def test_kiwer_adapter_sell_calls_kiwer_api_sell_with_changed_order():
    adapter = KiwerStockBrokerAdapter()
    adapter.api = Mock()

    adapter.sell("005930", 71000, 2)

    adapter.api.sell.assert_called_once_with("005930", 2, 71000)


def test_kiwer_adapter_get_price_returns_current_price():
    adapter = KiwerStockBrokerAdapter()
    adapter.api = Mock()
    adapter.api.current_price.return_value = 70000

    result = adapter.get_price("005930")

    assert result == 70000
    adapter.api.current_price.assert_called_once_with("005930")


def test_nemo_adapter_login_calls_nemo_api_cerification():
    adapter = NemoStockBrokerAdapter()
    adapter.api = Mock()

    adapter.login("user.id", "sk-1234")

    adapter.api.cerification.assert_called_once_with("user.id", "sk-1234")


def test_nemo_adapter_buy_calls_nemo_api_purchasing_stock():
    adapter = NemoStockBrokerAdapter()
    adapter.api = Mock()

    adapter.buy("005930", 70000, 3)

    adapter.api.purchasing_stock.assert_called_once_with("005930", 70000, 3)


def test_nemo_adapter_sell_calls_nemo_api_selling_stock():
    adapter = NemoStockBrokerAdapter()
    adapter.api = Mock()

    adapter.sell("005930", 71000, 2)

    adapter.api.selling_stock.assert_called_once_with("005930", 71000, 2)


def test_nemo_adapter_get_price_returns_market_price():
    adapter = NemoStockBrokerAdapter()
    adapter.api = Mock()
    adapter.api.get_market_price.return_value = 70000

    result = adapter.get_price("005930")

    assert result == 70000
    adapter.api.get_market_price.assert_called_once_with("005930", 0)


