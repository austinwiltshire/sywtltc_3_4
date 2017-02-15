"""Movie ticket processing system and database"""

MOVIE_PRICE = 5.0

def enough_money(customer):
    """Check if customer has adequate funds"""
    if customer["cash"] < 5.0:
        return False
    return True

def purchase(movie, customer):
    """Deduct $5 from moviegoer's account"""
    customer["cash"] = customer["cash"] - 5.0
#   customer["movies"] = customer["movies"].append(movie)
    return customer

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

