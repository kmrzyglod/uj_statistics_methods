import matplotlib.pyplot as plt
import random as rnd
import math
import numpy as np


# Fixing random state for reproducibility

def graph(formula, x_range):
    args = np.array(x_range)
    values = []
    for x in args:
        values.append(eval(formula))
    return args, values


def box_muller(num):
    iterations = int(0.5 * num if num % 2 == 0 else 0.5 * (num + 1))
    result = []
    for i in range(iterations):
        u = rnd.uniform(0, 1)
        v = rnd.uniform(0, 1)
        x = math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)
        y = math.sqrt(-2 * math.log(u)) * math.sin(2 * math.pi * v)
        result.append(x)
        result.append(y)
    if len(result) > num:
        result.pop()
    return result


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
            x = u * math.sqrt(-2 * math.log(s) / s)
            y = v * math.sqrt(-2 * math.log(s) / s)
            return x, y


x, y = graph("1/math.sqrt(2 * math.pi) * math.exp(-x**2/2)", np.arange(-4.0, 4.0, 0.01))

plt.figure(1)
gaussian_numbers_box_muller = box_muller(1000)
plt.hist(gaussian_numbers_box_muller, 100, normed=1)
plt.plot(x, y)
plt.grid(True)
plt.title("Gaussian Histogram Box-Muller")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.figure(2)
gaussian_numbers_polar = polar(1000)
plt.hist(gaussian_numbers_polar, 100, normed=1)
plt.plot(x, y)
plt.grid(True)
plt.title("Gaussian Histogram Polar")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()