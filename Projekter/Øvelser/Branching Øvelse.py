import random
x = random.random()  #Generate random number between 0 and 1
if x < 1/6: #Hvis x er mindre en 1/6 print 1
    print(1)
elif x < 2/6: #hvis x er mindre end 2/6 (og større end 1/6 somtestet på linje 3) print 2
    print(2)
elif x < 3/6:
    print(3)
elif x < 4/6:
    print(4)
elif x < 5/6:
    print(5)
else:
    print(6)
#Jeg laver opgaven nested (altså med under kriterier
height  = random.randint(80,180) # giver en tilfældig integer (heltal) mellem 80 og 180
if height < 120: #Hvis du er lavere end 120 kan du ikke køre forlystelsen
    print("Du kan ikke køre forlystelsen")
else:
    if height < 130: #Du når kun hertil hvis du er højere end 120, hvis du samtidig er lavere end 130 skal der være en vosken
        print("Du kan kun køre forlystelsen akkompagneret med en voksen")
    else: #Her når du til hvis du er højere end 120 OG 130, og du kan derfor køre forlystelsen alene.
        print("Tillyke, du kan køre forlystelsen alene")
#Bruger nu if elif else
if height < 120:
    print("Du kan ikke køre forlystelsen")
elif height < 130:
    rint("Du kan kun køre forlystelsen akkompagneret med en voksen")
else:
    print("Tillyke, du kan køre forlystelsen alene")