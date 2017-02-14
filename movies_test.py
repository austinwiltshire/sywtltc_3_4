"""Tests the functions of the code.py file"""

import movies

def test_enough_money():
    """Tests the purchase ticket function"""
    customer = {"movies": [], "cash": 4.0}
    customer2 = {"movies": [], "cash": 7.0}
    assert movies.enough_money(customer) is False
    assert movies.enough_money(customer2) is True

def test_purchase():
    """Tests $5 charge to account"""
    customer = movies.purchase({"movies": [], "cash": 100.0})
    actual_cash = customer["cash"]
    expected_cash = 95.0
    assert actual_cash == expected_cash
    customer = movies.purchase({"movies": [], "cash": 7.0})
    actual_cash = customer["cash"]
    expected_cash = 2.0
    assert actual_cash == expected_cash

def test_refund():
    """Tests $5 refund to account"""
    customer = movies.refund({"movies": [], "cash": 50.0})
    actual_cash = customer["cash"]
    expected_cash = 55.0
    assert actual_cash == expected_cash
    customer = movies.refund({"movies": [], "cash": 15.0})
    actual_cash = customer["cash"]
    expected_cash = 20.0
    assert actual_cash == expected_cash
