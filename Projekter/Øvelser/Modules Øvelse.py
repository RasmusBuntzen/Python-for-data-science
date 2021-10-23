def randint():
    return "Hello"
import random
from random import randint as test
print(randint())
print(randint())
print(random.randint(1,6))
print(test(1,6))
from random import * #This overwrites my randint function, and therefore gives an error if i dont input to numbers when i call the function.
print(randint(1,6))
