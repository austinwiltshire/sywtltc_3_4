"""Movie ticket process system and database"""

MOVIE_PRICE = 5.0

import pprint
    
def customer_db():
    """Define Customer database for testing"""
    return {
        "Bob" : {"movies":[],
                 "cash" : 100.0},
        "Jim" : {"movies": ["Xmen 8: The Xmennening"],
                 "cash" : 10.0},
        "Cary" : {"movies": ["Gigli: The Play: The Book: The movie", "The Bromance"],
                  "cash" : 120.0},
        "Ricci": {"movies": [],
                  "cash" : 4.0}
    }

def movie_db():
    """Define movie database for testing"""
    return {
        "Xmen" : {"title" : "Xmen 8: The Xmennening", "seats_avaliable" : 10},
        "Bromance" : {"title" : "The Bromance", "seats_avaliable" : 20},
        "Gigli" : {"title" : "Gigli: The Play: The Book: The movie", "seats_avaliable" : 102}
    }

def enough_money(customer):
    """Check if customer has adequate funds"""
    balance = customer["cash"]
    if balance < MOVIE_PRICE:
        return False
    return True

def purchase_ticket(movie, customer):
    """Performs the steps required in purchasing a ticket and returns altered customer and movie"""
    assert enough_money(customer)
    customer = charge(customer)
    customer = dispense_ticket(movie, customer)
    movie = remove_seat(movie)
    return customer, movie

def charge(customer):
    """Charge customer the price of one ticket"""
    customer["cash"] = customer["cash"] - MOVIE_PRICE
    return customer

def dispense_ticket(movie, customer):
    """Add movie to customer's account"""
    assert movie["seats_avaliable"] >= 1
    customer["movies"].append(movie["title"])
    return customer

def remove_seat(movie):
    """Remove seat from ticket database"""
    movie["seats_avaliable"] = movie["seats_avaliable"] - 1
    return movie

def refund_ticket(movie, customer):
    """Performs the steps required in refunding a ticket and returns altered customer and movie"""
    customer = add_funds(customer)
    customer = remove_ticket(movie, customer)
    movie = add_seat(movie)
    return customer, movie

def add_funds(customer):
    """Add the value of one ticket to moviegoer's account"""
    customer["cash"] = customer["cash"] + MOVIE_PRICE
    return customer

def remove_ticket(movie, customer):
    """Removies ticket from customers library"""
    assert movie["title"] in customer["movies"]
    customer["movies"].remove(movie["title"])
    return customer

def add_seat(movie):
    """Add seat back to database"""
    movie["seats_avaliable"] = movie["seats_avaliable"] + 1
    return movie

def print_movie_data(movie):
    """Prints movie database informations"""
    print("Movie Title:           ", movie["title"])
    print("Seats Remaining:       ", movie["seats_avaliable"])

def print_customer_data(customer): #movies have brackets around them
    """Prints customer database information"""
    movie_list = customer_db()
    print("Movie Tickets:         ", customer["movies"])
    print("Account Balance:       ", customer["cash"])

def print_all_movie_data():
    """Print all movie data raw"""
    __movies__ = movie_db()
    pprint.pprint(__movies__)

def print_all_customer_data():
    """Print all customer data raw"""
    __customers__ = customer_db()
    pprint.pprint(__customers__)
