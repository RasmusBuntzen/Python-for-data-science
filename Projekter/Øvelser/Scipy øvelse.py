import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -(np.cos(x)+np.sin(2*x))

res = scipy.optimize.minimize(f,0.0,method="powell") #Startvalue = 0.0
res2 = scipy.optimize.minimize(f,-2,method="powell") #Startvalue = -2
x = np.arange(-10,10,0.1)
plt.plot(f(x))
plt.show()
print(res.x) #.x printer kun x værdien
print(res2.x)