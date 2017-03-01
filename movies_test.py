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
    "Xmen" : {"title" : "Xmen 8: The Xmennening", "seats" : 10},
    "Bromance" : {"title" : "The Bromance", "seats" : 20},
    "Gigli" : {"title" : "Gigli: The Play: The Book: The movie", "seats" : 102}
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
    jim = {"movies": "Xmen 8: The Xmennening", "cash" : 10.0}
    jims_actual_cash = movies.charge(jim)["cash"]
    jims_expected_cash = 5.0
    assert jims_actual_cash == jims_expected_cash
def test_dispense_ticket():
    """Test adding ticket to customers account"""
    bob = {"movies": [], "cash": 100.0}
    xmen = {"title" : "Xmen 8: The Xmennening", "seats" : 10}
    bobs_library = movies.dispense_ticket(xmen, bob)["movies"]
    bobs_expected_library = ["Xmen 8: The Xmennening"]
    assert bobs_library == bobs_expected_library
    jim = {"movies": ["Xmen 8: The Xmennening"], "cash" : 10.0}
    bromance = {"title" : "The Bromance", "seats" : 20}
    jims_library = movies.dispense_ticket(bromance, jim)["movies"]
    jims_expected_library = ["Xmen 8: The Xmennening", "The Bromance"]
    assert jims_library == jims_expected_library
def test_remove_seat():
    """Tests remove seat function"""
    xmen = {"title" : ["Xmen 8: The Xmennening"], "seats" : 10}
    xmen_seats = movies.remove_seat(xmen)
    xmen_expected_seats = {"title" : ["Xmen 8: The Xmennening"], "seats" : 9}
    assert xmen_seats == xmen_expected_seats
    bromance = {"title" : ["The Bromance"], "seats" : 20}
    bro_seats = movies.remove_seat(bromance)
    bro_expected_seats = {"title" : ["The Bromance"], "seats" : 19}
    assert bro_seats == bro_expected_seats

def test_purchase_tickets():
    """Tests all subfunctions of purchase_tickets"""
    bob = {"movies": [], "cash": 100.0}
    bromance = {"title" : ["The Bromance"], "seats" : 20}
    actual_bob, actual_bromance = movies.purchase_ticket(bromance, bob)
    expected_bob = {"movies": [["The Bromance"]], "cash" : 95.0}
    expected_bromance = {"title" : ["The Bromance"], "seats" : 19}
    assert actual_bob == expected_bob
    assert actual_bromance == expected_bromance

def test_add_funds():
    """Tests charge function"""
    bob = {"movies": [], "cash": 100.0}
    bobs_actual_cash = movies.add_funds(bob)["cash"]
    bobs_expected_cash = 105.0
    assert bobs_actual_cash == bobs_expected_cash
    ricci = {"movies" : [], "cash" : 4.0}
    ricci_actual_cash = movies.add_funds(ricci)["cash"]
    ricci_expected_cash = 9.0
    assert ricci_actual_cash == ricci_expected_cash
def test_remove_ticket():
    """Tests removing ticket back from account"""
    jim = {"movies": ["Xmen 8: The Xmennening"], "cash" : 10.0}
    xmen = {"title" : "Xmen 8: The Xmennening", "seats" : 10}
    jims_library = movies.remove_ticket(xmen, jim)["movies"]
    jims_expected_library = []
    assert jims_library == jims_expected_library
    cary = {"movies": ["Gigli: The Play: The Book: The movie", "The Bromance"],
            "cash" : 120.0}
    bromance = {"title" : "The Bromance", "seats" : 20}
    cary_library = movies.remove_ticket(bromance, cary)["movies"]
    cary_expected_library = ["Gigli: The Play: The Book: The movie"]
    assert cary_library == cary_expected_library
def test_add_seat():
    """Tests remove seat function"""
    xmen = {"title" : "Xmen 8: The Xmennening", "seats" : 10}
    xmen_seats = movies.add_seat(xmen)["seats"]
    xmen_expected_seats = 11
    assert xmen_seats == xmen_expected_seats
    bromance = {"title" : "The Bromance", "seats" : 20}
    bro_seats = movies.add_seat(bromance)["seats"]
    bro_expected_seats = 21
    assert bro_seats == bro_expected_seats

def test_refund_ticket():
    """Tests all subfunctions of refund_tickets"""
    jim = {"movies": ["Xmen 8: The Xmennening"], "cash" : 10.0}
    xmen = {"title" : "Xmen 8: The Xmennening", "seats" : 10}
    actual_jim, actual_xmen = movies.refund_ticket(xmen, jim)
    expected_jim = {"movies": [], "cash" : 15.0}
    expected_xmen = {"title" : "Xmen 8: The Xmennening", "seats" : 11}
    assert actual_jim == expected_jim
    assert actual_xmen == expected_xmen
