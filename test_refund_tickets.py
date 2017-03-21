"""Test main refund function"""

import refund_tickets

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

def test_refund_ticket():
    """Tests all subfunctions of refund_tickets"""
    customers = customer_db()
    movies_ = movie_db()

    actual_jim, actual_xmen = refund_tickets.refund_ticket(movies_["Xmen"], customers["Jim"])

    expected_jim = {"movies": [], "cash" : 15.0}
    assert actual_jim == expected_jim

    expected_xmen = {"title" : "Xmen 8: The Xmennening", "seats_available" : 11}
    assert actual_xmen == expected_xmen
