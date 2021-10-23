necessary_var = "hello"
if (len(necessary_var) > 4):
    neccessary_var = necessary_var[:4]  # truncate if length larger than 4
print(necessary_var)

"""Længden af variablen er 5, så den går ind i if statementen
Laver variablen om til kun de første 4 tegn (0,1,2,3)
Printer hell

Når vi kører programmet ser vi at der printes hello

Vi ser i debuggeren at der bliver defineret 2 forskellige variabler, det burde der ikke.
Den første burde bare blive overwritetVi ser det skyles en stavefejl i den anden variables navn."""
print("\nRettet kode")
necessary_var = "hello"
if (len(necessary_var) > 4):
    necessary_var = necessary_var[:4]  # truncate if length larger than 4
print(necessary_var)