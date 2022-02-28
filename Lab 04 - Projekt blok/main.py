import pandas as pd
import numpy as np


def new_frequency_columns(df, when):
    df = pd.pivot_table(df, values="number", index=["sex", "name"], aggfunc=np.sum)
    df.loc["M", "frequency_male"] = (df["number"] * when) / len(df.loc["M", :])
    df.loc["F", "frequency_female"] = (df["number"] * when) / len(df.loc["F", :])
    return df


def import_data():
    all_data = pd.DataFrame()
    for i in np.arange(1880,2021):
        simple_data = pd.DataFrame(pd.read_csv("names/yob" + str(i) + ".txt", names=["name", "sex", "number"],
                                               index_col=0))
        simple_data = new_frequency_columns(simple_data, int(i))
        all_data = pd.concat([all_data, simple_data])
    data_ = pd.pivot_table(all_data, values=["number", "frequency_male", "frequency_female"], index=["sex", "name"], aggfunc=np.sum)
    return data_


def processing(df):
    print("Liczba różnych (unikalnych) imion: ", len(df.loc[df["number"] == 5, :]))  # "To safeguard privacy, we restrict our list of names to those with at least 5 occurrences."
    print("Liczba różnych (unikalnych) imion rozróżniając płeć: male -", len(df.loc[("M", df["number"] == 5), :]), "female -", len(df.loc[("F", df["number"] == 5), :]))
    print(df)


if __name__ == '__main__':
    data = import_data()
    processing(data)
