"""Functions avaliable for printing individual data as well as all movies and customer data"""

def print_movie_data(movie):
    """Prints movie database informations"""
    print("Movie Title:           ", movie["title"])
    print("Seats Remaining:       ", movie["seats_available"])

def print_customer_data(customer): #movies have brackets around them
    """Prints customer database information"""
    print("Movie Tickets:         ", ",  ".join(customer["movies"]))
    print("Account Balance:       ", customer["cash"])

def print_all_movie_data(movie_dictionary):
    """Print all movie data raw"""
    for movie_dictionary.itervalues():
        print_movie_data(movie_dictionary)
        print("")

def print_all_customer_data(customer_dictionary):
    """Print all customer data raw"""
    for customer, details in customer_dictionary.items():
        print(customer)
        print_customer_data(details)
        print("")
