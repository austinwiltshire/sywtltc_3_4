"""Tests main purchase ticket function"""

import purchase_tickets
import customer_db

def test_purchase_tickets():
    """Tests all subfunctions of purchase_tickets"""
    customers = customer_db.customer_db()
    movies_ = customer_db.movie_db()

    actual_bromance, actual_bob = purchase_tickets.purchase_ticket(movies_["Bromance"],
                                                                   customers["Bob"])

    expected_bob = {"movies": ["The Bromance"], "cash" : 95.0}
    assert actual_bob == expected_bob

    expected_bromance = {"title" : "The Bromance", "seats_available" : 19}
    assert actual_bromance == expected_bromance
