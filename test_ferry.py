import os
import pytest


from .ferry import Ferry, app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_calculate_trip_price_of_geese(client):
    rv = client.get('/_add_numbers?corn=1&price=0.25')
    assert rv.json['price'] == 0.25

@pytest.mark.parametrize("corn,geese,price,error",[
    [5,0,0.25,0],
    [5,2,0.25,1],
    [1,3,0.25,1],
    [0,5,0.25,0],
    [5,5,0.25,1],
    [5,-5,0.25,1]])
def test_errors_for_valid_config(client,corn,geese,price,error):
    rv = client.get("/_add_numbers?corn={}&geese={}&price={}".format(corn,geese,price))
    assert rv.json["error"] == error

