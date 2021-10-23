import numpy as np
print("Øvelse 1")
terning_kast = np.average(np.random.randint(1,7,10000)+np.random.randint(1,7,10000)) #Giver gennemsnittet af et array med 10.000 tilfældige tal mellem 1 og 6
print(terning_kast)

print("\nØvelse 2")
data = np.genfromtxt("experimental_results.txt") #Læser data fra filen ind i en array
print("Gennemsnit af kolone 1:",np.average(data[:,0]),"\nGennemsnit af kolone 2:",np.average(data[:,1])) #Printer gennemsnittet af alle entrys i de to koloner seperat

data_subset = data[0:500,1] #Laver et subset der består af de første 500 værdier i kolone 2 (OBS dette subset er nu 1 demisionelt)
#print(data_subset)
data_subset[:]=0 #Sætter alle værdier til 0
#print(data_subset)
print("Gennemsnit af kolone 1:",np.average(data[:,0]),"\nGennemsnit af kolone 2:",np.average(data[:,1])) #Bergener gennemsnit af kolonerne igen
#OBS Se at gennemsnittet ændres! Dette skyldes at når man slicer dannes der ikke en kopi men en reference til det oprindelige data
#Så hvis du ændre i referencen ændre du også det oprindelige data!