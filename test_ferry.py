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