import matplotlib.pyplot as plt
import numpy as np
print("Øvelse 1")
terning_kast = np.random.randint(1,7,10000)+np.random.randint(1,7,10000)
plt.hist(terning_kast,11) #laver et histogram (11 betyder at x-aksen er inddelt i 11 enheder)
plt.show()
#Det giver en normalfordeling som forventet

print("\nØvelse 2")
data = np.genfromtxt("fern_data.txt")
plt.scatter(data[:,0],data[:,1],edgecolors=None,s=0.5,color="Green")#Først sættes x og y værdierne, derefter fjernes edgdecolor, så sættes point størrelsen til 0.5, og punkternes farve ændres til grøn
plt.axis('off') #Akserne fjernes
plt.show()