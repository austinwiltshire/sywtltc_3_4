MOVIE_PRICE = 5.0

def enough_money(customer):
    assert customer["cash"] < 5.0, "Not enough money."

    elif customer[mvg]["cash"] > 5.0:
        customer[mvg]["cash"] = customer[mvg]["cash"] - 5.0
        customer[mvg]["movies"].append(mv);
        return True

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
