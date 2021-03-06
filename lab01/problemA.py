import matplotlib.pyplot as plt
import random as rnd
import math
import numpy as np


def graph(formula, x_range):
    args = np.array(x_range)
    values = []
    for x in args:
        values.append(eval(formula))
    return args, values

def polar(num):
    iterations = int(0.5 * num if num % 2 == 0 else 0.5 * (num + 1))
    result = []
    for i in range(iterations):
        x, y = polar_get_pair()
        result.append(x)
        result.append(y)
    if len(result) > num:
        result.pop()
    return result


def polar_get_pair():
    while True:
        u = rnd.uniform(-1, 1)
        v = rnd.uniform(-1, 1)
        s = u ** 2 + v ** 2
        if s < 1:
            x = math.sqrt(-2 * math.log(s)) * (u/math.sqrt(s))
            y = math.sqrt(-2 * math.log(s)) * (v/math.sqrt(s))
            return x, y


x, y = graph("1/math.sqrt(2 * math.pi) * math.exp(-x**2/2)", np.arange(-5.0, 5.0, 0.01))

gaussian_numbers_polar = polar(20000)
plt.hist(gaussian_numbers_polar, 50, normed=1)
plt.plot(x, y)
plt.grid(True)
plt.title("Gaussian Histogram Polar")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()