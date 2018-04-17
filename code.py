"""This code is for a Miovie Ticketing System"""

CASH = 5.0
MOVIE_DB = {"Xmen 8: The Xmennening": 10, "The Bromance" : 20,
            "Gigli: The Play: The Book: The movie" : 102}
MOVIEGOERS = {"Bob" : {"movies":[], "cash":100.0},
              "Jim" : {"movies": ["Xmen 8: The Xmennening"], "cash":10.0},
              "Cary" : {"movies": ["Gigli: The Play: The Book: The movie",
                                   "The Bromance"], "cash":120.0},
              "Ricci": {"movies": [], "cash":4.0}}

def purchase(movie, moviegoer):
    """Purchase Ticket Function"""

    MOVIE_DB[movie] = MOVIE_DB[movie] - 1
    if MOVIEGOERS[moviegoer]["cash"] > 5.0:

        MOVIEGOERS[moviegoer]["cash"] = MOVIEGOERS[moviegoer]["cash"] - 5.0
        MOVIEGOERS[moviegoer]["movies"].append(movie)

        return True

def test_purchase():
    """Test Purchase Function"""

    purchase("Xmen 8: The Xmennening", "Ricci")

    assert MOVIE_DB["Xmen 8: The Xmennening"] == 9
