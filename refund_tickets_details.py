"""Subfunctions of refund tickets file"""

import movie_theatre

def add_funds(customer):
    """Add the value of one ticket to moviegoer's account"""
    customer["cash"] = customer["cash"] + movie_theatre.MOVIE_PRICE
    return customer

def remove_ticket(movie, customer):
    """Removies ticket from customers library"""
    assert movie["title"] in customer["movies"]
    customer["movies"].remove(movie["title"])
    return customer

def add_seat(movie):
    """Add seat back to database"""
    movie["seats_available"] = movie["seats_available"] + 1
    return movie
