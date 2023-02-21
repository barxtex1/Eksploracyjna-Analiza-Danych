import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def example_dataframe():
    num_days = 20
    temperature = np.random.uniform(20, 28, size=(num_days, 1))
    pressure = np.random.uniform(990, 1010, size=(num_days, 1))
    rain = np.random.uniform(0, 20, size=(num_days, 1))
    random_data = np.hstack((temperature, pressure, rain))
    df_weather = pd.DataFrame(index=pd.date_range("20200501", periods=num_days, freq="1D"),
                              data=random_data, columns=["Temperature", "Pressure", "Rain"])
    df_people = pd.DataFrame({"Height": [180, 160, 195],
                              "Weight": [77, 52, 200]})
    df_weather_summary = df_weather.describe()

    # Plot data frame
    df_weather.plot()
    plt.show()

    df_weather.plot(kind='scatter', x='Temperature', y='Rain')
    plt.show()


def testing_dataframe():
    vals = np.random.randn(6, 4)
    print(vals)
    df = pd.DataFrame(vals, index=[0.0, 0.2, 0.3, 0.7, 1.0, 1.3], columns=["A", "B", "C", "D"])
    print(df)
    print(df[0.2:1.0])
    print(df.iloc[0:3, df.columns.get_loc('C')])
    alpha = np.array([0, np.pi / 4, np.pi / 2, np.pi * 3 / 4, np.pi])

    trig = pd.DataFrame({"sinus": np.round(np.sin(alpha), 10),
                         "cosinus": np.round(np.cos(alpha), 10),
                         "x^2": alpha ** 2,
                         "random": np.random.randn(len(alpha))}, index=alpha)
    trig.iloc[1:4, trig.columns.get_loc("random")] = 0
    trig.loc[1337, "cosinus"] = -1
    print(trig)
    rename_dict = {"sinus": "sin", "cosinus": "cos"}

    trig.rename(columns=rename_dict, inplace=True)
    print(trig)
    trig.sort_values("sin", axis=0, inplace=True,
                     ascending=False)  # sortowanie wzdłuż osi 0 (po wierszach), w miejscu, malejąco

    trig.to_csv("trig.csv")
    trig_from_csv = pd.DataFrame(pd.read_csv("trig.csv", index_col=0))  # read_csv() może zwracać nie tylko DataFrame przekazanie do konstruktora usprawni podpowiadanie składni w IDE
    print(trig_from_csv)
    print(type(trig_from_csv))
    print("#############")
    cos = pd.read_csv("trig.csv", index_col=0)
    print(cos)
    print(type(cos))
    print("Czy to to samo:", trig_from_csv == cos)


def final_tasks():
    data = pd.DataFrame(pd.read_csv("population_by_country_2019_2020.csv", index_col=0))
    data["Net population change"] = abs(data["Population (2020)"] - data["Population (2019)"])
    data["Population change [%]"] = (data["Net population change"] / data["Population (2020)"]) * 100
    data.sort_values("Population change [%]", axis=0, inplace=True, ascending=False)
    print(data.iloc[:10, :])
    most_population_change = data.filter(regex=r"Population \(20\d\d\)").iloc[:10, :]
    # most_population_change.plot(kind='bar')
    # plt.show()
    data["Density (2020)"] = "Low"
    print(data.columns)
    data.loc[data["Population (2020)"] / data["Land Area (Km²)"] > 500, "Density (2020)"] = "High"
    data.loc[data["Population (2020)"] / data["Land Area (Km²)"] < 500, "Density (2020)"] = data["Population (2020)"] / data["Land Area (Km²)"]
    print(data.iloc[:10, :])
    data_to_save = data.iloc[::2, :]
    data_to_save.to_csv("population_output.csv")

def main():
    # example_dataframe()
    # testing_dataframe()
    final_tasks()

if __name__ == '__main__':
    main()