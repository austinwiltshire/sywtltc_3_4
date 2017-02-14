"""Movie ticket processing system and database"""

MOVIE_PRICE = 5.0

def enough_money(customer):
    """Check if customer has adequate funds"""
    if customer["cash"] < 5.0:
        return False
    return True

def purchase(customer):
    """Deduct $5 from moviegoer's account"""
    customer["cash"] = customer["cash"] - 5.0
    return customer

def refund(customer):
    """Add $5 back to moviegoer's account"""
    customer["cash"] = customer["cash"] + 5.0
    return customer


    #customer[customer]["movies"].append("movies");
    #return True

if __name__ == "__main__":
    CUSTOMER_DB = {
        "Bob" : {"movies":[],
                 "cash" : 100.0},
        "Jim" : {"movies": ["Xmen 8: The Xmennening"],
                 "cash" : 10.0},
        "Cary" : {"movies": ["Gigli: The Play: The Book: The movie", "The Bromance"],
                  "cash" : 120.0},
        "Ricci": {"movies": [],
                  "cash" : 4.0}
    }
    MOVIE_DB = {
        "Xmen 8: The Xmennening": 10,
        "The Bromance" : 20,
        "Gigli: The Play: The Book: The movie" : 102
    }
