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
    "Xmen 8: The Xmennening": 10,
    "The Bromance" : 20,
    "Gigli: The Play: The Book: The movie" : 102
}

def test_enough_money():
    """Tests the purchase ticket function"""
    assert movies.enough_money("Ricci") is False
    assert movies.enough_money("Bob") is True

def test_purchase():
    """Tests $5 charge to account"""
    customer = movies.purchase({"movies": [], "cash": 100.0})
    actual_cash = customer["cash"]
    expected_cash = 95.0
    assert actual_cash == expected_cash
    customer = movies.purchase({"movies": [], "cash": 7.0})
    actual_cash = customer["cash"]
    expected_cash = 2.0
    assert actual_cash == expected_cash

def test_refund():
    """Tests $5 refund to account"""
    customer = movies.refund({"movies": [], "cash": 50.0})
    actual_cash = customer["cash"]
    expected_cash = 55.0
    assert actual_cash == expected_cash
    customer = movies.refund({"movies": [], "cash": 15.0})
    actual_cash = customer["cash"]
    expected_cash = 20.0
    assert actual_cash == expected_cash
