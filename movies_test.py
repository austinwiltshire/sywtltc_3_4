"""Tests the functions of the code.py file"""

import movies

CUSTOMERS = {
    "Bob" : {"movies":[],
             "cash" : 100.0},
    "Jim" : {"movies": ["Xmen 8: The Xmennening"],
             "cash" : 10.0},
    "Cary" : {"movies": ["Gigli: The Play: The Book: The movie", "The Bromance"],
              "cash" : 120.0},
    "Ricci": {"movies": [],
              "cash" : 4.0}
}
MOVIE_TICKETS = {
    "Xmen 8: The Xmennening" : {"seats" : 10},
    "The Bromance" : {"seats" : 20},
    "Gigli: The Play: The Book: The movie" : {"seats" : 102}
}

def test_enough_money():
    """Tests the enough money function"""
    assert movies.enough_money("Ricci") is False
    assert movies.enough_money("Bob") is True

def test_charge():
    """Tests charge function"""
    bob = movies.charge("Bob")
    actual_cash = bob["cash"]
    expected_cash = 95.0
    assert actual_cash == expected_cash
