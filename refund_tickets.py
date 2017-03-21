"""Functions and subfunctions for refunding a ticket to a customer"""

import refund_tickets_details

def refund_ticket(movie, customer):
    """Performs the steps required in refunding a ticket and returns altered customer and movie"""
    customer = refund_tickets_details.remove_ticket(movie,
                                                    refund_tickets_details.add_funds(customer))
    movie = refund_tickets_details.add_seat(movie)
    return customer, movie
