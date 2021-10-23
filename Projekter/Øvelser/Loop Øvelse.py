list = [6,9,4,8,7,1,2]

print("Opgave 2")
i = 1 #starter på 1 da len() funktionen starter med længde 1 og ikke 0
while i < len(list):
    print(list[i])
    i += 1

print("\nOpgave 3")
for j in list:
    print(j)

print("\nOpgave 4")
for j,val in enumerate(list): #j er indices 0,1,2,3.... val er værdien af hver indice så j=o val=6
    if j>0 and  list[j-1] < val: #hvis værdien på pladsen til venstre for den nuværende værdi er mindre, print val,
        # den vil tage 6 med da den kigger på plads -1 (2), så for at undgå dett skriver jeg j>0
        print(val)
#Opgave 4 kan også løses uden enumerate
print("\n")
for k in range(len(list)): #laver en list med samme længde som list [0,1,2,3,4,5,6]
    if k>0 and list[k-1] < list[k]: #samme som linje 15
        print(list[k])