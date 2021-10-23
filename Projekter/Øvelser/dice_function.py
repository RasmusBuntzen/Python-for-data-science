# import random
#
# def die():
#     x = random.random
#     return 1+int(x*6)
#
# def dice():
#     d1 = die()
#     d2 = die()
#     return d1+d2
#
# print(dice())

"""vi ser at når x = random.random køres bliver x ikke defineret ordentlig (den får ikke en værdi)
Dette skyldes at der manglere parenteser efter random funktionen"""

import random

def die():
     x = random.random()
     return 1+int(x*6)

def dice():
     d1 = die()
     d2 = die()
     return d1+d2

print(dice())