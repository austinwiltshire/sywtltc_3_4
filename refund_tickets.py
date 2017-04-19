"""Functions and subfunctions for refunding a ticket to a customer"""

import refund_tickets_details

def refund_ticket(movie, customer):
    """Performs the steps required in refunding a ticket and returns altered customer and movie
    
    Args:
        movie (dict): dictionary containing 'title' and 'seats_available' for each movie.
        customer (dict): dictionary containing 'movies' and 'cash' keys for each customer.

    Returns:
        movie: (dict) dictionary containing 'title' unchanged, and 'seats_remaining'
        increased by 1.
        customer: (dict) dictionary containing removed movie title in 'movies' key.
        'cash' key increased by MOVIE_PRICE."""
    customer = refund_tickets_details.remove_ticket(movie,
                                                    refund_tickets_details.add_funds(customer))
    movie = refund_tickets_details.add_seat(movie)
    return customer, movie
