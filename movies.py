"""Movie ticket processing system and database"""

MOVIE_PRICE = 5.0

def enough_money(customers):
    """Check if customer has adequate funds"""
    if customers["cash"] < 5.0:
        return False
    return True

    #   customer[customer]["cash"] = customer[customer]["cash"] - 5.0
     #  customer[customer]["movies"].append("movies");
      # return True

if __name__ == "__main__":
    CUSTOMERS = {
        "Bob" : {"movies":[],
                 "cash" : 100.0},
        "Jim" : {"movies": ["Xmen 8: The Xmennening"],
                 "cash" : 10.0},
        "Cary" : {"movies": ["Gigli: The Play: The Book: The movie", "The Bromance"],
                  "cash" : 120.0},
        "Ricci": {"movies": [],
                  "cash" : 4.0}
    }
    MOVIES = {
        "Xmen 8: The Xmennening": 10,
        "The Bromance" : 20,
        "Gigli: The Play: The Book: The movie" : 102
    }
