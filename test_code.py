"""Tests for Code.py"""

import revised_code

def test_revised_code():
    """Test Purchase Function"""

    revised_code.purchase("Xmen 8: The Xmennening", "Ricci")

    assert revised_code.MOVIE_DB["Xmen 8: The Xmennening"] == 9
