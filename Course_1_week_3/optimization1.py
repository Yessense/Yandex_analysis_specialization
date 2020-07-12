from math import sin, exp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

np.set_printoptions(suppress=True)

x = np.arange(1, 30, 0.1)
# print(x)
# print(x)
y = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
# print(y)
plt.plot(x, y)
plt.show()


def f(z):
    return sin(z / 5) * exp(z / 10) + 5 * exp(-z / 2)


res = minimize(f, x0=2)
print(res.x, res.fun)

res = minimize(f, x0=2, method='BFGS')
print(res.x, res.fun, f(res.x))
res2 = minimize(f, x0=30, method='BFGS')

file = open('result1.txt', 'w')
file.write(f'{round(res.fun,2)} {round(res2.fun,2)}')
file.close()
