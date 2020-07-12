from scipy.optimize import differential_evolution
from scipy.optimize import minimize
from math import sin, exp
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 30, 0.1)
y =np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
y = np.round(y)
plt.plot(x, y)
plt.show()



def f(z):
    return sin(z / 5) * exp(z / 10) + 5 * exp(-z / 2)


def h(z):
    return int(f(z))

res1 = minimize(h,x0=30,method='BFGS')
res2 = differential_evolution(h, [(1, 30)])

print(res1.x, res1.fun)
print(res2.x, res2.fun)

file = open('result3.txt', 'w')
file.write(f'{round(res1.fun, 2)} {round(res2.fun, 2)}')
file.close()
