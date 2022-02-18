import pandas as pd
import numpy as np


def import_data():
    all_data = pd.DataFrame()
    for i in np.arange(1880,2021):
        simple_data = pd.DataFrame(pd.read_csv("names/yob" + str(i) + ".txt", names=["name", "sex", "number"],
                                               index_col=0))
        all_data = pd.concat([all_data, simple_data])
    data_ = pd.pivot_table(all_data, values="number", index=["sex", "name"], aggfunc=np.sum, sort="number")
    return data_


def processing(df):
    print(df.sort_values("number"))
    print(df.loc[df["number"] == 1, :])


if __name__ == '__main__':
    data = import_data()
    processing(data)
