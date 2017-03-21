"""Function and subfunctions for purchasing a ticket from the movie database"""

import movie_theatre

def enough_money(customer):
    """Check if customer has adequate funds"""
    return customer["cash"] >= movie_theatre.MOVIE_PRICE

def charge(customer):
    """Charge customer the price of one ticket"""
    assert enough_money(customer)
    customer["cash"] = customer["cash"] - movie_theatre.MOVIE_PRICE
    return customer

def dispense_ticket(movie, customer):
    """Add movie to customer's account"""
    assert movie["seats_available"] >= 1
    customer["movies"].append(movie["title"])
    return customer

def remove_seat(movie):
    """Remove seat from ticket database"""
    assert movie["seats_available"] >= 1
    movie["seats_available"] = movie["seats_available"] - 1
    return movie
