#import coin_toss_module #Import the Module
#print(coin_toss_module.coin_toss()) #Call the function

#I now change the location of the module to a other directory (other file)
#New directory is C:\\Users\\Rasmus\\Google Drive\\Uni\\År 2\\Blok 1\\Pyhthon for data science\\Projekter\\my_modules
import sys
directory = "C:\\Users\\Rasmus\\Google Drive\\Uni\\År 2\\Blok 1\\Pyhthon for data science\\Projekter\\my_modules"
sys.path.append(directory)
import coin_toss_module #Import the Module
print(coin_toss_module.coin_toss()) #Call the function
print(sys.path)