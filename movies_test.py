"""Tests the functions of the code.py file"""

import movies

def test_enough_money():
    """Tests the purchase ticket function"""
    customer = {"movies": [], "cash": 4.0}
    assert movies.enough_money(customer) is False
