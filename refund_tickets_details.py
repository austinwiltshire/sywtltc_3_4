"""Subfunctions of refund tickets file"""

import movie_theatre

def add_funds(customer):
    """Add the value of one ticket to moviegoer's account

    Args:
        customer (dict): uses 'cash' key from customer's dictionary key that
        represents how much cash is in the customer’s account.

    Returns:
        cash: (dict) Returns customer's 'cash' key from dictionary with refunded MOVIE_PRICE added.
    """
    customer["cash"] = customer["cash"] + movie_theatre.MOVIE_PRICE
    return customer

def remove_ticket(movie, customer):
    """Removies ticket from customers library
    
    Args:
        customer (dict): A dictionary that supports a 'movies' key that
        represents which movies are in the customer’s account.
        movie (dict): A dictionary that supports a 'title' key that
        represents the title of the movie to be appended to customer's account.

    Returns:
        customer: (dict) Returns customers dictionary with  movie title removed
        from customer's 'movies' key.
    """
    assert movie["title"] in customer["movies"]
    customer["movies"].remove(movie["title"])
    return customer

def add_seat(movie):
    """Add seat back to database
    Args:
        movie (dict): A dictionary containing 'seats available' key.

    Returns:
        movie: (dict) Customers dictionary with 'seats available' key increased by 1.
    """
    movie["seats_available"] = movie["seats_available"] + 1
    return movie
