navn = "Name: {firstname} {lastname},\nAge: {age}".format(firstname = "Rasmus",lastname = "Buntzen",age = 22) #Dette er den nye vej
print(navn)

navn2 = "Name: %(firstname)s %(lastname)s, \nAge %(age)d" % {"firstname":"Rasmus","lastname":"Buntzen","age":22} #Dette er den gamle vej
print(navn2)

"""Hvad gør print(("%s\n"*5)%tuple(range(5)))
%s insætter en string 
\n laver ny linje
* 5 gør det "%s\n" 5 gange
tuple(range(5)) laver en tuple (0,1,2,3,4)

Konklussion
Der printes 0 (linje skift) 1 (linje skift) 2 ... op til 4
"""
print(("%s\n"*5)%tuple(range(5)))
print(("%s\n"*5)%(0,1,2,3,4))