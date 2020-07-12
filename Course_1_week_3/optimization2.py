from scipy.optimize import differential_evolution
from math import sin, exp


def f(z):
    return sin(z / 5) * exp(z / 10) + 5 * exp(-z / 2)


def h(z):
    return int(f(z))


res = differential_evolution(f, [(1, 30)])
print(res.x, res.fun)

file = open('result2.txt', 'w')
file.write(f'{round(res.fun, 2)}')
file.close()
