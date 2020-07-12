from math import sin, exp
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg
np.set_printoptions(suppress=True)

x = np.arange(1, 16, 0.1)
print(x)
# print(x)
y = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
print(y)

def f(z):
    return sin(z / 5) * exp(z / 10) + 5 * exp(-z / 2)


plt.plot(x, y)

test1 = np.array([[1, 1], [1, 15]])
b1 = np.array([f(1), f(15)])

print(test1, b1)

result1 = scipy.linalg.solve(test1, b1)

print()

# plt.plot([1, 15], test1.dot(result1))

test2 = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 15 ** 2]])
b2 = np.array([f(1), f(8), f(15)])
result2 = scipy.linalg.solve(test2, b2)
print(result2)

# plt.plot([1, 8, 15], test2.dot(result2))
#
test3 = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 15 ** 2, 15 ** 3]])
b3 = np.array([f(1), f(4), f(10), f(15)])
result3: np.array = scipy.linalg.solve(test3, b3)
print(result3)

# plt.plot([1, 4, 10, 15], test3.dot(result3))
new_x = x
new_y = result3[0] + result3[1]* x + result3[2] * x**2 + result3[3]* x**3
plt.plot(new_x, new_y)
print(np.round_(result3, decimals=2))
plt.show()

open('result2.txt', 'w').write('4.36 -1.3 0.19 -0.01')
