import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

def learning_proces():
    ## basic plot
    # x = np.linspace(0, 2, 100)
    # fig, ax = plt.subplots()
    # ax.plot(x, x)
    # ax.plot(x, x ** 2)
    # ax.plot(x, x ** 3)
    # ax.set_title('Rozkład Gaussa', fontsize=16)
    # plt.show()
    print('')
    ## bar plots
    # fig, ax = plt.subplots()
    # values = [30, 12, 40, 50, 13, 14, 45, 2]
    # x = np.arange(len(values))
    # width = 0.8
    # ax.bar(x, values, width)
    # plt.show()

    ## errorbar
    x = np.linspace(0, 10, 20)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    fig, axs = plt.subplots(2, 1)

    axs[0].plot(x, y_sin)
    axs[0].errorbar(x, y_sin, yerr=0.5, fmt='.k', capsize=2)

    axs[1].plot(x, y_cos)
    axs[1].errorbar(x, y_cos, xerr=0.2, yerr=np.random.random(len(x)), fmt='.r', capsize=2)
    plt.show()

def zadanie_1():
    x = np.linspace(-5, 5, 50)
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
    # fig, ax = plt.subplots()
    # ax.plot(x,f,':b')
    # ax.plot(x,f2,'or')
    # ax.plot(x,f3,'--g')
    # ax.plot(x,f4,'xk')
    return x, [f,f2,f3,f4]


def zadanie_2(x, functions):
    fig, ax = plt.subplots()
    mlk = [':b', 'or', '--g', 'xk']
    for i in range(len(functions)):
        ax.plot(x, functions[i], mlk[i])
        ax.grid(linestyle='-')
        ax.set_title('Rozkład Gaussa', fontsize=16)
        ax.set_xticks(np.arange(-5, 6, 1))
        ax.set_xticks(np.arange(-5, 5, 0.5), minor=True)
        ax.legend(['μ = -2, σ = 2', 'μ = 0, σ = 1', 'μ = 3, σ = 3', 'μ = 4, σ = 4'], loc='upper left')
        ax.set_ylabel("f(x)")
        ax.set_ylim(0, 1)
        ax.set_xlim(-5, 5)
    plt.show()


def zadanie_3():
    json_file = open('cancer_survival_in_us.json', 'r')
    data = json.load(json_file)
    data = data["age_groups"]
    man = []
    woman = []
    labelsx = []
    for d in data:
        man.append(d["male_survivors"])
        woman.append(d["female_survivors"])
        labelsx.append(d["age"])

    x = np.arange(len(man))
    labelsy = ['0%','10%','20%','30%','40%']
    width = 0.4
    fig, ax = plt.subplots()
    ax.bar(x - width / 2, man, width, label='Man')
    ax.bar(x + width / 2, woman, width, label='Woman')
    ax.legend()
    ax.set_xticks(x)
    ax.set_xticklabels(labelsx)
    ax.set_yticks(np.arange(0,50,10))
    ax.set_yticklabels(labelsy)
    ax.tick_params(axis='x', labelrotation=90)
    ax.grid(linestyle='-',axis='y')
    ax.set_axisbelow(True)
    ax.errorbar(x - width / 2, man, yerr=np.random.random(len(x)), fmt='.k', capsize=4)
    ax.errorbar(x + width / 2, woman, yerr=np.random.random(len(x)), fmt='.k', capsize=4)
    plt.show()

def zadanie_5():
    df = pd.DataFrame(pd.read_csv("russia2020_vote.csv"))
    df["relative"] = df["yes"]/df["given"]
    x1 = df["relative"]
    fig, ax = plt.subplots()
    ax.hist(x1,100)
    plt.show()

if __name__ == '__main__':
    # learning_proces()
    # x, f = zadanie_1()
    # zadanie_2(x, f)
    # zadanie_3()
    zadanie_5()
