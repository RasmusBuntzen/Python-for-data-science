print("Øvelse 3.1")
def coin_toss():
    """Tager 0 argument. Returnere Heads eller tailes (med en fair mønt)"""
    import random
    random_int = random.random() #Generere random tal mellem 0 og 1
    if random_int < 0.5: # Tjekker om tallet er over eller under 0.5 (simulere en 50/50 chance)
        return ("Heads")
    else:
        return ("Tailes")
print(coin_toss())

print("\nØvelse 3.2")
def coin_toss2(prob_of_heads): #Funktionen tager nu et argument
    """Tager 1 argument. Returnere Heads eller tailes (med den sandsynlihed for heads du selv sætter)"""
    import random
    random_int = random.random()
    if random_int < prob_of_heads: #Tjekker om tallet er over eller under det specifiserede tal (simulere den sandsynlighed brugeren har valgt)
        return ("Heads")
    else:
        return ("Tailes")
print(coin_toss2(0.7))

print("\nØvelse 3.3")
def coin_toss2(prob_of_heads=0.5):
    """ Tager 1 argument (valgfri). Returnere Heads eller tailes (med den sandsynlihed for heads du selv sætter, hvis intet argument angives er mønten fair)"""
    import random
    random_int = random.random()
    if random_int < prob_of_heads:
        return ("Heads")
    else:
        return ("Tailes")
print(coin_toss2(1))