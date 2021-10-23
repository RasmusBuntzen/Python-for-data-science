# Dette projekt handler om recursion
# recursion er en funktion der kalder sig selv

# Jeg vil bruge recursion til at udregne factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("What number do you want the factorial of? "))
print(f"The factorial of {num} is {factorial(num)}")

#Denne video forklare det ret godt https://www.youtube.com/watch?v=qXg6xwAhtKo

#Lad os sige vi vil finde factorial af 3
#i linje 10 bliver det til 3 * factorial(2), programmet finder nu ud af hvad factorial(2) er ved at køre funktionen
#Igen i linje 10 får vi at factorial(2) er 2 * factorial(1), programmet finder nu ud af hvad factorial(1) er
#I linje 10 finder vi ud af factorial(1) er 1 * factorial(0),programmet finder nu ud af hvad factorial(0) er
#Nu er n 0 og der returneres 1, så factorial(0) = 1
#dette betyder factorial(1) = 1*1 = 1
#factorial(2) = 2*1 = 2
#Og factorial(3) = 3*2 = 6
