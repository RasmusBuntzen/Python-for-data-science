import pandas as pd
import re
import numpy as np
from string import ascii_lowercase
from string import ascii_uppercase
import matplotlib.pyplot as plt
print("Øvelse 1")
pd_range = pd.Series(range(0,100)) # Hvis der ikke angives index navne er det bare 0, 1, 2 osv
print(pd_range)
pd_string = pd_range.astype("string")
print(pd_string)
print(len(pd_string))

print("\Øvelse 2")
words_data = pd.read_table("british-english.txt", keep_default_na=False)
print(words_data) # Default hedder rækker tal og col bogstaver
words_data.columns = ["Words"] #ændre navn på col
print(words_data)
pattern = re.compile('\A([aA].*)') # Laver en regular expression der leder efter ord der starter med a eller A
i=0
# while i < len(words_data):
#     match = pattern.search(words_data.loc[i,"Words"]) #Tjekker værd række om det matcher pattern"
#     if  match != None: #Hvis match ikke er None betyder det der er et match, som derefter printes
#         print(match.group(1))
#     i=i+1

#Dette kan gøre lette vha extract
print(words_data.Words.str.extract(pattern).dropna()) #dataframen og hvilken col der arbejdes med defineres, den trnasformeres til str, og der extractes efter pattern, dropna fjerne alle Nan værdier (altså der hvor der ikke er et match)


print("\nØvelse 3")
words_grps = words_data.groupby(words_data.Words.str[0])
x = 0
alpha = ascii_uppercase+ascii_lowercase+"Å"+"é" #Alpfabetet med stor , alfabetet med lille så Å og é
for Words,grp in words_grps:
    print(alpha[x],":",len(grp)) #Prints what is grouped by (first letter) and the number of entries in the group
    x = x+1

print("\nØvelse 4")
words_grps = words_data.groupby(words_data.Words.str[0])
alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z Å é"
alpha_list = alpha.split(" ")
df =pd.DataFrame()
list = []
for Words,grp in words_grps:
    length = len(grp)
    list.append(length)
np_array = np.array(list).reshape(54,1)

df = pd.DataFrame(np_array,index=alpha_list,columns=["Length"])
print(df)
df.plot.hist()
plt.show()




