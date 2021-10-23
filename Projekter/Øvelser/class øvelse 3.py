print("Øvelse 3")
class person:
    """Overordnet class. Indeholder navn og person nummer"""
    def __init__(self,navn,nummer):
        self.navn = navn
        self.nummer = nummer
class student(person):
    """Specialiseret class kun for students. Indeholder studie og karakterer"""
    def __init__(self,navn,nummer,studie, karakterer): # Laver en constructor (Husk den skal indolde variablerne fra den arvede constructor)
        person.__init__(self,navn,nummer) #Loader den arvede constructor
        self.studie = studie
        self.karakterer = karakterer
    def print_data(self):
        print("Navn: ", self.navn,"\nNummer: ",self.nummer, "\nStudie: ",self.studie,"\nKaratkerer: ", self.karakterer)
rasmus = student("Rasmus Bunzten", "NBM883", "Biologi",[12,10,10,12,12])
rasmus.print_data()

print("\nØvelse 4")
class StudentGroup:
    def __init__(self,students=[]):
        self.students = students
    def AddStudents(self,AddedStudent):
        self.students.append(AddedStudent)
    def PrintStudents(self):
        print(self.students)
signe = student("Signe frederiksen", "Bla123", "Psykoligi",[12,12,12,12,12])
gruppe = StudentGroup()

gruppe.AddStudents(rasmus)
gruppe.AddStudents(signe)
gruppe.PrintStudents() #Dette viser object koderne og ikke de egentlige navne, humlen er bare at den outputter 2 objects
