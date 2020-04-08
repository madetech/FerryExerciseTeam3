import pytest

from .ferry import Ferry

@pytest.fixture
def ferry():
    price = 25
    load = 1
    return Ferry(load, price)


def test_can_create_ferry(ferry):
    print(ferry)

def test_ferry_has_load(ferry):
    ferry.load

def test_ferry_has_price():
    ferry.price
