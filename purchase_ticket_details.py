"""Function and subfunctions for purchasing a ticket from the movie database"""

import movie_theatre

def enough_money(cash):
    """Check if customer has adequate funds

    Args:
        cash (dict): 'cash' key from customer's dictionary key that
        represents how much cash is in the customer’s account.

    Returns:
        cash: (dict) Returns customer's 'cash' key from dictionary if greater than MOVIE_PRICE.
    """
    return cash >= movie_theatre.MOVIE_PRICE

def charge(customer):
    """Charge customer the price of one ticket

    Args:
        customer (dict): A dictionary that supports a 'cash' key that
        represents how much cash is in the customer’s account.

    Returns:
        customer: (dict) Returns customer's dictionary 'cash' key reduced by price of one ticket.

    """
    assert enough_money(customer["cash"])
    customer["cash"] = customer["cash"] - movie_theatre.MOVIE_PRICE
    return customer

def dispense_ticket(movie, customer):
    """Add movie to customer's account

    Args:
        customer (dict): A dictionary that supports a 'movies' key that
        represents which movies are in the customer’s account.
        movie (dict): A dictionary that supports a 'title' key that
        represents the title of the movie to be appended to customer's account.

    Returns:
        customer: (dict) Returns customers dictionary with appended movie title
        to customer's 'movies' key.
    """

    assert movie["seats_available"] >= 1
    customer["movies"].append(movie["title"])
    return customer

def remove_seat(movie):
    """Remove seat from ticket database

    Args:
        movie (dict): A dictionary containing 'seats available' key.

    Returns:
        movie: (dict) Customers dictionary with 'seats available' key reduced by 1.
        """
    assert movie["seats_available"] >= 1
    movie["seats_available"] = movie["seats_available"] - 1
    return movie
