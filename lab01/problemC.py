import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def decision(probability):
    return rnd.random() < probability

def analitical(z, a_range):
    P_ruin_A = []
    for a_money in a_range:
        P_ruin_A.append(1 - a_money / z)
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


z = 20
a_range = np.arange(0, z, 0.5)
P_Ruin_A = []
games_num = 500
for a_money in a_range:
    aWins = 0
    for k in range(0, games_num):
        if game_simulation(0.5, a_money, z - a_money):
            aWins = aWins + 1
    P_Ruin_A.append((games_num - aWins)/games_num)

plt.scatter(a_range, P_Ruin_A)
plt.plot(a_range, analitical(z, a_range))
plt.grid(True)
plt.title("A player Ruin")
plt.xlabel("a")
plt.ylabel("P(ruin A)")

plt.show()
