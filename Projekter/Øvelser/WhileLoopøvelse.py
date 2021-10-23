x = 1
#while x < 4: # Da x = 1 og den ikke ændres vil x<4 altid være sandt og loopet vil aldrig slutte
#    print(x)
print("Øvelse 2")
while x <= 4: #Hvis x er 4 eller mindre
    print(5-x) #For at få tallene i omvendt rækkefølge
    x = x+1
x = 1
print("\nØvelse 3")
while x < 10: #Kører hvis x er mindre end 10
    if x % 3 == 0: # Hvis der ikke er nogen rest nor tallet divideres med 3 så print tallet (ellers printes tallet ikke)
        print(x)
    x = x+1