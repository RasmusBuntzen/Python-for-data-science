triplet = (1,2,3)
x,y,z = triplet
print(x,y,z)
quartet = (1,2,3,4)
"""x,y,z = quartet
Giver fejl "too many values to unpack" fordi jeg danner 3 variabler men prøver at assigne 4 ting"""
x,y,z = quartet[1:4]
print(x,y,z)