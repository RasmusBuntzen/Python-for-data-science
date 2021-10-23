print("Øvelse 1")
class MyInfo:
    def initialize(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def print(self):
        print("Name: ", self.firstname, self.lastname, "\nAge:  ", self.age)
info = MyInfo()
info.initialize("Rasmus","Buntzen",22)
info.print()

print("\nØvelse 2")
class MyInfo1:
    def __init__(self,firstname, lastname, age): #Dette er en metode der altid starter når classen køres (defineres som object).
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print(self):
        print("Name: ", self.firstname, self.lastname, "\nAge:  ", self.age)
info1 = MyInfo1("Rasmus","Buntzen",22)
info1.print()