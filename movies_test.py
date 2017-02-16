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
    bob = {"movies":[], "cash" : 100.0}
    ricci = {"movies": [], "cash" : 4.0}
    assert movies.enough_money(ricci) is False
    assert movies.enough_money(bob) is True

def test_charge():
    """Tests charge function"""
    bob = {"movies": [], "cash": 100.0}
    bobs_actual_cash = movies.charge(bob)["cash"]
    bobs_expected_cash = 95.0
    assert bobs_actual_cash == bobs_expected_cash
    jim = {"movies": ["Xmen 8: The Xmennening"], "cash" : 10.0}
    jims_actual_cash = movies.charge(jim)["cash"]
    jims_expected_cash = 5.0
    assert jims_actual_cash == jims_expected_cash

def test_dispense_ticket():
    """Test adding ticket to customers account"""
    bob = {"movies": [], "cash": 100.0}
    bobs_library = movies.dispense_ticket("Xmen 8: The Xmennening", bob)["movies"]
    bobs_expected_library = ['Xmen 8: The Xmennening']
    assert bobs_library == bobs_expected_library
    jim = {"movies": ["Xmen 8: The Xmennening"], "cash" : 10.0}
    jims_library = movies.dispense_ticket("The Bromance", jim)["movies"]
    jims_expected_library = ['Xmen 8: The Xmennening', "The Bromance"]
    assert jims_library == jims_expected_library

