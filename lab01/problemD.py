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
    return L_prob


result1 = calculate_prob(1/2, 50, 50, 5000)
result2 = calculate_prob(1/5, 50, 50, 100000)
result3 = calculate_prob(4/5, 50, 50, 100000)

plt.figure(1)
plt.hist(result2, 50, normed=1)
plt.grid(True)
plt.title("pn = 1/5")
plt.xlabel("L")
plt.ylabel("P(L)")

plt.figure(2)
plt.hist(result1, 50, normed=1)
plt.grid(True)
plt.title("pn = 1/2")
plt.xlabel("L")
plt.ylabel("P(L)")

plt.figure(3)
plt.hist(result3, 50, normed=1)
plt.grid(True)
plt.title("pn = 4/5")
plt.xlabel("L")
plt.ylabel("P(L)")
plt.show()
