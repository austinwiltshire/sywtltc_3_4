"""This code is for a Miovie Ticketing System"""

CASH = 5.0
MOVIE_DB = {"Xmen 8: The Xmennening": 10, "The Bromance" : 20,
            "Gigli: The Play: The Book: The movie" : 102}
MOVIEGOERS = {"Bob" : {"movies":[], "cash":100.0, "tickets": 0},
              "Jim" : {"movies": ["Xmen 8: The Xmennening"], "cash":10.0, "tickets":0},
              "Cary" : {"movies": ["Gigli: The Play: The Book: The movie",
                                   "The Bromance"], "cash":120.0, "tickets":0},
              "Ricci": {"movies": [], "cash":4.0, "tickets":0}}

def purchase(movie, moviegoer):
    """Purchase Ticket Function"""

    if MOVIEGOERS[moviegoer]["cash"] > 5.0: #Check if Moviegoer has enough cash

        MOVIE_DB[movie] = MOVIE_DB[movie] - 1
        MOVIEGOERS[moviegoer]["cash"] = MOVIEGOERS[moviegoer]["cash"] - 5.0
        MOVIEGOERS[moviegoer]["movies"].append(movie)
        MOVIEGOERS[moviegoer]["tickets"] = MOVIEGOERS[moviegoer]["tickets"] + 1

        return True

def refund(movie, moviegoer):
    """Refund Ticket function"""

    if MOVIEGOERS[moviegoer]["cash"] > 5.0:

        MOVIE_DB[movie] = MOVIE_DB[movie] + 1
        MOVIEGOERS[moviegoer]["cash"] = MOVIEGOERS[moviegoer]["cash"] + 5.0
        MOVIEGOERS[moviegoer]["movies"].append(movie)
        MOVIEGOERS[moviegoer]["tickets"] = MOVIEGOERS[moviegoer]["tickets"] - 1
