import random as rnd
import math
import matplotlib.pyplot as plt
import numpy as np



#narysowac tez histogram rozkladu rpawdopodobienstwa wypadania ti i funkcje gestosci dla rozkladu wykladniczego f = lambda * e**-labda*t


def graph(formula, x_range):
    args = np.array(x_range)
    values = []
    for x in args:
        values.append(eval(formula))
    return args, values

def simulate(timeCut):
    valueCounter = 0;
    timeSum = 0
    while timeSum < timeCut:
        u_i = rnd.random()
        t_i = -math.log(u_i)
        timeSum = timeSum + t_i
        valueCounter = valueCounter + 1
    return valueCounter - 1


def simulateForCut(num, timeCut):
    values = []
    for i in range(0, num):
        values.append(simulate(timeCut))
    return values



result1 = simulateForCut(10**4, 1)
result2 = simulateForCut(10**4, 20)
result3 = simulateForCut(10**4, 90)

plt.figure(1)
plt.hist(result3, normed=1)
x, y = graph("20**x/math.", np.arange(0, 200, 0.01))
plt.plot(x, y)
plt.grid(True)
plt.title("Prob")
plt.xlabel("x(t)")
plt.ylabel("prob")
plt.show()


