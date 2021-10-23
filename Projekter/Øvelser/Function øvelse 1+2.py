print("Øvelse 1")
def terning(antal_kast): #Definere en funktion der tager 1 argument
    """Funktionen tager 1 argument der bestemmer antallet af terning kast. Den printer kastenes resultat"""
    import random # importere random pakken til at generere tal
    for i in range(antal_kast): #kører et loop de antal gange specificeret i argumentet
        x = random.random()# generere et tal mellem 0 og 1 (er inde i parrentesen for at hver kast bliver forskelligt)
        if x < 1/6:
            print(1)
        elif x < 2/6:
            print(2)
        elif x < 3/6:
            print(3)
        elif x < 4/6:
            print(4)
        elif x < 5/6:
            print(5)
        else:
            print(6)

terning(3)

print("\nØvelse 2.1")
#Ændre bare print statments til return
def terning2(antal_kast): #Definere en funktion der tager 1 argument
    """Funktionen tager 1 argument der bestemmer antallet af terning kast. Den returnere kastenes resultat som en string"""
    import random # importere random pakken til at generere tal
    values = []
    for i in range(antal_kast): #kører et loop de antal gange specificeret i argumentet
        x = random.random()# generere et tal mellem 0 og 1 (er inde i parrentesen for at hver kast bliver forskelligt)
        if x < 1/6:
            values.append(1)
        elif x < 2/6:
            values.append(2)
        elif x < 3/6:
            values.append(3)
        elif x < 4/6:
            values.append(4)
        elif x < 5/6:
            values.append(5)
        else:
            values.append(6)
    return(values)
result = terning2(3)
print(result)

print("\nØvelse 2.2")
def terninger_sum(antal_kast):
    """Funktionen tager 1 argument der bestemmer antallet af terning kast. Den returnere kastenes sum"""
    return(sum(terning2(antal_kast))) #Sum() returnere summen af alle elementer i en liste.
print(terninger_sum(2))

print("\nØvelse 3.1")
