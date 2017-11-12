import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def decision(probability):
    return rnd.random() < probability

def game_simulation(p_A, a_money, b_money):
    a_wins = 0
    a_wins_table = []
    while a_money > 0 and b_money > 0:
        if decision(p_A):
            a_money = a_money + 1
            b_money = b_money - 1
            a_wins = a_wins + 1
        else:
            a_money = a_money - 1
            b_money = b_money + 1
        a_wins_table.append(a_wins)
    return a_wins_table


result = game_simulation(1/5, 50, 50)
plt.plot(range(0, len(result)), result)
plt.grid(True)
plt.title("trajectory")
plt.xlabel("num of game")
plt.ylabel("wins")

plt.show()
