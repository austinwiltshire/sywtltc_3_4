"""Tests the functions of the code.py file"""

import movies

def customer_db():
    """Define Customer database for testing"""
    return {
        "Bob" : {"movies":[],
                 "cash" : 100.0},
        "Jim" : {"movies": ["Xmen 8: The Xmennening"],
                 "cash" : 10.0},
        "Cary" : {"movies": ["Gigli: The Play: The Book: The movie", "The Bromance"],
                  "cash" : 120.0},
        "Ricci": {"movies": [],
                  "cash" : 4.0}
    }

def movie_db():
    """Define movie database for testing"""
    return {
        "Xmen" : {"title" : "Xmen 8: The Xmennening", "seats_avaliable" : 10},
        "Bromance" : {"title" : "The Bromance", "seats_avaliable" : 20},
        "Gigli" : {"title" : "Gigli: The Play: The Book: The movie", "seats_avaliable" : 102}
    }

def test_enough_money():
    """Tests the enough money function"""
    customers = customer_db()
    bob = customers["Bob"]
    ricci = customers["Ricci"]
    assert not movies.enough_money(ricci)
    assert movies.enough_money(bob)

def test_charge():
    """Tests charge function"""
    customers = customer_db()
    bob = customers["Bob"]
    assert movies.enough_money(bob)
    bobs_actual_cash = movies.charge(bob)["cash"]
    bobs_expected_cash = 95.0
    assert bobs_actual_cash == bobs_expected_cash
    jim = customers["Jim"]
    assert movies.enough_money(bob)
    jims_actual_cash = movies.charge(jim)["cash"]
    jims_expected_cash = 5.0
    assert jims_actual_cash == jims_expected_cash
    ricci = customers["Ricci"]
    assert not movies.enough_money(ricci)

def test_dispense_ticket():
    """Test adding ticket to customers account"""
    customers = customer_db()
    movies_ = movie_db()
    bob = customers["Bob"]
    xmen = movies_["Xmen"]
    bobs_library = movies.dispense_ticket(xmen, bob)["movies"]
    bobs_expected_library = ["Xmen 8: The Xmennening"]
    assert bobs_library == bobs_expected_library
    jim = customers["Jim"]
    bromance = movies_["Bromance"]
    jims_library = movies.dispense_ticket(bromance, jim)["movies"]
    jims_expected_library = ["Xmen 8: The Xmennening", "The Bromance"]
    assert jims_library == jims_expected_library

def test_remove_seat():
    """Tests remove seat function"""
    movies_ = movie_db()
    xmen = movies_["Xmen"]
    assert xmen["seats_avaliable"] >= 1
    xmen_seats_avaliable = movies.remove_seat(xmen)
    xmen_expected_seats_avaliable = {"title" : "Xmen 8: The Xmennening", "seats_avaliable" : 9}
    assert xmen_seats_avaliable == xmen_expected_seats_avaliable
    bromance = movies_["Bromance"]
    assert bromance["seats_avaliable"] >= 1
    bro_seats_avaliable = movies.remove_seat(bromance)
    bro_expected_seats_avaliable = {"title" : "The Bromance", "seats_avaliable" : 19}
    assert bro_seats_avaliable == bro_expected_seats_avaliable

def test_purchase_tickets():
    """Tests all subfunctions of purchase_tickets"""
    customers = customer_db()
    movies_ = movie_db()
    bob = customers["Bob"]
    bromance = movies_["Bromance"]
    actual_bob, actual_bromance = movies.purchase_ticket(bromance, bob)
    expected_bob = {"movies": ["The Bromance"], "cash" : 95.0}
    expected_bromance = {"title" : "The Bromance", "seats_avaliable" : 19}
    assert actual_bob == expected_bob
    assert actual_bromance == expected_bromance

def test_add_funds():
    """Tests charge function"""
    customers = customer_db()
    bob = customers["Bob"]
    bobs_actual_cash = movies.add_funds(bob)["cash"]
    bobs_expected_cash = 105.0
    assert bobs_actual_cash == bobs_expected_cash
    ricci = customers["Ricci"]
    ricci_actual_cash = movies.add_funds(ricci)["cash"]
    ricci_expected_cash = 9.0
    assert ricci_actual_cash == ricci_expected_cash

def test_remove_ticket():
    """Tests removing ticket back from account"""
    customers = customer_db()
    movies_ = movie_db()
    jim = customers["Jim"]
    xmen = movies_["Xmen"]
    jims_library = movies.remove_ticket(xmen, jim)["movies"]
    jims_expected_library = []
    assert jims_library == jims_expected_library
    cary = customers["Cary"]
    bromance = movies_["Bromance"]
    cary_library = movies.remove_ticket(bromance, cary)["movies"]
    cary_expected_library = ["Gigli: The Play: The Book: The movie"]
    assert cary_library == cary_expected_library

def test_add_seat():
    """Tests remove seat function"""
    movies_ = movie_db()
    xmen = movies_["Xmen"]
    xmen_seats_avaliable = movies.add_seat(xmen)["seats_avaliable"]
    xmen_expected_seats_avaliable = 11
    assert xmen_seats_avaliable == xmen_expected_seats_avaliable
    bromance = movies_["Bromance"]
    bro_seats_avaliable = movies.add_seat(bromance)["seats_avaliable"]
    bro_expected_seats_avaliable = 21
    assert bro_seats_avaliable == bro_expected_seats_avaliable

def test_refund_ticket():
    """Tests all subfunctions of refund_tickets"""
    customers = customer_db()
    movies_ = movie_db()
    jim = customers["Jim"]
    xmen = movies_["Xmen"]
    actual_jim, actual_xmen = movies.refund_ticket(xmen, jim)
    expected_jim = {"movies": [], "cash" : 15.0}
    expected_xmen = {"title" : "Xmen 8: The Xmennening", "seats_avaliable" : 11}
    assert actual_jim == expected_jim
    assert actual_xmen == expected_xmen
