import sqlite3
import requests
import json
import pandas as pd
import time
import matplotlib.pyplot as plt


def learning_sqlite():
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")  # połączenie do bazy danych - pliku
    c = conn.cursor()

    # for row in c.execute('SELECT ArtistId, Name FROM Artist WHERE ArtistID BETWEEN 20 and 40 ORDER BY Name'):
    #     print(row)

    # zadanie 1
    # for row in c.execute('SELECT InvoiceId, CustomerId, BillingCity, Total FROM Invoice WHERE BillingCountry LIKE "USA" ORDER BY BillingCity DESC'):
    #     invoiceID, customerID, city, total = row
    #     print("invoice:", invoiceID, "customer:", customerID, "city:", city, "total:", total)

    # Zadanie 2
    for row in c.execute(
            'SELECT Artist.Name, Album.Title FROM Artist INNER JOIN Album ON Album.ArtistId = Album.ArtistId'):
        print(row)
    conn.close()


def restAPI_learning():
    req = requests.get(
        "https://blockchain.info/ticker")  # wysłanie zapytania GET pod odpowiedni adres, zapisanie odpowiedzi
    bitcoin_dict = json.loads(req.text)

    # Zadanie 3
    bitcoin_dataFrame = pd.DataFrame(bitcoin_dict.values(), index=bitcoin_dict.keys())
    print(bitcoin_dataFrame)


def OpenWeather_API():
    # file = json.loads(open("/home/barxtex/PycharmProjects/secrets/openweather_pass.json", "r").read())
    # url = "https://api.openweathermap.org/data/2.5/onecall"
    # api_key = file["api"]
    # latitude = 52.406376
    # longitude = 16.925167
    # units = "metric"
    # req = requests.get(f"{url}?lat={latitude}&lon={longitude}&units={units}&exclude=minutely&appid={api_key}")

    # Zadanie 4
    # weather_pz = open("weather_poznan.json", "w")
    # weather_pz.write(req.text)
    # weather_pz.close()

    # first method
    weather_pz = json.loads(open("weather_poznan.json", "r").read())
    weather_hourly = weather_pz["hourly"]
    weather_dataFrame = pd.DataFrame(data=weather_hourly)
    weather_dataFrame["dt"] = pd.to_datetime(weather_dataFrame["dt"], unit='s')
    weather_dataFrame.set_index(weather_dataFrame["dt"], inplace=True)
    weather_dataFrame = weather_dataFrame.loc[:, ["temp", "feels_like", "humidity", "wind_speed"]]

    # second method
    # weather_pz = json.loads(open("weather_poznan.json", "r").read())
    # weather_hourly = weather_pz["hourly"]
    # index_array = [pd.to_datetime(weather_hourly[i]["dt"], unit='h') for i in range(len(weather_hourly))]
    # weather_dataFrame = pd.DataFrame(data=weather_hourly, index=index_array)
    # weather_dataFrame = weather_dataFrame.loc[:, ["temp", "feels_like", "humidity", "wind_speed"]]
    # print(weather_dataFrame)
    weather_dataFrame.plot()
    plt.show()


def main():
    # learning_sqlite()
    # restAPI_learning()
    OpenWeather_API()


if __name__ == '__main__':
    main()
