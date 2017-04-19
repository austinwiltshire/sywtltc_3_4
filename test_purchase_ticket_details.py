"""Tests the functions of the purchase_ticket_details.py file"""

import purchase_ticket_details
import customer_db

def test_enough_money():
    """Tests the enough money function"""
    customers = customer_db.customer_db()

    ricci = customers["Ricci"]
    assert ricci["cash"] < 5
    assert not purchase_ticket_details.enough_money(ricci["cash"])

    bob = customers["Bob"]
    assert purchase_ticket_details.enough_money(bob["cash"])

def test_charge():
    """Tests charge function"""
    customers = customer_db.customer_db()

    bob = customers["Bob"]
    assert bob["cash"] == 100.0
    assert purchase_ticket_details.enough_money(bob["cash"])
    bobs_actual_cash = purchase_ticket_details.charge(bob)["cash"]
    bobs_expected_cash = 95.0
    assert bobs_actual_cash == bobs_expected_cash

    jim = customers["Jim"]
    assert jim["cash"] == 10
    assert purchase_ticket_details.enough_money(bob["cash"])
    jims_actual_cash = purchase_ticket_details.charge(jim)["cash"]
    jims_expected_cash = 5.0
    assert jims_actual_cash == jims_expected_cash

    ricci = customers["Ricci"]
    assert ricci["cash"] == 4.0
    assert not purchase_ticket_details.enough_money(ricci["cash"])

def test_dispense_ticket():
    """Test adding ticket to customers account"""
    customers = customer_db.customer_db()
    movies_ = customer_db.movie_db()

    bob, xmen = customers["Bob"], movies_["Xmen"]
    bobs_library = purchase_ticket_details.dispense_ticket(xmen, bob)["movies"]
    bobs_expected_library = ["Xmen 8: The Xmennening"]
    assert bobs_library == bobs_expected_library

    jim, bromance = customers["Jim"], movies_["Bromance"]
    jims_library = purchase_ticket_details.dispense_ticket(bromance, jim)["movies"]
    jims_expected_library = ["Xmen 8: The Xmennening", "The Bromance"]
    assert jims_library == jims_expected_library

def test_remove_seat():
    """Tests remove seat function"""
    movies_ = customer_db.movie_db()

    xmen = movies_["Xmen"]
    assert xmen["seats_available"] == 10
    xmen = purchase_ticket_details.remove_seat(xmen)
    assert xmen["seats_available"] == 9

    hungergames = movies_["Hungergames"]
    assert hungergames["seats_available"] == 1
    hungergames = purchase_ticket_details.remove_seat(hungergames)
    assert hungergames["seats_available"] == 0
