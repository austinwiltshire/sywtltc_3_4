"""Tests details for refund function"""

import refund_tickets_details
import customer_db

def test_add_funds():
    """Tests charge function"""
    customers = customer_db.customer_db()

    bob = customers["Bob"]
    assert bob["cash"] == 100.0
    bobs_actual_cash = refund_tickets_details.add_funds(bob)["cash"]
    bobs_expected_cash = 105.0
    assert bobs_actual_cash == bobs_expected_cash

    ricci = customers["Ricci"]
    assert ricci["cash"] == 4.0
    ricci_actual_cash = refund_tickets_details.add_funds(ricci)["cash"]
    ricci_expected_cash = 9.0
    assert ricci_actual_cash == ricci_expected_cash

def test_remove_ticket():
    """Tests removing ticket back from account"""
    customers = customer_db.customer_db()
    movies_ = customer_db.movie_db()

    jim, xmen = customers["Jim"], movies_["Xmen"]
    jims_library = refund_tickets_details.remove_ticket(xmen, jim)["movies"]
    jims_expected_library = []
    assert jims_library == jims_expected_library

    cary, bromance = customers["Cary"], movies_["Bromance"]
    cary_library = refund_tickets_details.remove_ticket(bromance, cary)["movies"]
    cary_expected_library = ["Gigli: The Play: The Book: The movie"]
    assert cary_library == cary_expected_library

def test_add_seat():
    """Tests remove seat function"""
    movies_ = customer_db.movie_db()

    xmen = movies_["Xmen"]
    assert xmen["seats_available"] == 10
    xmen_seats_available = refund_tickets_details.add_seat(xmen)["seats_available"]
    xmen_expected_seats_available = 11
    assert xmen_seats_available == xmen_expected_seats_available

    bromance = movies_["Bromance"]
    assert bromance["seats_available"] == 20
    bro_seats_available = refund_tickets_details.add_seat(bromance)["seats_available"]
    bro_expected_seats_available = 21
    assert bro_seats_available == bro_expected_seats_available
