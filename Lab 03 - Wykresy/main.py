import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd


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
    ax.plot(x, density_function(x, 0, 1), ".r")
    ax.plot(x, density_function(x, -2, 2), ":b")
    ax.plot(x, density_function(x, 3, 3), "--g")
    ax.plot(x, density_function(x, 4, 4), "xk")
    return fig, ax


def zadanie_2(fig, ax: matplotlib.axes._subplots.Axes):
    ax.set_ylim(0, 1)
    ax.set_xlim(-5, 5)
    ax.set_xticks(np.arange(-5, 5, 0.5), minor=True)
    ax.set_ylabel("f(x)")
    ax.set_title("Rozkład Gaussa", fontsize=16)
    ax.grid()
    ax.legend(["u = 0, o = 1", "u = -2, o = 2", "u = 3, o = 3", "u = 4, o = 4"], loc='upper left')
    plt.show()


def main():
    # matplotlib_learning()
    figure, axes = zadanie_1()
    zadanie_2(figure, axes)
    # NOW GRUPOWANIE WYKRESÓW SŁUPKOWYCH


if __name__ == '__main__':
    main()
