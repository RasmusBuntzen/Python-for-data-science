print("Øvelse 4")
data = '''# Measurements started
Sep 9, 9:05, T=22deg
SEP 9, 10:15, T=25deg
# Taking a coffee break
Sep 9, 11:15, T=-10deg
# Weekend
Sept 12, 09:00AM, T=32deg
Oct12 13:00, T=32degr'''

import re #importere det rigtige module

data_lines = data.split('\n') #Splitterdataen ind i en list hvor hver item i listen er en linje fra data
pattern = re.compile("([a-z A-Z]+) ?([0-9]+) ?,? ?([0-9]+:[0-9]+[a-z A-Z]*),? T=(-?[0-9]+)[a-z A-Z]+") #Laver en regular expression der matcher de linjer jeg gerne vil have ud

for data_line in data_lines: # laver et loop der køre en gange for værd item i listen data_lines
    if pattern.match(data_line): #hvis den pågælende linje matcher min regular expression så printes linjen
        print(data_line)

print("\nØvelse 5")
for data_line in data_lines: # laver et loop der køre en gange for værd item i listen data_lines
    if pattern.match(data_line): #hvis den pågælende linje matcher min regular expression så gemmes itemet i variablen match
       match = pattern.match(data_line)
       if float(match.group(4)) > -0.1 : #Laver temraturen om til float, hvis temperaturen er over -0.1 (positiv) så printes den
           print(match.group(4))
