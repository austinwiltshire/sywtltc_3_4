"""Tests for Code.py"""

import revised_code

def test_revised_code():
    """Test Purchase Function"""

    revised_code.purchase("Xmen 8: The Xmennening", "Ricci")

    assert revised_code.MOVIE_DB["Xmen 8: The Xmennening"] == 10
    assert revised_code.MOVIEGOERS["Ricci"]["cash"] == 4
    assert revised_code.MOVIEGOERS["Ricci"]["tickets"] == 0

    revised_code.purchase("The Bromance", "Cary")

    assert revised_code.MOVIE_DB["The Bromance"] == 19
    assert revised_code.MOVIEGOERS["Cary"]["cash"] == 115.0
    assert revised_code.MOVIEGOERS["Cary"]["tickets"] == 1

    revised_code.refund("The Bromance", "Cary")

    assert revised_code.MOVIE_DB["The Bromance"] == 20
    assert revised_code.MOVIEGOERS["Cary"]["cash"] == 120.0
    assert revised_code.MOVIEGOERS["Cary"]["tickets"] == 0
