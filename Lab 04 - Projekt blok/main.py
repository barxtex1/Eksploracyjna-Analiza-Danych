import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def new_frequency_columns(df, when):
    df = pd.pivot_table(df, values="number", index=["sex", "name"], aggfunc=np.sum)
    df.loc["M", "frequency_male"] = (df["number"] * when) / np.sum(df.loc["M", "number"])
    df.loc["F", "frequency_female"] = (df["number"] * when) / np.sum(df.loc["F", "number"])
    return df


def plot_graph(count_of_born, birthrate_sex):
    czas = np.arange(1880, 2021)
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(czas, count_of_born, '-b')
    axs[1].plot(czas, birthrate_sex, '-g')
    for i in range(len(count_of_born)):
        if birthrate_sex[i] == max(birthrate_sex):
            print("Największy stosunek liczby narodzin dziewczynek do liczby narodzin chłopców był w roku", 1880+int(i))
        elif birthrate_sex[i] == min(birthrate_sex):
            print("Najmniejszy stosunek liczby narodzin dziewczynek do liczby narodzin chłopców był w roku", 1880+int(i))
    plt.show()


def most_popular_names(df):
    print("xxx")


def import_data():
    all_data = pd.DataFrame()
    count_of_born_ = []
    birthrate_sex_ = []
    for i in np.arange(1880, 2021):
        simple_data = pd.DataFrame(pd.read_csv("names/yob" + str(i) + ".txt", names=["name", "sex", "number"],
                                               index_col=0))
        simple_data = new_frequency_columns(simple_data, int(i))
        count_of_born_.append(np.sum(simple_data["number"]))
        birthrate_sex_.append(np.sum(simple_data.loc["F", "number"]) / np.sum(simple_data.loc["M", "number"]))
        all_data = pd.concat([all_data, simple_data])
    data_ = pd.pivot_table(all_data, values=["number", "frequency_male", "frequency_female"], index=["sex", "name"], aggfunc=np.sum)
    # plot_graph(np.array(count_of_born_), np.array(birthrate_sex_))
    return data_


def processing(df):
    print("Liczba różnych (unikalnych) imion: ", len(df.loc[df["number"] == 5, :]))  # "To safeguard privacy, we restrict our list of names to those with at least 5 occurrences."
    print("Liczba różnych (unikalnych) imion rozróżniając płeć: male -", len(df.loc[("M", df["number"] == 5), :]), "female -", len(df.loc[("F", df["number"] == 5), :]))
    # print(df)


if __name__ == '__main__':
    data = import_data()
    processing(data)
