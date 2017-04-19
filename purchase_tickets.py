"""Function for purchasing a ticket from the movie database"""

import purchase_ticket_details

def purchase_ticket(movie, customer):
    """Performs the steps required in purchasing a ticket and returns altered customer and movie

    Args:
        movie (dict): dictionary containing 'title' and 'seats_available' for each movie.
        customer (dict): dictionary containing 'movies' and 'cash' keys for each customer.

    Returns:
        movie: (dict) dictionary containing 'title' unchanged, and 'seats_remaining'
        reduced by 1.
        customer: (dict) dictionary containing appended movie title to 'movies' key.
        'cash' key reduced by MOVIE_PRICE.
    """
    assert purchase_ticket_details.enough_money(customer["cash"])
    customer = purchase_ticket_details.dispense_ticket(movie,
                                                       purchase_ticket_details.charge(customer))
    movie = purchase_ticket_details.remove_seat(movie)
    return movie, customer
