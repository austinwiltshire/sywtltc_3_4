MOVIE_PRICE = 5.0

movie = {
"Xmen 8: The Xmennening": 10,
"The Bromance" : 20,
"Gigli: The Play: The Book: The movie" : 102
}

customer = {
"Bob" : {"movies":[], "cash" : 100.0},
"Jim" : {"movies": ["Xmen 8: The Xmennening"], "cash" : 10.0},
"Cary" : {"movies": ["Gigli: The Play: The Book: The movie", "The Bromance"], "cash" : 120.0},
"Ricci": {"movies": [], "cash" : 4.0}
}


def purchase_ticket(movie, customer):
    _mv_db[mv] = _mv_db[mv] - 1
    if _mvg_d[mvg]["cash"] > 5.0:
        _mvg_d[mvg]["cash"] = _mvg_d[mvg]["cash"] - 5.0; _mvg_d[mvg]["movies"].append(mv); return True
    return False
def tesst():
    do_p("Xmen 8: The Xmennening", "Ricci")
    assert _mv_db["Xmen 8: The Xmennening"] == 10 #WTF?
