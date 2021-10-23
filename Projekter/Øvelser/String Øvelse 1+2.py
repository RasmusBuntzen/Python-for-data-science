#Øvelse 1
First_name = "Rasmus"
Last_name = "Buntzen"
Age = 22
print("Name: " + First_name + " " + Last_name + "\nAge: "+ str(Age))

#Øvelse 2
DNA = "AAGCAGAATGCTTAGGACTAGTTAC"
RNA = DNA.replace("T","U")
print("DNA sekvensen :"+DNA)
print("RNA sekvensen :"+RNA)
print("Længden af RNA sekvensen er: "+ str(len(RNA)) + "\nDen miderste base er: " +RNA[len(RNA)//2]) #I use // because the length is uneven and therefore return a float
print("")