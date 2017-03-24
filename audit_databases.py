"""Functions avaliable for printing individual data as well as all movies and customer data"""

def print_movie_data(movie):
    """Prints movie database informations"""
    print("Movie Title:           ", movie["title"])
    print("Seats Remaining:       ", movie["seats_available"])

def print_customer_data(customer):
    """Prints customer database information"""
    print("Movie Tickets:         ", ",  ".join(customer["movies"]))
    print("Account Balance:       ", customer["cash"])

def print_all_movie_data(movie_dictionary):
    """Print all movie data raw"""
    for details in movie_dictionary.values():
        print_movie_data(details)
    print("")

def print_all_customer_data(customer_dictionary):
    """Print all customer data raw"""
    for details in customer_dictionary.values():
        for name in customer_dictionary.keys():
            print(name)
            print_customer_data(details)
            print("")
        return
