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
        "Xmen" : {"title" : "Xmen 8: The Xmennening", "seats_available" : 10},
        "Bromance" : {"title" : "The Bromance", "seats_available" : 20},
        "Gigli" : {"title" : "Gigli: The Play: The Book: The movie", "seats_available" : 102},
        "Hungergames" : {"title" : "The Hunger Games", "seats_available" : 1}
    }

def test_enough_money():
    """Tests the enough money function"""
    customers = customer_db()

    ricci = customers["Ricci"]
    assert ricci["cash"] < 5
    assert not movies.enough_money(ricci)

    bob = customers["Bob"]
    assert movies.enough_money(bob)

def test_charge():
    """Tests charge function"""
    customers = customer_db()

    bob = customers["Bob"]
    assert bob["cash"] == 100.0
    assert movies.enough_money(bob)
    bobs_actual_cash = movies.charge(bob)["cash"]
    bobs_expected_cash = 95.0
    assert bobs_actual_cash == bobs_expected_cash

    jim = customers["Jim"]
    assert jim["cash"] == 10
    assert movies.enough_money(bob)
    jims_actual_cash = movies.charge(jim)["cash"]
    jims_expected_cash = 5.0
    assert jims_actual_cash == jims_expected_cash

    ricci = customers["Ricci"]
    assert ricci["cash"] == 4.0
    assert not movies.enough_money(ricci)

def test_dispense_ticket():
    """Test adding ticket to customers account"""
    customers = customer_db()
    movies_ = movie_db()

    bob, xmen = customers["Bob"], movies_["Xmen"]
    bobs_library = movies.dispense_ticket(xmen, bob)["movies"]
    bobs_expected_library = ["Xmen 8: The Xmennening"]
    assert bobs_library == bobs_expected_library

    jim, bromance = customers["Jim"], movies_["Bromance"]
    jims_library = movies.dispense_ticket(bromance, jim)["movies"]
    jims_expected_library = ["Xmen 8: The Xmennening", "The Bromance"]
    assert jims_library == jims_expected_library

def test_remove_seat():
    """Tests remove seat function"""
    movies_ = movie_db()

    xmen = movies_["Xmen"]
    assert xmen["seats_available"] == 10
    xmen = movies.remove_seat(xmen)
    assert xmen["seats_available"] == 9

    hungergames = movies_["Hungergames"]
    assert hungergames["seats_available"] == 1
    hungergames = movies.remove_seat(hungergames)
    assert hungergames["seats_available"] == 0

def test_purchase_tickets():
    """Tests all subfunctions of purchase_tickets"""
    customers = customer_db()
    movies_ = movie_db()

    actual_bob, actual_bromance = movies.purchase_ticket(movies_["Bromance"], customers["Bob"])

    expected_bob = {"movies": ["The Bromance"], "cash" : 95.0}
    assert actual_bob == expected_bob

    expected_bromance = {"title" : "The Bromance", "seats_available" : 19}
    assert actual_bromance == expected_bromance

def test_add_funds():
    """Tests charge function"""
    customers = customer_db()

    bob = customers["Bob"]
    assert bob["cash"] == 100.0
    bobs_actual_cash = movies.add_funds(bob)["cash"]
    bobs_expected_cash = 105.0
    assert bobs_actual_cash == bobs_expected_cash

    ricci = customers["Ricci"]
    assert ricci["cash"] == 4.0
    ricci_actual_cash = movies.add_funds(ricci)["cash"]
    ricci_expected_cash = 9.0
    assert ricci_actual_cash == ricci_expected_cash

def test_remove_ticket():
    """Tests removing ticket back from account"""
    customers = customer_db()
    movies_ = movie_db()

    jim, xmen = customers["Jim"], movies_["Xmen"]
    jims_library = movies.remove_ticket(xmen, jim)["movies"]
    jims_expected_library = []
    assert jims_library == jims_expected_library

    cary, bromance = customers["Cary"], movies_["Bromance"]
    cary_library = movies.remove_ticket(bromance, cary)["movies"]
    cary_expected_library = ["Gigli: The Play: The Book: The movie"]
    assert cary_library == cary_expected_library

def test_add_seat():
    """Tests remove seat function"""
    movies_ = movie_db()

    xmen = movies_["Xmen"]
    assert xmen["seats_available"] == 10
    xmen_seats_available = movies.add_seat(xmen)["seats_available"]
    xmen_expected_seats_available = 11
    assert xmen_seats_available == xmen_expected_seats_available

    bromance = movies_["Bromance"]
    assert bromance["seats_available"] == 20
    bro_seats_available = movies.add_seat(bromance)["seats_available"]
    bro_expected_seats_available = 21
    assert bro_seats_available == bro_expected_seats_available

def test_refund_ticket():
    """Tests all subfunctions of refund_tickets"""
    customers = customer_db()
    movies_ = movie_db()

    actual_jim, actual_xmen = movies.refund_ticket(movies_["Xmen"], customers["Jim"])

    expected_jim = {"movies": [], "cash" : 15.0}
    assert actual_jim == expected_jim

    expected_xmen = {"title" : "Xmen 8: The Xmennening", "seats_available" : 11}
    assert actual_xmen == expected_xmen
