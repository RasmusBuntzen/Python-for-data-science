input = open("british-english.txt","r") #imports the file
lines = input.readlines() #Reads alle the lines ito a list
import re
pattern = re.compile(r"(\b[a-z]).*\1\b[^']",re.IGNORECASE) #Patternet tager det førstbogstav og gemmer det i group 1 .* matcher alle bogstaverne i ordet (pånår første og sidste)
# \b referere til group1 og siger at sidste bogstav skal være det samme som første bogstav
#\b[^'] undgår ord der slutter på ...'s
for line in lines: #Runs the loop once for each line
    if pattern.match(line): #hvis linjen matcher patternet printes den
        print(line)
