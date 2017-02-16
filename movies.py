"""Movie ticket processing system and database"""

def enough_money(customer):
    """Check if customer has adequate funds"""
    balance = customer["cash"]
    if balance < 5.0:
        return False
    return True

def purchase_ticket(movie, customer):
    """Performs the steps required in purchasing a ticket and returns altered customer and movie"""
    customer = charge(customer)
    customer = dispense_ticket(movie, customer)
    movie = remove_seat(movie)
    return customer, movie

def charge(customer):
    """Charge customer $5"""
    customer["cash"] = customer["cash"] - 5.0
    return customer
def dispense_ticket(movie, customer):
    """Add movie to customer's account"""
    customer["movies"].append(movie)
    return customer
def remove_seat(movie):
    """Remove seat from ticket database"""
    movie["seats"] = movie["seats"] - 1
    return movie

def refund(movie, customer):
    """Add $5 back to moviegoer's account"""
    customer["cash"] = customer["cash"] + 5.0
    return customer

def enter_theatre(movie, customer):
    """Removes ticket from account"""
#    customer["movies"] = customer["movies"] - movie

def audit(movies, customers):
    """Prints system data"""
    print(CUSTOMER)
    print(MOVIE)

