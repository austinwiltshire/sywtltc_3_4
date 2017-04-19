"""Test main refund function"""

import refund_tickets
import customer_db

def test_refund_ticket():
    """Tests all subfunctions of refund_tickets"""
    customers = customer_db.customer_db()
    movies_ = customer_db.movie_db()

    actual_jim, actual_xmen = refund_tickets.refund_ticket(movies_["Xmen"], customers["Jim"])

    expected_jim = {"movies": [], "cash" : 15.0}
    assert actual_jim == expected_jim

    expected_xmen = {"title" : "Xmen 8: The Xmennening", "seats_available" : 11}
    assert actual_xmen == expected_xmen
