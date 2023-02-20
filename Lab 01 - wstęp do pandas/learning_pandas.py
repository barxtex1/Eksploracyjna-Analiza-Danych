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
    # start Modyfikacja zawartości


def main():
    # example_dataframe()
    testing_dataframe()

if __name__ == '__main__':
    main()