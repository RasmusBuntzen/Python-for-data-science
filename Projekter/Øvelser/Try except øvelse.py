try:
    print(hey) #Dette er en name error da den tror hey er en variable og den ikke er defineret
except NameError:
    print("Hov! Husk gåseøjne")

l = [1,2,3,4]
try:
    print(l[4])#Dette er en index error da den index der spørges efter ikke findes (Index error er under lookup error)
except IndexError:
    print("Det index du kigger efter findes ikke")

try:
    print(1/0)#Dette er en zero divison error som er under arithmetic error
except ZeroDivisionError:
    print("Hov! Du må ikke dividere med 0")