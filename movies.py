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
    customer["movies"].append(movie["title"])
    return customer
def remove_seat(movie):
    """Remove seat from ticket database"""
    movie["seats"] = movie["seats"] - 1.0
    return movie

def refund_ticket(movie, customer):
    """Performs the steps required in refunding a ticket and returns altered customer and movie"""
    customer = add_funds(customer)
    customer = remove_ticket(movie, customer)
    movie = remove_seat(movie)
    return customer, movie

def add_funds(customer):
    """Add $5 back to moviegoer's account"""
    customer["cash"] = customer["cash"] + 5.0
    return customer
def remove_ticket(movie, customer):
    """Removies ticket from customers library"""
    customer["movies"].remove(movie)
    return customer
def add_seat(movie):
    """Add seat back to database"""
    movie["seats"] = movie["seats"] + 1
    return movie


#def enter_theatre(movie, customer):
 #   """Removes ticket from account"""
#    customer["movies"] = customer["movies"] - movie

def audit(movies, customers):
    """Prints system data"""
    print(CUSTOMER)
    print(MOVIE)

