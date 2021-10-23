def funktion(x):
    """Tager et tal som indput, hvis tallet er lige printes det hvis ikke raiser funktionen en exception"""
    assert x % 2 == 0
    print(x)
funktion(2)
funktion(5)