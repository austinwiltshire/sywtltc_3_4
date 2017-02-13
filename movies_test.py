"""Tests the functions of the code.py file"""

import movies

def test_enough_money():
    """Tests the purchase ticket function"""
    customer = {"movies": [], "cash": 4.0}
    customer2 = {"movies": [], "cash": 7.0}
    assert movies.enough_money(customer) is False
    assert movies.enough_money(customer2) is True

def test_deduct_money():
    """Tests $5 charge to account"""
    customer = movies.deduct_money({"movies": [], "cash": 100.0})
    actual_cash = customer["cash"]
    expected_cash = 95.0
    assert actual_cash == expected_cash
    customer = movies.deduct_money({"movies": [], "cash": 7.0})
    actual_cash = customer["cash"]
    expected_cash = 2.0
    assert actual_cash == expected_cash
