import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def decision(probability):
    return rnd.random() < probability

def analitical(a_money, b_money, p_range):
    z = a_money + b_money
    P_ruin_A = []
    for p in p_range:
        if p == 0.5:
            P_ruin_A.append(1 - a_money / z)
        else:
            q = 1 - p
            numerator = (q/p)**a_money - (q/p)**z
            denominator = 1 - (q/p)**z
            P_ruin_A.append(numerator/denominator)

    return P_ruin_A



def game_simulation(p_A, a_money, b_money):
    while a_money > 0 and b_money > 0:
        if decision(p_A):
            a_money = a_money + 1
            b_money = b_money - 1
        else:
            a_money = a_money - 1
            b_money = b_money + 1

    return a_money > 0


p_A = np.arange(0.4, 0.6, 0.01)
P_Ruin_A = []
a_money = 50
b_money = 50
games_num = 500
for p_A_i in p_A:
    aWins = 0
    for k in range(0, games_num):
        if game_simulation(p_A_i, a_money, b_money):
            aWins = aWins + 1
    P_Ruin_A.append((games_num - aWins)/games_num)

plt.scatter(p_A, P_Ruin_A)
plt.plot(p_A, analitical(a_money, b_money, p_A))
plt.grid(True)
plt.title("A player Ruin")
plt.xlabel("p_a")
plt.ylabel("P(ruin A)")

plt.show()
