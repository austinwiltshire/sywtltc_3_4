"""Function for purchasing a ticket from the movie database"""

import purchase_ticket_details

def purchase_ticket(movie, customer):
    """Performs the steps required in purchasing a ticket and returns altered customer and movie"""
    assert purchase_ticket_details.enough_money(customer)
    customer = purchase_ticket_details.dispense_ticket(movie,
                                                       purchase_ticket_details.charge(customer))
    movie = purchase_ticket_details.remove_seat(movie)
    return movie, customer
