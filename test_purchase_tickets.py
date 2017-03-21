"""Tests main purchase ticket function"""

import purchase_tickets

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

def test_purchase_tickets():
    """Tests all subfunctions of purchase_tickets"""
    customers = customer_db()
    movies_ = movie_db()

    actual_bromance, actual_bob = purchase_tickets.purchase_ticket(movies_["Bromance"],
                                                                   customers["Bob"])

    expected_bob = {"movies": ["The Bromance"], "cash" : 95.0}
    assert actual_bob == expected_bob

    expected_bromance = {"title" : "The Bromance", "seats_available" : 19}
    assert actual_bromance == expected_bromance
