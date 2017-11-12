import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def decision(probability):
    return rnd.random() < probability

def game_simulation(p_A, a_money, b_money):
    num_of_games = 0
    while a_money > 0 and b_money > 0:
        if decision(p_A):
            a_money = a_money + 1
            b_money = b_money - 1
        else:
            a_money = a_money - 1
            b_money = b_money + 1
        num_of_games = num_of_games + 1

    return num_of_games


def calculate_prob(p_a, a_money, b_money, games_num):
    L_prob = []
    for i in range(0, games_num):
        L_prob.append(game_simulation(p_a, a_money, b_money))
    return max(L_prob)



p_range = np.arange(0.4, 0.6, 0.02)
L_max = []
a_money = 50
b_money = 50
num_of_games = 1000
for p in p_range:
    L_max.append(calculate_prob(p, a_money, b_money, num_of_games))

plt.scatter(p_range, L_max)
plt.grid(True)
plt.title("Max L")
plt.xlabel("p_a")
plt.ylabel("L_max")


plt.show()
