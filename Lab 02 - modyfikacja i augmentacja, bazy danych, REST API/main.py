import sqlite3
import requests
import pandas as pd
import json
from password import API


# conn = sqlite3.connect("Chinook_Sqlite.sqlite")  # połączenie do bazy danych - pliku
# c = conn.cursor()

## zad1
# command = 'SELECT InvoiceId, CustomerId, BillingCity, Total FROM Invoice WHERE BillingCountry = "USA"'
# for InvoiceId, CustomerId, BillingCity, Total in c.execute(command):
#     print("invoice:" ,InvoiceId , "customer: ",CustomerId, "city: ", BillingCity, "total: ", Total)
##

# command = 'SELECT Track.Name, Album.Title ' \
#           'FROM Track ' \
#           'INNER JOIN Album ON Track.AlbumId = Album.AlbumId'
# for Name, Title in c.execute(command):
#     print("Song name: ",Name,"- Album title: ",Title)

## zad2
# command = 'SELECT Artist.Name, Album.Title ' \
#           'FROM Album ' \
#           'LEFT JOIN Artist ON Artist.ArtistId = Album.ArtistId'
# for Name, Title in c.execute(command):
#     print("Artist name: ",Name,"- Album title: ",Title)
#
# conn.close()
##
# req = requests.get("https://blockchain.info/ticker")
# bitcoin_dict = json.loads(req.text)
#
#
# ## zad3
# df = pd.DataFrame(data=bitcoin_dict.values(),index=bitcoin_dict.keys(), columns=["15m","last","buy", "sell", "symbol"])
# print(df)
# ##

# url = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = API
# latitude = 37.2431
# longitude = -115.7930
# req = requests.get(f"{url}?lat={latitude}&lon={longitude}&exclude=minutely&appid={api_key}")
# print(req.text)
# data = json.loads(req.text)
# with open('weather_forecast.json', 'w') as outfile:
#     json.dump(data, outfile)


#### ZAD4
url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = API
latitude = 53.169558090827394
longitude = 15.421173151897403
req = requests.get(f"{url}?lat={latitude}&lon={longitude}&lang=pl&units=metric&exclude=daily&appid={api_key}")
data = json.loads(req.text)
data_hourly = json.dumps(data["hourly"])
print(data_hourly["dt"])
# df = pd.DataFrame(data_hourly.values(),index=data_hourly.keys(),columns=[])
# print(df)