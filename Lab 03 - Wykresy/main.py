import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd
import json


def density_function(x, mean, std_dev):
    f = (1 / (std_dev * np.sqrt(np.pi))) * np.exp((-(x - mean) ** 2) / (2 * std_dev))
    return f


def matplotlib_learning():
    x = np.linspace(0, 2, 20)
    fig, ax = plt.subplots()
    ax.plot(x, x)
    ax.plot(x, x ** 2, ".--b")
    plt.show()


def zadanie_1():
    x = np.linspace(-5, 5, 50)
    fig, ax = plt.subplots()
    ax.plot(x, density_function(x, 0, 1), ".r", markersize=12)
    ax.plot(x, density_function(x, -2, 2), ":b")
    ax.plot(x, density_function(x, 3, 3), "--g")
    ax.plot(x, density_function(x, 4, 4), "xk")
    return fig, ax


def zadanie_2(fig, ax: matplotlib.axes._subplots.Axes):
    ax.set_ylim(0, 1)
    ax.set_xlim(-5, 5)
    # ax.set_xticks(np.arange(-5, 5, 0.5), minor=True)
    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_xticks(np.arange(-5, 5, 0.5), minor=True)
    ax.set_ylabel("f(x)")
    ax.set_title("Rozkład Gaussa", fontsize=16)
    ax.tick_params(axis="x", which="major", labelrotation=50)
    ax.grid(which='major')
    ax.legend(["u = 0, o = 1", "u = -2, o = 2", "u = 3, o = 3", "u = 4, o = 4"], loc='upper left')
    plt.show()

def zadanie_3():
    file = json.loads(open("cancer_survival_in_us.json", "r").read())
    man = [male['male_survivors'] for male in file["age_groups"]]
    woman = [female['female_survivors'] for female in file["age_groups"]]
    age = [age['age'] for age in file["age_groups"]]
    x = np.arange(len(man))
    width = 0.3
    fig, ax = plt.subplots()
    ax.bar(x - width / 2, man, width, label='Man')
    ax.bar(x + width / 2, woman, width, label='Woman')
    ax.legend()
    ax.set_xticks(x)
    ax.set_xticklabels(age)
    ax.tick_params(axis="x", labelrotation=90)
    ax.set_yticks(np.arange(0, 50, 10))
    ax.set_yticklabels([str(y) + "%" for y in np.arange(0, 50, 10)])
    ax.grid(axis='y')
    ax.set_axisbelow(True)
    # zadanie 4
    ax.errorbar(x - width / 2, man, yerr=np.random.randint(5, size=len(man)), fmt='.k', capsize=2)
    ax.errorbar(x + width / 2, woman, yerr=np.random.randint(5, size=len(woman)), fmt='.k', capsize=2)
    plt.show()

def zadanie_5():
    data = pd.read_csv("russia2020_vote.csv")
    data["za"] = data["yes"]/data["given"]
    fig, ax = plt.subplots(1, 2)
    ax[0].hist(data["za"])
    ax[1].hist(data["za"], 100)
    plt.show()


def main():
    # matplotlib_learning()
    # figure, axes = zadanie_1()
    # zadanie_2(figure, axes)
    # zadanie_3()
    zadanie_5()

if __name__ == '__main__':
    main()
