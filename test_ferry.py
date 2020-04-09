import os
import pytest

from pprint import pformat
import dictdiffer

from .ferry import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_calculate_trip_price_of_geese(client):
    rv = client.get('/_add_numbers?corn=2&price=0.25')
    assert rv.json['price'] == 0.75

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


@pytest.mark.parametrize(
    'corn,expected_response', [
        [
            3,
            [
                {
                    'farm_side': {'corn': 2, 'geese': 0},
                    'in_transit': {'corn': 1, 'geese': 0},
                    'market_side': {'corn': 0, 'geese': 0},
                },
                {
                    'farm_side': {'corn': 1, 'geese': 0},
                    'in_transit': {'corn': 1, 'geese': 0},
                    'market_side': {'corn': 1, 'geese': 0},
                },
                {
                    'farm_side': {'corn': 0, 'geese': 0},
                    'in_transit': {'corn': 1, 'geese': 0},
                    'market_side': {'corn': 2, 'geese': 0},
                }
            ]
        ],
        [
            2,
            [
                {
                    'farm_side': {'corn': 1, 'geese': 0},
                    'in_transit': {'corn': 1, 'geese': 0},
                    'market_side': {'corn': 0, 'geese': 0},
                },
                {
                    'farm_side': {'corn': 0, 'geese': 0},
                    'in_transit': {'corn': 1, 'geese': 0},
                    'market_side': {'corn': 1, 'geese': 0},
                }
            ]
        ]
    ]
)
def test_get_configuration(client, corn, expected_response):
    geese = 0
    price = 0.25
    rv = client.get("/_add_numbers?corn={}&geese={}&price={}".format(corn,geese,price))
    assert isinstance(rv.json['itinerary'], list), pformat(
        list(dictdiffer.diff(rv.json["error"], expected_response))
    )

    assert rv.json['itinerary'] == expected_response, pformat(
        list(dictdiffer.diff(rv.json["error"], expected_response))
    )

    #  [
        #  {
            #  'farm_side': {'corn': 2, 'geese': 0},
            #  'in_transit': {'corn': 1, 'geese': 0},
            #  'market_side': {'corn': 0, 'geese': 0},
        #  },
        #  {
            #  'farm_side': {'corn': 1, 'geese': 0},
            #  'in_transit': {'corn': 1, 'geese': 0},
            #  'market_side': {'corn': 1, 'geese': 0},
        #  },
        #  {
            #  'farm_side': {'corn': 0, 'geese': 0},
            #  'in_transit': {'corn': 1, 'geese': 0},
            #  'market_side': {'corn': 2, 'geese': 0},
        #  }
    #  ]



