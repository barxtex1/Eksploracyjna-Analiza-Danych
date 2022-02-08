import matplotlib.pyplot as plt
import numpy as np


def learning_proces():
    ## basic plot
    x = np.linspace(0, 2, 100)
    fig, ax = plt.subplots()
    ax.plot(x, x)
    ax.plot(x, x ** 2)
    ax.plot(x, x ** 3)
    plt.show()

def zadanie_1():
    x = np.linspace(-5, 5, 100)
    std_dev = 2
    std_dev2 = 1
    std_dev3 = 3
    std_dev4 = 4
    mean = -2
    mean2 = 0
    mean3 = 3
    mean4 = 4
    f = (1 / (std_dev * np.sqrt(np.pi))) * np.exp((-(x - mean) ** 2) / (2 * std_dev))
    f2 = (1 / (std_dev2 * np.sqrt(np.pi))) * np.exp((-(x - mean2) ** 2) / (2 * std_dev2))
    f3 = (1 / (std_dev3 * np.sqrt(np.pi))) * np.exp((-(x - mean3) ** 2) / (2 * std_dev3))
    f4 = (1 / (std_dev4 * np.sqrt(np.pi))) * np.exp((-(x - mean4) ** 2) / (2 * std_dev4))
    fig, ax = plt.subplots()
    ax.plot(x,f,':b')
    ax.plot(x,f2,'or')
    ax.plot(x,f3,'--g')
    ax.plot(x,f4,'xk')
    plt.show()



if __name__ == '__main__':
    # learning_proces()
    zadanie_1()